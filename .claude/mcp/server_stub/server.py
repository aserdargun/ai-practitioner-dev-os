#!/usr/bin/env python3
"""
MCP Server Stub for AI Practitioner Learning OS

A minimal Model Context Protocol server implementation.
Uses Python stdlib only - no external dependencies.

Usage:
    python server.py

Environment:
    MCP_PORT - Port to listen on (default: 8765)
    MCP_HOST - Host to bind to (default: localhost)
    REPO_ROOT - Repository root path (default: ../../../)
"""

import json
import os
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


# Configuration
PORT = int(os.environ.get("MCP_PORT", 8765))
HOST = os.environ.get("MCP_HOST", "localhost")
REPO_ROOT = Path(os.environ.get("REPO_ROOT", "../../..")).resolve()

# Allowed paths for reading (relative to repo root)
ALLOWED_READ_PATHS = [
    "paths/",
    "docs/",
    ".claude/memory/",
    ".claude/skills/",
    ".claude/commands/",
    "templates/",
    "examples/",
    "README.md",
    "CLAUDE.md",
]

# Blocked patterns
BLOCKED_PATTERNS = [".git/", ".env", "secret", ".key", ".pem"]

# Memory files that can be written to
WRITABLE_MEMORY_FILES = ["progress_log.jsonl", "decisions.jsonl"]


def is_path_allowed(path: str) -> bool:
    """Check if a path is allowed for reading."""
    # Normalize path
    path = path.lstrip("/")

    # Check blocked patterns
    for pattern in BLOCKED_PATTERNS:
        if pattern in path.lower():
            return False

    # Check allowed paths
    for allowed in ALLOWED_READ_PATHS:
        if path.startswith(allowed) or path == allowed.rstrip("/"):
            return True

    return False


def tool_hello(input_data: dict) -> dict:
    """Hello tool - returns a greeting."""
    return {
        "message": "Hello from AI Practitioner Learning OS!",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }


def tool_read_repo_file(input_data: dict) -> dict:
    """Read a file from the repository."""
    path = input_data.get("path", "")

    if not path:
        raise ValueError("Missing required parameter: path")

    if not is_path_allowed(path):
        raise PermissionError(f"Access denied: {path}")

    file_path = REPO_ROOT / path

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if not file_path.is_file():
        raise ValueError(f"Not a file: {path}")

    content = file_path.read_text(encoding="utf-8")

    return {
        "content": content,
        "path": path,
        "size_bytes": len(content.encode("utf-8")),
    }


def tool_write_memory_entry(input_data: dict) -> dict:
    """Append an entry to a memory file."""
    file_name = input_data.get("file", "")
    entry = input_data.get("entry", {})

    if not file_name:
        raise ValueError("Missing required parameter: file")

    if not entry:
        raise ValueError("Missing required parameter: entry")

    if file_name not in WRITABLE_MEMORY_FILES:
        raise PermissionError(f"Cannot write to: {file_name}")

    # Ensure entry has timestamp
    if "timestamp" not in entry:
        entry["timestamp"] = datetime.utcnow().isoformat() + "Z"

    # Check entry size
    entry_json = json.dumps(entry)
    if len(entry_json) > 10240:  # 10KB limit
        raise ValueError("Entry too large (max 10KB)")

    # Write to file
    file_path = REPO_ROOT / ".claude" / "memory" / file_name

    # Ensure directory exists
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Append entry
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(entry_json + "\n")

    # Count entries
    entry_count = sum(1 for _ in open(file_path, encoding="utf-8"))

    return {
        "success": True,
        "file": file_name,
        "entry_count": entry_count,
    }


# Tool registry
TOOLS = {
    "hello": tool_hello,
    "read_repo_file": tool_read_repo_file,
    "write_memory_entry": tool_write_memory_entry,
}


class MCPHandler(BaseHTTPRequestHandler):
    """HTTP request handler for MCP server."""

    def _send_json(self, data: Any, status: int = 200):
        """Send a JSON response."""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def _send_error(self, code: str, message: str, status: int = 400):
        """Send an error response."""
        self._send_json({"error": {"code": code, "message": message}}, status)

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
            self._send_json({"status": "healthy"})
        elif parsed.path == "/tools":
            self._send_json({"tools": list(TOOLS.keys())})
        else:
            self._send_error("NOT_FOUND", f"Unknown endpoint: {parsed.path}", 404)

    def do_POST(self):
        """Handle POST requests."""
        parsed = urlparse(self.path)

        # Check for tool call
        if parsed.path.startswith("/tools/"):
            tool_name = parsed.path[7:]  # Remove "/tools/" prefix

            if tool_name not in TOOLS:
                self._send_error("TOOL_NOT_FOUND", f"Unknown tool: {tool_name}", 404)
                return

            # Read request body
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8") if content_length else "{}"

            try:
                request_data = json.loads(body)
                input_data = request_data.get("input", {})
            except json.JSONDecodeError:
                self._send_error("INVALID_JSON", "Request body is not valid JSON")
                return

            # Call tool
            try:
                result = TOOLS[tool_name](input_data)
                self._send_json({"result": result})
            except ValueError as e:
                self._send_error("INVALID_INPUT", str(e))
            except PermissionError as e:
                self._send_error("PATH_NOT_ALLOWED", str(e), 403)
            except FileNotFoundError as e:
                self._send_error("FILE_NOT_FOUND", str(e), 404)
            except Exception as e:
                self._send_error("INTERNAL_ERROR", str(e), 500)
        else:
            self._send_error("NOT_FOUND", f"Unknown endpoint: {parsed.path}", 404)

    def log_message(self, format: str, *args):
        """Log HTTP requests."""
        print(f"[{datetime.now().isoformat()}] {args[0]}")


def main():
    """Run the MCP server."""
    print(f"Starting MCP Server...")
    print(f"  Host: {HOST}")
    print(f"  Port: {PORT}")
    print(f"  Repo root: {REPO_ROOT}")
    print(f"  Available tools: {', '.join(TOOLS.keys())}")
    print()

    server = HTTPServer((HOST, PORT), MCPHandler)
    print(f"Server running at http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == "__main__":
    main()
