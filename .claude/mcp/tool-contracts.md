# MCP Tool Contracts

This document defines the tool contracts (schemas and constraints) for the AI Practitioner Learning OS MCP tools.

---

## Tool: hello

A simple test tool to verify MCP connectivity.

### Schema

```json
{
  "name": "hello",
  "description": "Returns a greeting message to verify MCP connectivity",
  "inputSchema": {
    "type": "object",
    "properties": {},
    "required": []
  },
  "outputSchema": {
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
    }
  }
}
```

### Example

**Request**:
```json
{"tool": "hello", "input": {}}
```

**Response**:
```json
{"message": "Hello from AI Practitioner Learning OS!", "timestamp": "2026-01-07T10:00:00Z"}
```

---

## Tool: read_repo_file

Read files from the repository with safety constraints.

### Schema

```json
{
  "name": "read_repo_file",
  "description": "Read a file from the repository (safe subset only)",
  "inputSchema": {
    "type": "object",
    "properties": {
      "path": {
        "type": "string",
        "description": "Relative path to the file from repo root"
      }
    },
    "required": ["path"]
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "content": {
        "type": "string",
        "description": "File contents"
      },
      "path": {
        "type": "string",
        "description": "Resolved file path"
      },
      "size_bytes": {
        "type": "integer",
        "description": "File size in bytes"
      }
    }
  }
}
```

### Constraints

**Allowed paths**:
- `paths/**` - Learning paths
- `docs/**` - Documentation
- `.claude/memory/**` - Memory files (read-only via this tool)
- `templates/**` - Project templates
- `examples/**` - Example code

**Blocked paths**:
- `.git/**` - Git internals
- `**/.env` - Environment files
- `**/secrets*` - Secret files
- `**/*.key` - Key files

### Example

**Request**:
```json
{"tool": "read_repo_file", "input": {"path": "paths/Beginner/README.md"}}
```

**Response**:
```json
{
  "content": "# Beginner Dashboard\n...",
  "path": "paths/Beginner/README.md",
  "size_bytes": 2048
}
```

---

## Tool: write_memory_entry

Append entries to memory files (append-only).

### Schema

```json
{
  "name": "write_memory_entry",
  "description": "Append an entry to a memory file (append-only)",
  "inputSchema": {
    "type": "object",
    "properties": {
      "file": {
        "type": "string",
        "enum": ["progress_log.jsonl", "decisions.jsonl"],
        "description": "Memory file to append to"
      },
      "entry": {
        "type": "object",
        "description": "JSON object to append"
      }
    },
    "required": ["file", "entry"]
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "success": {
        "type": "boolean"
      },
      "file": {
        "type": "string"
      },
      "entry_count": {
        "type": "integer",
        "description": "Total entries in file after append"
      }
    }
  }
}
```

### Constraints

**Allowed files**:
- `progress_log.jsonl` - Progress events
- `decisions.jsonl` - Decision records

**NOT allowed**:
- `learner_profile.json` - Must be edited manually
- `best_practices.md` - Use `/add-best-practice` command

**Entry requirements**:
- Must include `timestamp` field (ISO 8601 format)
- Must include `event` or `decision` field
- Size limit: 10KB per entry

### Example

**Request**:
```json
{
  "tool": "write_memory_entry",
  "input": {
    "file": "progress_log.jsonl",
    "entry": {
      "timestamp": "2026-01-07T14:00:00Z",
      "event": "task_completed",
      "task": "EDA notebook",
      "duration_hours": 2
    }
  }
}
```

**Response**:
```json
{
  "success": true,
  "file": "progress_log.jsonl",
  "entry_count": 15
}
```

---

## Error Responses

All tools return errors in this format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message"
  }
}
```

### Error Codes

| Code | Description |
|------|-------------|
| `INVALID_INPUT` | Input doesn't match schema |
| `PATH_NOT_ALLOWED` | Tried to access blocked path |
| `FILE_NOT_FOUND` | Requested file doesn't exist |
| `WRITE_NOT_ALLOWED` | Tried to write to read-only file |
| `ENTRY_TOO_LARGE` | Entry exceeds size limit |
| `INTERNAL_ERROR` | Server-side error |

---

## Rate Limits

For safety, tools have rate limits:

| Tool | Limit |
|------|-------|
| `hello` | 100/minute |
| `read_repo_file` | 60/minute |
| `write_memory_entry` | 30/minute |
