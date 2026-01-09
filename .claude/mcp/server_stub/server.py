#!/usr/bin/env python3
"""
MCP Server Stub for AI Practitioner Learning OS

A minimal MCP server providing tools for:
- Testing connectivity (hello)
- Reading repository files (read_repo_file)
- Appending to memory files (write_memory_entry)

Usage:
    python server.py

This server uses stdio transport for MCP communication.
"""

import json
import sys
import re
from datetime import datetime
from pathlib import Path
from typing import Any

# Configuration
REPO_ROOT = Path(__file__).parent.parent.parent.parent  # Navigate to repo root

ALLOWED_READ_PATHS = [
    "docs/**",
    "paths/**",
    "stacks/**",
    ".claude/memory/*",
    ".claude/commands/*",
    ".claude/skills/*",
    "README.md",
    "CLAUDE.md",
]

DENIED_READ_PATHS = [
    ".env",
    ".env.*",
    "**/secrets/**",
    "**/*.key",
    "**/*.pem",
    ".git/**",
]

ALLOWED_WRITE_FILES = [
    ".claude/memory/progress_log.jsonl",
    ".claude/memory/decisions.jsonl",
    ".claude/memory/best_practices.md",
]

MAX_FILE_SIZE = 100 * 1024  # 100KB
MAX_ENTRY_SIZE = 5 * 1024   # 5KB


def match_pattern(path: str, pattern: str) -> bool:
    """Check if path matches glob-like pattern."""
    import fnmatch
    return fnmatch.fnmatch(path, pattern)


def is_path_allowed(path: str) -> tuple[bool, str]:
    """Check if path is allowed for reading."""
    # Security checks
    if ".." in path:
        return False, "Path traversal not allowed"
    if path.startswith("/"):
        return False, "Absolute paths not allowed"
    if not re.match(r'^[a-zA-Z0-9_\-./]+$', path):
        return False, "Invalid characters in path"

    # Check denied paths first
    for pattern in DENIED_READ_PATHS:
        if match_pattern(path, pattern):
            return False, f"Path matches denied pattern: {pattern}"

    # Check allowed paths
    for pattern in ALLOWED_READ_PATHS:
        if match_pattern(path, pattern):
            return True, "OK"

    return False, "Path not in allowed list"


def tool_hello(arguments: dict) -> dict:
    """Simple greeting tool for testing."""
    name = arguments.get("name", "World")
    if not name or len(name) > 100:
        return {"error": "Invalid name"}
    return {"greeting": f"Hello, {name}! MCP is working."}


def tool_read_repo_file(arguments: dict) -> dict:
    """Read a file from the repository."""
    path = arguments.get("path", "")

    # Validate path
    allowed, reason = is_path_allowed(path)
    if not allowed:
        return {"exists": False, "error": reason}

    # Read file
    full_path = REPO_ROOT / path
    if not full_path.exists():
        return {"exists": False, "error": "File not found"}

    if not full_path.is_file():
        return {"exists": False, "error": "Not a file"}

    # Check size
    if full_path.stat().st_size > MAX_FILE_SIZE:
        return {"exists": True, "error": f"File too large (max {MAX_FILE_SIZE} bytes)"}

    try:
        content = full_path.read_text(encoding="utf-8")
        return {"exists": True, "content": content}
    except Exception as e:
        return {"exists": True, "error": f"Read error: {str(e)}"}


