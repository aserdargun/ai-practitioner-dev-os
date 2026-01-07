#!/usr/bin/env python3
"""
Example MCP Client for AI Practitioner Learning System

Demonstrates how to interact with the MCP server tools.
Uses Python stdlib only (no external dependencies).

Usage:
    python example_client.py evaluate
    python example_client.py log "task_completed" "Finished data pipeline"
    python example_client.py best-practice "Always test edge cases"
"""

import json
import subprocess
import sys
from pathlib import Path


def call_tool(tool_name: str, arguments: dict) -> dict:
    """Call an MCP tool via the server."""
    server_path = Path(__file__).parent / "example_server.py"

    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments,
        },
    }

    # Start server process
    process = subprocess.Popen(
        ["python3", str(server_path)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Send request
    stdout, stderr = process.communicate(input=json.dumps(request) + "\n", timeout=10)

    # Parse response
    if stdout.strip():
        response = json.loads(stdout.strip())
        if "content" in response:
            return json.loads(response["content"][0]["text"])
        elif "error" in response:
            return {"error": response["error"]}
    return {"error": {"message": "No response from server"}}


def cmd_evaluate():
    """Run evaluation."""
    print("Running evaluation...")
    result = call_tool("evaluate_progress", {"learner_id": "learner-001", "scope": "week"})
    print(json.dumps(result, indent=2))

    if "scores" in result:
        print("\n--- Summary ---")
        print(f"Overall Score: {result['overall']:.0%}")
        for dimension, score in result["scores"].items():
            print(f"  {dimension}: {score:.0%}")
        if result.get("recommendations"):
            print("\nRecommendations:")
            for rec in result["recommendations"]:
                print(f"  - {rec}")


def cmd_adapt():
    """Run adaptation."""
    print("Running adaptation analysis...")

    # First evaluate
    evaluation = call_tool("evaluate_progress", {"learner_id": "learner-001"})

    # Then adapt
    result = call_tool("adapt_path", {"learner_id": "learner-001", "evaluation_result": evaluation})
    print(json.dumps(result, indent=2))

    if result.get("mutations"):
        print("\n--- Proposed Changes ---")
        for mutation in result["mutations"]:
            print(f"  [{mutation['type']}] {mutation['description']}")
    else:
        print("\n--- No changes needed ---")


def cmd_log(event: str, message: str):
    """Log progress."""
    print(f"Logging: {event} - {message}")
    result = call_tool("log_progress", {
        "learner_id": "learner-001",
        "event": event,
        "message": message,
    })
    print(json.dumps(result, indent=2))

    if result.get("success"):
        print(f"\nEntry logged at {result['timestamp']}")


def cmd_best_practice(practice: str, title: str = None):
    """Add a best practice."""
    title = title or practice[:50]
    print(f"Adding best practice: {title}")
    result = call_tool("add_best_practice", {
        "title": title,
        "practice": practice,
    })
    print(json.dumps(result, indent=2))

    if result.get("success"):
        print(f"\nBest practice added on {result['entry_date']}")


def cmd_list_tools():
    """List available tools."""
    server_path = Path(__file__).parent / "example_server.py"

    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/list",
        "params": {},
    }

    process = subprocess.Popen(
        ["python3", str(server_path)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    stdout, _ = process.communicate(input=json.dumps(request) + "\n", timeout=10)

    if stdout.strip():
        response = json.loads(stdout.strip())
        if "tools" in response:
            print("Available tools:")
            for tool in response["tools"]:
                print(f"  - {tool['name']}: {tool['description']}")


def print_usage():
    """Print usage information."""
    print("""
MCP Client - AI Practitioner Learning System

Usage:
    python example_client.py <command> [arguments]

Commands:
    evaluate                  Run progress evaluation
    adapt                     Get adaptation recommendations
    log <event> <message>     Log a progress entry
    best-practice <practice>  Add a best practice
    list-tools                List available MCP tools
    help                      Show this help message

Examples:
    python example_client.py evaluate
    python example_client.py log task_completed "Finished data validation"
    python example_client.py best-practice "Always validate inputs at boundaries"
    """)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1].lower()

    if command == "evaluate":
        cmd_evaluate()
    elif command == "adapt":
        cmd_adapt()
    elif command == "log" and len(sys.argv) >= 4:
        cmd_log(sys.argv[2], sys.argv[3])
    elif command == "best-practice" and len(sys.argv) >= 3:
        cmd_best_practice(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    elif command == "list-tools":
        cmd_list_tools()
    elif command in ("help", "-h", "--help"):
        print_usage()
    else:
        print(f"Unknown command or missing arguments: {command}")
        print_usage()


if __name__ == "__main__":
    main()
