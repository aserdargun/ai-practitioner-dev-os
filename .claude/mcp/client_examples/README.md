# MCP Client Examples

Example client implementations for interacting with the MCP server.

## Python Client

[python_client.py](python_client.py) provides a simple client class.

### Quick Start

```python
from python_client import MCPClient

# Connect to server
client = MCPClient("http://localhost:5000")

# Test connectivity
result = client.hello("Learner")
print(result["message"])  # "Hello, Learner!"

# Read a file
content = client.read_file(".claude/memory/progress_log.jsonl")
print(content)

# Write to memory (with approval)
client.write_memory(
    "progress_log.jsonl",
    '{"timestamp": "2026-01-15T10:00:00Z", "event": "test"}'
)
```

### Running Examples

```bash
# Start the server first
python .claude/mcp/server_stub/server.py &

# Run the client
python .claude/mcp/client_examples/python_client.py
```

## Error Handling

```python
from python_client import MCPClient, MCPError

client = MCPClient("http://localhost:5000")

try:
    content = client.read_file("nonexistent.txt")
except MCPError as e:
    print(f"Tool call failed: {e}")
```

## Integration with Agents

```python
class MyAgent:
    def __init__(self):
        self.mcp = MCPClient("http://localhost:5000")

    def log_progress(self, event, description):
        """Log a progress event."""
        import json
        from datetime import datetime

        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event": event,
            "description": description
        }

        # In production, require user approval here
        self.mcp.write_memory("progress_log.jsonl", json.dumps(entry))
```

## See Also

- [../server_stub/](../server_stub/) — Server implementation
- [../tool-contracts.md](../tool-contracts.md) — Tool specifications
- [../safety.md](../safety.md) — Security guidelines
