# MCP Examples

This document shows how agents use MCP tools in the learning OS.

## Basic Tool Usage

### Hello Tool (Testing)

```python
# Agent wants to test connectivity
request = {
    "tool": "hello",
    "input": {"name": "Learner"}
}

response = mcp_client.call(request)
# {"greeting": "Hello, Learner!"}
```

### Reading Documentation

```python
# Agent needs to check month goals
request = {
    "tool": "read_repo_file",
    "input": {"path": "paths/advanced/month-03/README.md"}
}

response = mcp_client.call(request)
# {"content": "# Month 03: RAG Systems\n...", "size": 4521}
```

### Logging Progress

```python
# Agent wants to log a completed task (after user approval)
request = {
    "tool": "write_memory_entry",
    "input": {
        "file": "progress_log.jsonl",
        "entry": {
            "timestamp": "2026-01-09T14:30:00Z",
            "type": "task_complete",
            "task": "Implemented retrieval function",
            "notes": "Tested with 5 documents"
        }
    }
}

response = mcp_client.call(request)
# {"success": true, "line_number": 42}
```

## Agent Workflows

### Planner Agent: Status Check

```python
# Planner reads memory to understand current state

# 1. Read learner profile
profile = mcp_client.call({
    "tool": "read_repo_file",
    "input": {"path": ".claude/memory/learner_profile.json"}
})

# 2. Read recent progress
progress = mcp_client.call({
    "tool": "read_repo_file",
    "input": {"path": ".claude/memory/progress_log.jsonl"}
})

# 3. Read current month
month_readme = mcp_client.call({
    "tool": "read_repo_file",
    "input": {"path": "paths/advanced/month-03/README.md"}
})

# 4. Synthesize status report
status = synthesize_status(profile, progress, month_readme)
```

### Builder Agent: Check Best Practices

```python
# Builder checks for relevant patterns before implementation

best_practices = mcp_client.call({
    "tool": "read_repo_file",
    "input": {"path": ".claude/memory/best_practices.md"}
})

# Parse and find relevant practices
relevant = find_relevant_practices(best_practices["content"], "RAG")
```

### Evaluator Agent: Log Decision

```python
# After user approves an adaptation

# 1. Present to user (not via MCP)
user_approved = present_adaptation_to_user(adaptation)

# 2. If approved, log the decision
if user_approved:
    mcp_client.call({
        "tool": "write_memory_entry",
        "input": {
            "file": "decisions.jsonl",
            "entry": {
                "timestamp": get_utc_timestamp(),
                "type": "adaptation_approved",
                "decision": "Insert remediation week after Month 03",
                "rationale": "Velocity below threshold",
                "user_approved": True
            }
        }
    })
```

## Error Handling

### Path Validation Error

```python
# Trying to read a forbidden path
response = mcp_client.call({
    "tool": "read_repo_file",
    "input": {"path": ".env"}
})
# {"error": "Path not allowed: .env"}
```

### File Not Found

```python
response = mcp_client.call({
    "tool": "read_repo_file",
    "input": {"path": "docs/nonexistent.md"}
})
# {"error": "File not found: docs/nonexistent.md"}
```

### Invalid Entry

```python
# Missing required field
response = mcp_client.call({
    "tool": "write_memory_entry",
    "input": {
        "file": "progress_log.jsonl",
        "entry": {"note": "Missing timestamp and type"}
    }
})
# {"error": "Validation failed: 'timestamp' is required"}
```

## Complete Workflow Example

```python
"""
Complete example: /evaluate command flow
"""

class EvaluatorAgent:
    def __init__(self, mcp_client):
        self.mcp = mcp_client

    def evaluate_month(self, month: int) -> dict:
        # 1. Gather data via MCP
        profile = self._read_file(".claude/memory/learner_profile.json")
        progress = self._read_file(".claude/memory/progress_log.jsonl")
        month_readme = self._read_file(f"paths/advanced/month-{month:02d}/README.md")

        # 2. Compute scores (internal logic)
        scores = self._compute_scores(profile, progress, month_readme)

        # 3. Generate report (returned to user, not written yet)
        return {
            "month": month,
            "scores": scores,
            "status": "PASSING" if scores["overall"] >= 70 else "NEEDS_ATTENTION",
            "recommendations": self._generate_recommendations(scores)
        }

    def _read_file(self, path: str) -> dict:
        response = self.mcp.call({
            "tool": "read_repo_file",
            "input": {"path": path}
        })
        if "error" in response:
            raise Exception(response["error"])
        return response

    def _compute_scores(self, profile, progress, month_readme):
        # Scoring logic here
        pass

    def _generate_recommendations(self, scores):
        # Recommendation logic here
        pass
```

## Best Practices

1. **Always handle errors** - Check for error responses
2. **Validate before writing** - Ensure entry format is correct
3. **User approval first** - Never write without explicit approval
4. **Read before recommend** - Gather context from memory
5. **Log decisions** - Record important choices to decisions.jsonl
