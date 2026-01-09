# MCP Tool Examples

How agents use MCP tools in the learning OS.

## Example 1: Testing Connectivity

### Scenario
Agent wants to verify MCP is working before proceeding.

### Tool Call
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "hello",
    "arguments": {
      "name": "Learner"
    }
  },
  "id": 1
}
```

### Response
```json
{
  "jsonrpc": "2.0",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\"greeting\": \"Hello, Learner! MCP is working.\"}"
      }
    ]
  },
  "id": 1
}
```

---

## Example 2: Reading Progress

### Scenario
Evaluator agent needs to read progress log for evaluation.

### Tool Call
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "read_repo_file",
    "arguments": {
      "path": ".claude/memory/progress_log.jsonl"
    }
  },
  "id": 2
}
```

### Response
```json
{
  "jsonrpc": "2.0",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\"content\": \"{\\\"timestamp\\\": \\\"2026-01-15T09:00:00\\\", \\\"event\\\": \\\"week_started\\\"}\\n{\\\"timestamp\\\": \\\"2026-01-19T18:00:00\\\", \\\"event\\\": \\\"week_completed\\\"}\", \"exists\": true}"
      }
    ]
  },
  "id": 2
}
```

---

## Example 3: Reading Month Goals

### Scenario
Planner agent needs to see current month's goals.

### Tool Call
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "read_repo_file",
    "arguments": {
      "path": "paths/beginner/month-03/README.md"
    }
  },
  "id": 3
}
```

### Response
```json
{
  "jsonrpc": "2.0",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\"content\": \"# Month 3: Data Pipelines\\n\\n## Learning Goals\\n- Build end-to-end data pipeline\\n- ...\", \"exists\": true}"
      }
    ]
  },
  "id": 3
}
```

---

## Example 4: Logging Progress Event

### Scenario
After user completes a task, log the event (with approval).

### Tool Call
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "write_memory_entry",
    "arguments": {
      "file": "progress_log.jsonl",
      "entry": {
        "timestamp": "2026-03-15T14:30:00Z",
        "event": "task_completed",
        "task": "Implement data validation",
        "month": 3,
        "week": 2
      }
    }
  },
  "id": 4
}
```

### Response
```json
{
  "jsonrpc": "2.0",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\"success\": true, \"message\": \"Entry appended to progress_log.jsonl\"}"
      }
    ]
  },
  "id": 4
}
```

---

## Example 5: Adding Best Practice

### Scenario
Coach agent helps capture a learning.

### Tool Call
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "write_memory_entry",
    "arguments": {
      "file": "best_practices.md",
      "content": "\n### Always validate input data types before processing\n*Captured: 2026-03-15 | Source: Month 3 project*\n\nBefore processing any DataFrame, verify column types match expectations.\n"
    }
  },
  "id": 5
}
```

### Response
```json
{
  "jsonrpc": "2.0",
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\"success\": true, \"message\": \"Content appended to best_practices.md\"}"
      }
    ]
  },
  "id": 5
}
```

---

## Example 6: Recording a Decision

### Scenario
After adapt-path recommendation is approved, log the decision.

### Tool Call
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "write_memory_entry",
    "arguments": {
      "file": "decisions.jsonl",
      "entry": {
        "timestamp": "2026-03-15T15:00:00Z",
        "decision": "Insert remediation week",
        "rationale": "Quality score below target, need focused testing practice",
        "approved_by": "learner",
        "category": "path_adaptation"
      }
    }
  },
  "id": 6
}
```

---

## Example 7: Denied Read (Safety)

### Scenario
Attempting to read a file outside allowed paths.

### Tool Call
```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "read_repo_file",
    "arguments": {
      "path": ".env"
    }
  },
  "id": 7
}
```

### Response
```json
{
  "jsonrpc": "2.0",
  "error": {
    "code": -32001,
    "message": "Path not allowed",
    "data": {
      "path": ".env",
      "reason": "Environment files are restricted for security"
    }
  },
  "id": 7
}
```

---

## Agent Integration Pattern

Typical flow for agents using MCP:

```
1. Agent receives user request
2. Agent determines needed information
3. Agent calls read_repo_file for context
4. Agent processes and generates response
5. Agent proposes memory update to user
6. If approved, agent calls write_memory_entry
7. Agent confirms completion to user
```

### Code Example (Python)

```python
async def handle_status_request(client):
    # Read current progress
    progress = await client.call_tool("read_repo_file", {
        "path": ".claude/memory/progress_log.jsonl"
    })

    # Read learner profile
    profile = await client.call_tool("read_repo_file", {
        "path": ".claude/memory/learner_profile.json"
    })

    # Generate status report
    report = generate_status(progress, profile)

    return report
```
