#!/usr/bin/env python3
"""
MCP Python Client

A simple client for interacting with the MCP server.
Uses only Python standard library.

Usage:
    from python_client import MCPClient

    client = MCPClient("http://localhost:5000")
    result = client.hello("World")
"""

import json
import urllib.request
import urllib.error
from typing import Optional, Any


class MCPError(Exception):
    """Error from MCP tool call."""
    pass


class MCPClient:
    """Client for MCP server."""

    def __init__(self, base_url: str = "http://localhost:5000"):
        """Initialize client with server URL."""
        self.base_url = base_url.rstrip("/")

    def _request(self, method: str, path: str, data: Optional[dict] = None) -> dict:
        """Make HTTP request to server."""
        url = f"{self.base_url}{path}"

        if data is not None:
            body = json.dumps(data).encode("utf-8")
            headers = {"Content-Type": "application/json"}
        else:
            body = None
            headers = {}

        req = urllib.request.Request(url, data=body, headers=headers, method=method)

        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8")
            try:
                error_data = json.loads(error_body)
                raise MCPError(error_data.get("error", f"HTTP {e.code}"))
            except json.JSONDecodeError:
                raise MCPError(f"HTTP {e.code}: {error_body}")
        except urllib.error.URLError as e:
            raise MCPError(f"Connection failed: {e.reason}")

    def health(self) -> dict:
        """Check server health."""
        return self._request("GET", "/health")

    def list_tools(self) -> list:
        """List available tools."""
        result = self._request("GET", "/tools")
        return result.get("tools", [])

    def call_tool(self, tool_name: str, parameters: dict) -> Any:
        """Call a tool with parameters."""
        result = self._request("POST", f"/tools/{tool_name}", {
            "parameters": parameters
        })

        if not result.get("success"):
            raise MCPError(result.get("error", "Unknown error"))

        return result.get("result")

    def hello(self, name: str = "World") -> dict:
        """Call hello tool."""
        return self.call_tool("hello", {"name": name})

    def read_file(self, path: str) -> str:
        """Read a file from the repository."""
        result = self.call_tool("read_repo_file", {"path": path})
        return result.get("content", "")

    def write_memory(self, file: str, entry: str) -> dict:
        """Write an entry to a memory file."""
        return self.call_tool("write_memory_entry", {
            "file": file,
            "entry": entry
        })


def main():
    """Demo the client."""
    print("MCP Client Demo")
    print("=" * 40)

    client = MCPClient()

    # Health check
    print("\n1. Health Check")
    try:
        health = client.health()
        print(f"   Status: {health['status']}")
        print(f"   Timestamp: {health['timestamp']}")
    except MCPError as e:
        print(f"   Error: {e}")
        print("   Is the server running? Try: python server_stub/server.py")
        return

    # List tools
    print("\n2. List Tools")
    tools = client.list_tools()
    for tool in tools:
        print(f"   - {tool}")

    # Hello tool
    print("\n3. Hello Tool")
    result = client.hello("Learner")
    print(f"   Message: {result['message']}")

    # Read file
    print("\n4. Read File")
    try:
        content = client.read_file(".claude/memory/progress_log.jsonl")
        lines = content.strip().split("\n")
        print(f"   Read {len(lines)} entries from progress_log.jsonl")
        if lines:
            print(f"   Last entry: {lines[-1][:50]}...")
    except MCPError as e:
        print(f"   Error: {e}")

    # Write memory (demo - would require approval in real use)
    print("\n5. Write Memory (demo)")
    print("   Skipping write demo - requires user approval in real use")

    print("\n" + "=" * 40)
    print("Demo complete!")


if __name__ == "__main__":
    main()
