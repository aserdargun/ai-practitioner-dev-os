# MCP Client Examples

Example code for interacting with the MCP server.

## Python Client

The `python_client.py` file demonstrates how to:
- Connect to the MCP server
- List available tools
- Call tools and handle responses
- Process errors

### Running the Example

```bash
# Start the server in one terminal
python ../.claude/mcp/server_stub/server.py

# Run the client in another terminal
python python_client.py
```

### Usage in Your Code

```python
from python_client import MCPClient

# Create client
client = MCPClient("python", ["../server_stub/server.py"])

# Connect
client.connect()

# List tools
tools = client.list_tools()
print(tools)

# Call a tool
result = client.call_tool("hello", {"name": "Developer"})
print(result)

# Read a file
content = client.call_tool("read_repo_file", {"path": "README.md"})
print(content)

# Disconnect
client.disconnect()
```

## Other Languages

MCP is language-agnostic. The same patterns apply:
1. Spawn the server process
2. Communicate via stdin/stdout using JSON-RPC
3. Handle responses and errors

### Node.js Example (Conceptual)

```javascript
const { spawn } = require('child_process');

const server = spawn('python', ['server.py']);

server.stdout.on('data', (data) => {
    const response = JSON.parse(data.toString());
    console.log(response);
});

// Send request
const request = {
    jsonrpc: "2.0",
    method: "tools/call",
    params: { name: "hello", arguments: { name: "Node" } },
    id: 1
};
server.stdin.write(JSON.stringify(request) + '\n');
```

## Error Handling

Always handle:
- Connection failures
- Invalid responses
- Tool errors

```python
try:
    result = client.call_tool("read_repo_file", {"path": ".env"})
except MCPError as e:
    if e.code == -32001:
        print("Access denied: path not allowed")
    else:
        print(f"Error: {e.message}")
```
