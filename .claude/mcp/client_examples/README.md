# MCP Client Examples

Example code for calling MCP tools from Python.

## Overview

This folder contains client examples that demonstrate how to interact with the MCP server.

## Files

- `python_client.py` - Basic Python client for MCP

## Usage

### Running with the Server

```bash
# Start the server and client together (pipe mode)
python python_client.py | python ../server_stub/server.py
```

### Programmatic Usage

```python
from python_client import MCPClient

# Create client (connects to server via subprocess)
client = MCPClient("python ../server_stub/server.py")

# Call tools
greeting = client.call("hello", {"name": "Learner"})
print(greeting)  # {"greeting": "Hello, Learner!"}

# Read a file
content = client.call("read_repo_file", {"path": "README.md"})
print(content["size"])  # File size

# Write to memory (append-only)
result = client.call("write_memory_entry", {
    "file": "progress_log.jsonl",
    "entry": {
        "timestamp": "2026-01-09T12:00:00Z",
        "type": "example",
        "message": "Test entry"
    }
})
print(result)  # {"success": true, "line_number": X}
```

## Error Handling

```python
result = client.call("read_repo_file", {"path": ".env"})
if "error" in result:
    print(f"Error: {result['error']}")
else:
    print(f"Content: {result['content'][:100]}...")
```

## Integration Tips

1. **Always check for errors** - Every response might contain an "error" key
2. **Handle timeouts** - Add timeout logic for production use
3. **Validate before calling** - Pre-validate inputs to avoid round-trips
4. **Log calls** - Keep an audit trail of MCP interactions
