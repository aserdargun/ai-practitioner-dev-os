# Tool Contracts

Formal definitions of available MCP tools with schemas and constraints.

## Contract Format

Each tool contract specifies:
- **Name**: Tool identifier
- **Description**: What the tool does
- **Input Schema**: JSON Schema for parameters
- **Output Schema**: JSON Schema for results
- **Constraints**: Limitations and safety rules
- **Examples**: Usage examples

---

## hello

Test tool for verifying MCP connectivity.

### Input Schema
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Name to greet",
      "default": "World"
    }
  },
  "required": []
}
```

### Output Schema
```json
{
  "type": "object",
  "properties": {
    "message": {
      "type": "string",
      "description": "Greeting message"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "Server timestamp"
    }
  },
  "required": ["message", "timestamp"]
}
```

### Constraints
- No side effects
- Always succeeds

### Example
```json
// Input
{"name": "Learner"}

// Output
{"message": "Hello, Learner!", "timestamp": "2026-01-15T10:30:00Z"}
```

---

## read_repo_file

Read a file from the repository within safe boundaries.

### Input Schema
```json
{
  "type": "object",
  "properties": {
    "path": {
      "type": "string",
      "description": "Relative path from repo root",
      "pattern": "^[a-zA-Z0-9_./-]+$"
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
    "path": {
      "type": "string",
      "description": "Normalized path"
    },
    "size": {
      "type": "integer",
      "description": "File size in bytes"
    }
  },
  "required": ["content", "path"]
}
```

### Constraints
- **Allowed paths**: Only within repository root
- **Blocked patterns**:
  - `..` (path traversal)
  - `.env*` (environment files)
  - `*secret*`, `*credential*` (sensitive files)
  - `.git/` (git internals)
- **Size limit**: 1MB maximum
- **Read-only**: Cannot modify files

### Example
```json
// Input
{"path": ".claude/memory/progress_log.jsonl"}

// Output
{
  "content": "{\"timestamp\": \"2026-01-01...\n",
  "path": ".claude/memory/progress_log.jsonl",
  "size": 1234
}
```

---

## write_memory_entry

Append an entry to a memory file. Append-only operation.

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
      "type": "string",
      "description": "Content to append",
      "maxLength": 10000
    }
  },
  "required": ["file", "entry"]
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
    "file": {
      "type": "string"
    },
    "bytes_written": {
      "type": "integer"
    }
  },
  "required": ["success", "file"]
}
```

### Constraints
- **Append-only**: Cannot overwrite or delete
- **Allowed files**: Only the three memory files listed
- **Format validation**:
  - `.jsonl` files: Entry must be valid JSON
  - `.md` files: Entry is appended as-is with newline
- **Size limit**: 10KB per entry
- **Requires approval**: User must approve before write

### Example
```json
// Input
{
  "file": "progress_log.jsonl",
  "entry": "{\"timestamp\": \"2026-01-15T10:00:00Z\", \"event\": \"milestone\", \"description\": \"Completed EDA\"}"
}

// Output
{
  "success": true,
  "file": "progress_log.jsonl",
  "bytes_written": 98
}
```

---

## Tool Registration

Tools must be registered in the MCP server:

```python
TOOLS = {
    "hello": {
        "description": "Test connectivity",
        "handler": handle_hello,
        "schema": HELLO_SCHEMA
    },
    "read_repo_file": {
        "description": "Read repository file",
        "handler": handle_read_file,
        "schema": READ_FILE_SCHEMA
    },
    "write_memory_entry": {
        "description": "Append to memory file",
        "handler": handle_write_memory,
        "schema": WRITE_MEMORY_SCHEMA
    }
}
```

---

## Extending Tools

To add a new tool:

1. Define the contract in this file
2. Add handler in `server_stub/server.py`
3. Register in TOOLS dictionary
4. Update [examples.md](examples.md) with usage
5. Review [safety.md](safety.md) for constraints