def tool_write_memory_entry(arguments: dict) -> dict:
    """Append an entry to a memory file."""
    file_name = arguments.get("file", "")

    # Validate file
    target_path = f".claude/memory/{file_name}"
    if target_path not in ALLOWED_WRITE_FILES:
        return {"success": False, "message": f"File not allowed: {file_name}"}

    full_path = REPO_ROOT / target_path

    # Prepare content based on file type
    if file_name.endswith(".jsonl"):
        entry = arguments.get("entry", {})
        if not entry:
            return {"success": False, "message": "Entry required for JSONL files"}

        # Validate entry
        if "timestamp" not in entry:
            entry["timestamp"] = datetime.utcnow().isoformat() + "Z"

        content_to_write = json.dumps(entry) + "\n"

    elif file_name.endswith(".md"):
        content = arguments.get("content", "")
        if not content:
            return {"success": False, "message": "Content required for MD files"}

        content_to_write = content if content.startswith("\n") else "\n" + content

    else:
        return {"success": False, "message": "Unknown file type"}

    # Check size
    if len(content_to_write) > MAX_ENTRY_SIZE:
        return {"success": False, "message": f"Entry too large (max {MAX_ENTRY_SIZE} bytes)"}

    # Write (append)
    try:
        with open(full_path, "a", encoding="utf-8") as f:
            f.write(content_to_write)
        return {"success": True, "message": f"Entry appended to {file_name}"}
    except Exception as e:
        return {"success": False, "message": f"Write error: {str(e)}"}


# Tool registry
TOOLS = {
    "hello": {
        "description": "A simple greeting tool to test MCP connectivity",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Name to greet"}
            },
            "required": ["name"]
        },
        "handler": tool_hello
    },
    "read_repo_file": {
        "description": "Read a file from the repository (safe paths only)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Relative path to file"}
            },
            "required": ["path"]
        },
        "handler": tool_read_repo_file
    },
    "write_memory_entry": {
        "description": "Append an entry to a memory file",
        "inputSchema": {
            "type": "object",
            "properties": {
                "file": {
                    "type": "string",
                    "enum": ["progress_log.jsonl", "decisions.jsonl", "best_practices.md"]
                },
                "entry": {"type": "object", "description": "Entry for JSONL files"},
                "content": {"type": "string", "description": "Content for MD files"}
            },
            "required": ["file"]
        },
        "handler": tool_write_memory_entry
    }
}


def handle_request(request: dict) -> dict:
    """Handle incoming MCP request."""
    method = request.get("method", "")
    params = request.get("params", {})
    request_id = request.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "learning-os-mcp", "version": "1.0.0"}
            },
            "id": request_id
        }

    elif method == "tools/list":
        tools = [
            {
                "name": name,
                "description": tool["description"],
                "inputSchema": tool["inputSchema"]
            }
            for name, tool in TOOLS.items()
        ]
        return {
            "jsonrpc": "2.0",
            "result": {"tools": tools},
            "id": request_id
        }

    elif method == "tools/call":
        tool_name = params.get("name", "")
        arguments = params.get("arguments", {})

        if tool_name not in TOOLS:
            return {
                "jsonrpc": "2.0",
                "error": {"code": -32601, "message": f"Tool not found: {tool_name}"},
                "id": request_id
            }

        try:
            result = TOOLS[tool_name]["handler"](arguments)
            return {
                "jsonrpc": "2.0",
                "result": {
                    "content": [{"type": "text", "text": json.dumps(result)}]
                },
                "id": request_id
            }
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "error": {"code": -32603, "message": str(e)},
                "id": request_id
            }

    elif method == "notifications/initialized":
        return None  # No response for notifications

    else:
        return {
            "jsonrpc": "2.0",
            "error": {"code": -32601, "message": f"Method not found: {method}"},
            "id": request_id
        }


def main():
    """Main loop: read requests from stdin, write responses to stdout."""
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break

            request = json.loads(line)
            response = handle_request(request)

            if response:  # Skip None responses (notifications)
                sys.stdout.write(json.dumps(response) + "\n")
                sys.stdout.flush()

        except json.JSONDecodeError:
            error_response = {
                "jsonrpc": "2.0",
                "error": {"code": -32700, "message": "Parse error"},
                "id": None
            }
            sys.stdout.write(json.dumps(error_response) + "\n")
            sys.stdout.flush()
        except Exception as e:
            error_response = {
                "jsonrpc": "2.0",
                "error": {"code": -32603, "message": str(e)},
                "id": None
            }
            sys.stdout.write(json.dumps(error_response) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
