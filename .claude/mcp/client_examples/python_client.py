#!/usr/bin/env python3
"""
MCP Client Example for AI Practitioner Learning OS

Demonstrates how to interact with the MCP server.

Usage:
    python python_client.py
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Optional


class MCPError(Exception):
    """MCP protocol error."""
    def __init__(self, code: int, message: str, data: Any = None):
        self.code = code
        self.message = message
        self.data = data
        super().__init__(f"MCP Error {code}: {message}")


class MCPClient:
    """Simple MCP client for stdio transport."""

    def __init__(self, command: str, args: list[str], cwd: Optional[str] = None):
        self.command = command
        self.args = args
        self.cwd = cwd
        self.process: Optional[subprocess.Popen] = None
        self.request_id = 0

    def connect(self):
        """Start the server process."""
        self.process = subprocess.Popen(
            [self.command] + self.args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=self.cwd,
            text=True
        )

        # Initialize
        response = self._send_request("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "python-client", "version": "1.0.0"}
        })

        # Send initialized notification
        self._send_notification("notifications/initialized", {})

        return response

    def disconnect(self):
        """Stop the server process."""
        if self.process:
            self.process.terminate()
            self.process.wait()
            self.process = None

    def _send_request(self, method: str, params: dict) -> dict:
        """Send a request and wait for response."""
        if not self.process:
            raise RuntimeError("Not connected")

        self.request_id += 1
        request = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": self.request_id
        }

        # Send request
        self.process.stdin.write(json.dumps(request) + "\n")
        self.process.stdin.flush()

        # Read response
        response_line = self.process.stdout.readline()
        if not response_line:
            raise RuntimeError("No response from server")

        response = json.loads(response_line)

        # Check for error
        if "error" in response:
            error = response["error"]
            raise MCPError(
                error.get("code", -1),
                error.get("message", "Unknown error"),
                error.get("data")
            )

        return response.get("result", {})

    def _send_notification(self, method: str, params: dict):
        """Send a notification (no response expected)."""
        if not self.process:
            raise RuntimeError("Not connected")

        notification = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params
        }

        self.process.stdin.write(json.dumps(notification) + "\n")
        self.process.stdin.flush()

    def list_tools(self) -> list[dict]:
        """Get list of available tools."""
        result = self._send_request("tools/list", {})
        return result.get("tools", [])

    def call_tool(self, name: str, arguments: dict) -> Any:
        """Call a tool and return the result."""
        result = self._send_request("tools/call", {
            "name": name,
            "arguments": arguments
        })

        # Extract content
        content = result.get("content", [])
        if content and content[0].get("type") == "text":
            return json.loads(content[0]["text"])

        return result


def main():
    """Demo the MCP client."""
    # Find server path
    script_dir = Path(__file__).parent
    server_path = script_dir.parent / "server_stub" / "server.py"

    print("MCP Client Demo")
    print("=" * 40)

    # Create and connect client
    client = MCPClient("python3", [str(server_path)])

    try:
        print("\nConnecting to server...")
        init_result = client.connect()
        print(f"Connected! Server: {init_result.get('serverInfo', {}).get('name')}")

        # List tools
        print("\nAvailable tools:")
        tools = client.list_tools()
        for tool in tools:
            print(f"  - {tool['name']}: {tool['description']}")

        # Test hello tool
        print("\nTesting 'hello' tool...")
        result = client.call_tool("hello", {"name": "Developer"})
        print(f"  Result: {result}")

        # Test read_repo_file tool
        print("\nTesting 'read_repo_file' tool...")
        result = client.call_tool("read_repo_file", {"path": "README.md"})
        if result.get("exists"):
            content_preview = result["content"][:100] + "..." if len(result.get("content", "")) > 100 else result.get("content", "")
            print(f"  File exists: True")
            print(f"  Preview: {content_preview}")
        else:
            print(f"  Error: {result.get('error')}")

        # Test denied path
        print("\nTesting denied path (.env)...")
        try:
            result = client.call_tool("read_repo_file", {"path": ".env"})
            print(f"  Result: {result}")
        except MCPError as e:
            print(f"  Access denied (expected): {e.message}")

        # Test write_memory_entry tool
        print("\nTesting 'write_memory_entry' tool...")
        result = client.call_tool("write_memory_entry", {
            "file": "progress_log.jsonl",
            "entry": {
                "event": "mcp_test",
                "message": "Client test successful"
            }
        })
        print(f"  Result: {result}")

    except MCPError as e:
        print(f"MCP Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("\nDisconnecting...")
        client.disconnect()
        print("Done!")


if __name__ == "__main__":
    main()
