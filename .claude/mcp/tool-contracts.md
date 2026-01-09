# Tool Contracts

Schemas and constraints for MCP tools in the learning OS.

## Contract Format

Each tool contract defines:
- **Name**: Tool identifier
- **Description**: What the tool does
- **Input Schema**: JSON Schema for inputs
- **Output Schema**: JSON Schema for outputs
- **Constraints**: Limitations and safety rules

---

## hello

### Description
A simple greeting tool to test MCP connectivity.

### Input Schema
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Name to greet",
      "maxLength": 100
    }
  },
  "required": ["name"]
}
```

### Output Schema
```json
{
  "type": "object",
  "properties": {
    "greeting": {
      "type": "string",
      "description": "The greeting message"
    }
  }
}
```

### Constraints
- Input name must be non-empty
- No side effects
- Always returns a response

---

## read_repo_file

### Description
Read a file from the repository. Limited to safe directories.

### Input Schema
```json
{
  "type": "object",
  "properties": {
    "path": {
      "type": "string",
      "description": "Relative path to file from repo root",
      "pattern": "^[a-zA-Z0-9_\\-./]+$"
    }
  },
  "required": ["path"]
}
```

### Output Schema
```json
{
  "type": "object",
  "properties": {
    "content": {
      "type": "string",
      "description": "File contents"
    },
    "exists": {
      "type": "boolean",
      "description": "Whether file exists"
    },
    "error": {
      "type": "string",
      "description": "Error message if failed"
    }
  }
}
```

### Constraints
- **Allowed paths**:
  - `docs/*`
  - `paths/*`
  - `stacks/*`
  - `.claude/memory/*`
  - `.claude/commands/*`
  - `.claude/skills/*`
  - `README.md`
  - `CLAUDE.md`

- **Denied paths**:
  - `.env*`
  - `**/secrets*`
  - `**/*.key`
  - `**/*.pem`
  - `.git/*`

- **Size limit**: 100KB max file size
- **No directory listing**: Must specify exact file

---

## write_memory_entry

### Description
Append an entry to a memory file. Append-only, no overwriting.

### Input Schema
```json
{
  "type": "object",
  "properties": {
    "file": {
      "type": "string",
      "enum": ["progress_log.jsonl", "decisions.jsonl", "best_practices.md"],
      "description": "Target memory file"
    },
    "entry": {
      "type": "object",
      "description": "Entry to append (for JSONL files)",
      "properties": {
        "timestamp": {
          "type": "string",
          "format": "date-time"
        },
        "event": {
          "type": "string"
        }
      }
    },
    "content": {
      "type": "string",
      "description": "Content to append (for .md files)",
      "maxLength": 5000
    }
  },
  "required": ["file"]
}
```

### Output Schema
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "message": {
      "type": "string"
    }
  }
}
```

### Constraints
- **Append-only**: Cannot modify existing content
- **Target files only**: Only the three memory files listed
- **Size limit**: Max 5KB per entry
- **Timestamp required**: JSONL entries must have timestamp
- **No deletion**: Cannot remove entries
- **Requires approval**: Implementation should prompt user

---

## Tool Discovery

Tools can be discovered via the MCP protocol:

```json
{
  "jsonrpc": "2.0",
  "method": "tools/list",
  "id": 1
}
```

Response:
```json
{
  "jsonrpc": "2.0",
  "result": {
    "tools": [
      {
        "name": "hello",
        "description": "A simple greeting tool",
        "inputSchema": { ... }
      },
      {
        "name": "read_repo_file",
        "description": "Read a repository file",
        "inputSchema": { ... }
      },
      {
        "name": "write_memory_entry",
        "description": "Append to memory",
        "inputSchema": { ... }
      }
    ]
  },
  "id": 1
}
```

---

## Error Handling

All tools return errors in a consistent format:

```json
{
  "error": {
    "code": -32600,
    "message": "Invalid request",
    "data": {
      "details": "Specific error information"
    }
  }
}
```

### Error Codes
- `-32700`: Parse error
- `-32600`: Invalid request
- `-32601`: Tool not found
- `-32602`: Invalid params
- `-32603`: Internal error
- `-32000`: Access denied
- `-32001`: Path not allowed
- `-32002`: Size limit exceeded
