#!/usr/bin/env python3
"""
MCP Server Stub

A reference implementation of an MCP server for the learning OS.
Uses only Python standard library.

Usage:
    python server.py [--port PORT]
"""

import json
import os
import re
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import argparse

# Configuration
DEFAULT_PORT = 5000
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
MEMORY_DIR = os.path.join(REPO_ROOT, ".claude", "memory")
MAX_FILE_SIZE = 1024 * 1024  # 1MB
MAX_ENTRY_SIZE = 10 * 1024  # 10KB

# Blocked path patterns
BLOCKED_PATTERNS = [
    r"\.\.",  # Path traversal
    r"\.env",  # Environment files
    r"secret",  # Secret files
    r"credential",  # Credential files
    r"\.git/",  # Git internals
    r"\.key$",  # Private keys
    r"\.pem$",  # Certificates
]

# Allowed memory files for writing
ALLOWED_MEMORY_FILES = [
    "progress_log.jsonl",
    "decisions.jsonl",
    "best_practices.md",
]


def is_path_safe(path: str) -> bool:
    """Check if path is safe to access."""
    path_lower = path.lower()
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, path_lower):
            return False
    return True


def handle_hello(params: dict) -> dict:
    """Handle hello tool call."""
    name = params.get("name", "World")
    return {
        "message": f"Hello, {name}!",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


def handle_read_file(params: dict) -> dict:
    """Handle read_repo_file tool call."""
    path = params.get("path", "")

    if not path:
        raise ValueError("path parameter is required")

    if not is_path_safe(path):
        raise ValueError(f"Path not allowed: {path}")

    # Resolve full path
    full_path = os.path.normpath(os.path.join(REPO_ROOT, path))

    # Verify it's within repo
    if not full_path.startswith(REPO_ROOT):
        raise ValueError("Path outside repository")

    # Check file exists
    if not os.path.isfile(full_path):
        raise FileNotFoundError(f"File not found: {path}")

    # Check file size
    size = os.path.getsize(full_path)
    if size > MAX_FILE_SIZE:
        raise ValueError(f"File too large: {size} bytes (max {MAX_FILE_SIZE})")

    # Read file
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    return {
        "content": content,
        "path": path,
        "size": size
    }


def handle_write_memory(params: dict) -> dict:
    """Handle write_memory_entry tool call."""
    file_name = params.get("file", "")
    entry = params.get("entry", "")

    if not file_name:
        raise ValueError("file parameter is required")

    if not entry:
        raise ValueError("entry parameter is required")

    if file_name not in ALLOWED_MEMORY_FILES:
        raise ValueError(f"File not allowed: {file_name}. Allowed: {ALLOWED_MEMORY_FILES}")

    if len(entry) > MAX_ENTRY_SIZE:
        raise ValueError(f"Entry too large: {len(entry)} bytes (max {MAX_ENTRY_SIZE})")

    # Validate JSON for .jsonl files
    if file_name.endswith(".jsonl"):
        try:
            json.loads(entry)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}")

    # Build full path
    full_path = os.path.join(MEMORY_DIR, file_name)

    # Ensure directory exists
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    # Append entry
    with open(full_path, "a", encoding="utf-8") as f:
        f.write(entry)
        if not entry.endswith("\n"):
            f.write("\n")

    return {
        "success": True,
        "file": file_name,
        "bytes_written": len(entry) + 1
    }


# Tool registry
TOOLS = {
    "hello": {
        "description": "Test connectivity",
        "handler": handle_hello
    },
    "read_repo_file": {
        "description": "Read a file from the repository",
        "handler": handle_read_file
    },
    "write_memory_entry": {
        "description": "Append an entry to a memory file",
        "handler": handle_write_memory
    }
}


class MCPHandler(BaseHTTPRequestHandler):
    """HTTP request handler for MCP server."""

    def send_json(self, data: dict, status: int = 200):
        """Send JSON response."""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_OPTIONS(self):
        """Handle CORS preflight."""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        """Handle GET requests."""
        parsed = urlparse(self.path)

        if parsed.path == "/health":
            self.send_json({
                "status": "healthy",
                "timestamp": datetime.utcnow().isoformat() + "Z"
            })

        elif parsed.path == "/tools":
            self.send_json({
                "tools": list(TOOLS.keys())
            })

        else:
            self.send_json({"error": "Not found"}, 404)

    def do_POST(self):
        """Handle POST requests."""
        parsed = urlparse(self.path)

        # Parse tool name from path
        match = re.match(r"/tools/(\w+)", parsed.path)
        if not match:
            self.send_json({"error": "Invalid path"}, 400)
            return

        tool_name = match.group(1)

        if tool_name not in TOOLS:
            self.send_json({"error": f"Unknown tool: {tool_name}"}, 404)
            return

        # Read request body
        content_length = int(self.headers.get("Content-Length", 0))
        if content_length > 0:
            body = self.rfile.read(content_length)
            try:
                data = json.loads(body)
            except json.JSONDecodeError:
                self.send_json({"error": "Invalid JSON"}, 400)
                return
        else:
            data = {}

        params = data.get("parameters", {})

        # Call tool handler
        try:
            result = TOOLS[tool_name]["handler"](params)
            self.send_json({
                "success": True,
                "result": result
            })
        except FileNotFoundError as e:
            self.send_json({
                "success": False,
                "error": str(e)
            }, 404)
        except ValueError as e:
            self.send_json({
                "success": False,
                "error": str(e)
            }, 400)
        except Exception as e:
            self.send_json({
                "success": False,
                "error": f"Internal error: {type(e).__name__}"
            }, 500)

    def log_message(self, format, *args):
        """Custom log format."""
        print(f"[{datetime.now().isoformat()}] {args[0]}")


def main():
    """Run the MCP server."""
    parser = argparse.ArgumentParser(description="MCP Server Stub")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Port to listen on")
    args = parser.parse_args()

    server = HTTPServer(("localhost", args.port), MCPHandler)
    print(f"MCP Server running on http://localhost:{args.port}")
    print(f"Repository root: {REPO_ROOT}")
    print(f"Available tools: {list(TOOLS.keys())}")
    print("Press Ctrl+C to stop")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == "__main__":
    main()
