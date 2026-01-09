# Tool Contracts

This document defines the schemas and constraints for MCP tools in this learning OS.

## Contract Structure

Each tool contract specifies:
- **Name**: Tool identifier
- **Description**: What the tool does
- **Input Schema**: Expected parameters (JSON Schema)
- **Output Schema**: Return value format
- **Constraints**: Limitations and safety rules

---

## Tool: hello

### Description
A simple greeting tool for testing MCP connectivity.

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
      "type": "string"
    }
  }
}
```

### Constraints
- No side effects
- Always returns successfully
- For testing only

---

## Tool: read_repo_file

### Description
Read a file from the repository. Limited to safe paths only.

### Input Schema
```json
{
  "type": "object",
  "properties": {
    "path": {
      "type": "string",
      "description": "Relative path from repo root",
      "pattern": "^[a-zA-Z0-9/_.-]+$",
      "maxLength": 256
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
      "description": "File content"
    },
    "size": {
      "type": "integer",
      "description": "File size in bytes"
    }
  }
}
```

### Constraints
- **Allowed paths**:
  - `docs/**`
  - `paths/**`
  - `stacks/**`
  - `.claude/memory/**` (read-only)
  - `README.md`, `CLAUDE.md`
- **Denied paths**:
  - `.env*`
  - `**/secrets/**`
  - `**/.git/**`
  - Any path with `..`
- Maximum file size: 1MB
- Text files only (UTF-8)

---

## Tool: write_memory_entry

### Description
Append an entry to a memory file. Append-only, never overwrites.

### Input Schema
```json
{
  "type": "object",
  "properties": {
    "file": {
      "type": "string",
      "enum": ["progress_log.jsonl", "decisions.jsonl"],
      "description": "Which memory file to append to"
    },
    "entry": {
      "type": "object",
      "description": "JSON object to append",
      "properties": {
        "timestamp": {
          "type": "string",
          "format": "date-time"
        },
        "type": {
          "type": "string"
        }
      },
      "required": ["timestamp", "type"]
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
    "line_number": {
      "type": "integer",
      "description": "Line number of appended entry"
    }
  }
}
```

### Constraints
- **Append-only**: Never modifies existing content
- **Allowed files**: Only `progress_log.jsonl` and `decisions.jsonl`
- **Entry validation**: Must include timestamp and type
- **Human approval**: Claude must obtain user approval before calling
- Maximum entry size: 10KB

---

## Adding New Tools

When adding a new tool:

1. Define the contract in this file
2. Implement in `server_stub/server.py`
3. Add safety checks per `safety.md`
4. Document in `examples.md`
5. Test thoroughly

### Contract Template

```markdown
## Tool: my_new_tool

### Description
[What it does]

### Input Schema
```json
{
  "type": "object",
  "properties": {
    // ...
  },
  "required": []
}
```

### Output Schema
```json
{
  "type": "object",
  "properties": {
    // ...
  }
}
```

### Constraints
- [Constraint 1]
- [Constraint 2]
```

## Validation

All tool inputs are validated against their schemas before execution. Invalid inputs return an error without executing.

```python
def validate_input(tool_name: str, input_data: dict) -> bool:
    schema = TOOL_SCHEMAS[tool_name]["input"]
    try:
        jsonschema.validate(input_data, schema)
        return True
    except jsonschema.ValidationError:
        return False
```
