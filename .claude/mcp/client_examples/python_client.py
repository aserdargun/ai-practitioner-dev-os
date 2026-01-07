#!/usr/bin/env python3
"""
MCP Python Client Example

A simple client for the AI Practitioner Learning OS MCP server.
Uses Python stdlib only - no external dependencies.

Usage:
    from python_client import MCPClient

    client = MCPClient("http://localhost:8765")
    response = client.hello()
    print(response)
"""

import json
import urllib.request
import urllib.error
from datetime import datetime
from typing import Any, Optional


class MCPError(Exception):
    """Exception raised for MCP errors."""

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")


class MCPClient:
    """Client for MCP server."""

    def __init__(self, base_url: str = "http://localhost:8765"):
        """Initialize the client.

        Args:
            base_url: Base URL of the MCP server
        """
        self.base_url = base_url.rstrip("/")

    def _request(self, method: str, path: str, data: Optional[dict] = None) -> dict:
        """Make an HTTP request to the server.

        Args:
            method: HTTP method (GET, POST)
            path: URL path
            data: Request body data (for POST)

        Returns:
            Response data as dictionary

        Raises:
            MCPError: If the server returns an error
        """
        url = f"{self.base_url}{path}"

        if data is not None:
            body = json.dumps(data).encode("utf-8")
            headers = {"Content-Type": "application/json"}
        else:
            body = None
            headers = {}

        request = urllib.request.Request(url, data=body, headers=headers, method=method)

        try:
            with urllib.request.urlopen(request) as response:
                response_data = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            error_data = json.loads(e.read().decode("utf-8"))
            if "error" in error_data:
                raise MCPError(error_data["error"]["code"], error_data["error"]["message"])
            raise

        return response_data

    def call_tool(self, tool_name: str, input_data: dict) -> dict:
        """Call an MCP tool.

        Args:
            tool_name: Name of the tool to call
            input_data: Input parameters for the tool

        Returns:
            Tool result

        Raises:
            MCPError: If the tool returns an error
        """
        response = self._request("POST", f"/tools/{tool_name}", {"input": input_data})
        return response.get("result", {})

    def health(self) -> dict:
        """Check server health.

        Returns:
            Health status
        """
        return self._request("GET", "/health")

    def list_tools(self) -> list:
        """List available tools.

        Returns:
            List of tool names
        """
        response = self._request("GET", "/tools")
        return response.get("tools", [])

    # Convenience methods

    def hello(self) -> dict:
        """Call the hello tool.

        Returns:
            Greeting message and timestamp
        """
        return self.call_tool("hello", {})

    def read_file(self, path: str) -> str:
        """Read a file from the repository.

        Args:
            path: Relative path to the file

        Returns:
            File contents

        Raises:
            MCPError: If file not found or access denied
        """
        result = self.call_tool("read_repo_file", {"path": path})
        return result.get("content", "")

    def log_progress(self, entry: dict) -> dict:
        """Log a progress entry.

        Args:
            entry: Progress entry (timestamp will be added if missing)

        Returns:
            Write result
        """
        if "timestamp" not in entry:
            entry["timestamp"] = datetime.utcnow().isoformat() + "Z"

        return self.call_tool("write_memory_entry", {
            "file": "progress_log.jsonl",
            "entry": entry
        })

    def log_decision(self, entry: dict) -> dict:
        """Log a decision entry.

        Args:
            entry: Decision entry (timestamp will be added if missing)

        Returns:
            Write result
        """
        if "timestamp" not in entry:
            entry["timestamp"] = datetime.utcnow().isoformat() + "Z"

        return self.call_tool("write_memory_entry", {
            "file": "decisions.jsonl",
            "entry": entry
        })


def main():
    """Example usage of the MCP client."""
    print("MCP Client Example")
    print("=" * 40)

    # Create client
    client = MCPClient()

    # Check health
    print("\n1. Health check:")
    try:
        health = client.health()
        print(f"   Status: {health['status']}")
    except Exception as e:
        print(f"   Error: {e}")
        print("   Make sure the server is running!")
        return

    # List tools
    print("\n2. Available tools:")
    tools = client.list_tools()
    for tool in tools:
        print(f"   - {tool}")

    # Call hello
    print("\n3. Hello tool:")
    response = client.hello()
    print(f"   Message: {response['message']}")
    print(f"   Timestamp: {response['timestamp']}")

    # Read a file
    print("\n4. Read file:")
    try:
        content = client.read_file("README.md")
        print(f"   README.md ({len(content)} bytes)")
        print(f"   First line: {content.split(chr(10))[0]}")
    except MCPError as e:
        print(f"   Error: {e}")

    # Log progress (commented out to not modify files during demo)
    print("\n5. Log progress (demo - not actually writing):")
    print("   Would log: {'event': 'demo', 'message': 'MCP client test'}")
    # Uncomment to actually log:
    # client.log_progress({"event": "demo", "message": "MCP client test"})

    print("\n" + "=" * 40)
    print("Demo complete!")


if __name__ == "__main__":
    main()
