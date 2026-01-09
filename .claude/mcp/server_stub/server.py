#!/usr/bin/env python3
"""
Minimal MCP Server Stub for AI Practitioner Learning OS.

This server exposes three tools:
- hello: Simple greeting (testing)
- read_repo_file: Read allowed files from the repo
- write_memory_entry: Append to memory files

Usage:
    python server.py

The server reads JSON requests from stdin and writes responses to stdout.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


# Configuration
REPO_ROOT = Path(__file__).parent.parent.parent.parent
MEMORY_DIR = REPO_ROOT / ".claude" / "memory"

# Allowed paths for reading
ALLOWED_READ_PREFIXES = [
    "docs/",
    "paths/",
    "stacks/",
    ".claude/memory/",
]
ALLOWED_ROOT_FILES = ["README.md", "CLAUDE.md", "SETUP.md", "STACK.md"]

# Allowed files for writing
ALLOWED_WRITE_FILES = ["progress_log.jsonl", "decisions.jsonl"]

# Size limits
MAX_FILE_SIZE = 1024 * 1024  # 1MB
MAX_ENTRY_SIZE = 10 * 1024   # 10KB


def validate_read_path(path: str) -> tuple[bool, str]:
    """Validate that a path is allowed for reading."""
    # Normalize
    normalized = os.path.normpath(path)

    # Check for path traversal
    if ".." in normalized:
        return False, "Path traversal not allowed"

    # Check root files
    if normalized in ALLOWED_ROOT_FILES:
        return True, ""

    # Check prefixes
    for prefix in ALLOWED_READ_PREFIXES:
        if normalized.startswith(prefix):
            return True, ""

    return False, f"Path not allowed: {path}"


def handle_hello(input_data: dict) -> dict:
    """Handle the hello tool - simple greeting."""
    name = input_data.get("name", "World")
    if len(name) > 100:
        return {"error": "Name too long (max 100 characters)"}
    return {"greeting": f"Hello, {name}!"}


def handle_read_repo_file(input_data: dict) -> dict:
    """Handle the read_repo_file tool - read allowed files."""
    path = input_data.get("path", "")

    # Validate path
    is_valid, error = validate_read_path(path)
    if not is_valid:
        return {"error": error}

    # Build full path
    full_path = REPO_ROOT / path

    # Check if file exists
    if not full_path.exists():
        return {"error": f"File not found: {path}"}

    if not full_path.is_file():
        return {"error": f"Not a file: {path}"}

    # Check size
    size = full_path.stat().st_size
    if size > MAX_FILE_SIZE:
        return {"error": f"File too large: {size} bytes (max {MAX_FILE_SIZE})"}

    # Read content
    try:
        content = full_path.read_text(encoding="utf-8")
        return {"content": content, "size": size}
    except UnicodeDecodeError:
        return {"error": "File is not valid UTF-8 text"}
    except Exception as e:
        return {"error": f"Failed to read file: {type(e).__name__}"}


def handle_write_memory_entry(input_data: dict) -> dict:
    """Handle the write_memory_entry tool - append to memory files."""
    file_name = input_data.get("file", "")
    entry = input_data.get("entry", {})

    # Validate file name
    if file_name not in ALLOWED_WRITE_FILES:
        return {"error": f"File not allowed: {file_name}. Allowed: {ALLOWED_WRITE_FILES}"}

    # Validate entry has required fields
    if "timestamp" not in entry:
        return {"error": "Entry must have 'timestamp' field"}
    if "type" not in entry:
        return {"error": "Entry must have 'type' field"}

    # Validate entry size
    entry_json = json.dumps(entry)
    if len(entry_json) > MAX_ENTRY_SIZE:
        return {"error": f"Entry too large: {len(entry_json)} bytes (max {MAX_ENTRY_SIZE})"}

    # Build path
    file_path = MEMORY_DIR / file_name

    # Ensure directory exists
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Count existing lines
    try:
        existing_lines = len(file_path.read_text().splitlines()) if file_path.exists() else 0
    except Exception:
        existing_lines = 0

    # Append entry
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(entry_json + "\n")
        return {"success": True, "line_number": existing_lines + 1}
    except Exception as e:
        return {"error": f"Failed to write: {type(e).__name__}"}


# Tool registry
TOOL_HANDLERS = {
    "hello": handle_hello,
    "read_repo_file": handle_read_repo_file,
    "write_memory_entry": handle_write_memory_entry,
}


def process_request(request: dict) -> dict:
    """Process a single MCP request."""
    tool_name = request.get("tool")
    input_data = request.get("input", {})

    if not tool_name:
        return {"error": "Missing 'tool' field"}

    if tool_name not in TOOL_HANDLERS:
        return {"error": f"Unknown tool: {tool_name}"}

    handler = TOOL_HANDLERS[tool_name]
    try:
        return handler(input_data)
    except Exception as e:
        return {"error": f"Tool execution failed: {type(e).__name__}"}


def main():
    """Main loop - read requests from stdin, write responses to stdout."""
    # Read from stdin
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            request = json.loads(line)
            response = process_request(request)
        except json.JSONDecodeError:
            response = {"error": "Invalid JSON"}

        # Write response
        print(json.dumps(response), flush=True)


if __name__ == "__main__":
    main()
