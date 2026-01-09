#!/usr/bin/env python3
"""
MCP Python Client Example.

Demonstrates how to interact with the MCP server from Python.
"""

import json
import subprocess
import sys
from typing import Any, Optional


class MCPClient:
    """Simple MCP client that communicates via subprocess."""

    def __init__(self, server_command: str):
        """
        Initialize the MCP client.

        Args:
            server_command: Shell command to start the MCP server
        """
        self.server_command = server_command
        self._process: Optional[subprocess.Popen] = None

    def start(self) -> None:
        """Start the MCP server process."""
        self._process = subprocess.Popen(
            self.server_command,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

    def stop(self) -> None:
        """Stop the MCP server process."""
        if self._process:
            self._process.terminate()
            self._process.wait()
            self._process = None

    def call(self, tool: str, input_data: dict) -> dict:
        """
        Call an MCP tool.

        Args:
            tool: Name of the tool to call
            input_data: Input parameters for the tool

        Returns:
            Tool response as a dictionary
        """
        if not self._process:
            self.start()

        request = json.dumps({"tool": tool, "input": input_data})

        try:
            self._process.stdin.write(request + "\n")
            self._process.stdin.flush()
            response_line = self._process.stdout.readline()
            return json.loads(response_line)
        except Exception as e:
            return {"error": f"Client error: {type(e).__name__}: {e}"}

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()


def demo():
    """Demonstrate MCP client usage."""
    # Path to server (adjust if needed)
    server_path = "../server_stub/server.py"

    print("=== MCP Client Demo ===\n")

    # For demo, we'll use a simpler approach
    # In real usage, use the MCPClient class above

    def call_tool(tool: str, input_data: dict) -> dict:
        """Simple tool caller using subprocess."""
        request = json.dumps({"tool": tool, "input": input_data})
        result = subprocess.run(
            ["python", server_path],
            input=request,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            return {"error": f"Server error: {result.stderr}"}
        return json.loads(result.stdout.strip())

    # Demo 1: Hello tool
    print("1. Testing hello tool:")
    result = call_tool("hello", {"name": "AI Practitioner"})
    print(f"   Response: {result}\n")

    # Demo 2: Read file
    print("2. Reading a file:")
    result = call_tool("read_repo_file", {"path": "CLAUDE.md"})
    if "error" in result:
        print(f"   Error: {result['error']}\n")
    else:
        print(f"   File size: {result['size']} bytes")
        print(f"   First 100 chars: {result['content'][:100]}...\n")

    # Demo 3: Read forbidden file
    print("3. Attempting to read forbidden file (.env):")
    result = call_tool("read_repo_file", {"path": ".env"})
    print(f"   Response: {result}\n")

    # Demo 4: Write entry (demonstration only - won't actually write without server)
    print("4. Write entry example (request format):")
    entry = {
        "timestamp": "2026-01-09T12:00:00Z",
        "type": "demo",
        "message": "This is a demo entry",
    }
    print(f"   Entry: {json.dumps(entry, indent=2)}\n")

    print("=== Demo Complete ===")


if __name__ == "__main__":
    demo()
