# MCP Usage Examples

How agents and commands use MCP tools.

## Basic Tool Call Pattern

```python
# 1. Prepare the request
tool_request = {
    "tool": "tool_name",
    "parameters": {
        "param1": "value1",
        "param2": "value2"
    }
}

# 2. Send to MCP server
response = mcp_client.call(tool_request)

# 3. Handle response
if response["success"]:
    result = response["result"]
else:
    error = response["error"]
```

---

## Example: Reading Progress Log

**Scenario**: Evaluator agent needs to read recent progress.

```python
# Read the progress log
response = mcp_client.call({
    "tool": "read_repo_file",
    "parameters": {
        "path": ".claude/memory/progress_log.jsonl"
    }
})

if response["success"]:
    content = response["result"]["content"]
    # Parse JSONL
    entries = [json.loads(line) for line in content.strip().split('\n')]
    # Filter recent entries
    recent = [e for e in entries if e["timestamp"] > cutoff_date]
```

---

## Example: Logging a Milestone

**Scenario**: Builder agent completed a milestone and wants to log it.

```python
import json
from datetime import datetime

# Prepare entry
entry = {
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "event": "milestone",
    "description": "Completed RAG pipeline implementation",
    "month": 3,
    "week": 2
}

# Request user approval first!
print("Proposed memory update:")
print(json.dumps(entry, indent=2))
approved = input("Approve this update? (yes/no): ")

if approved.lower() == "yes":
    response = mcp_client.call({
        "tool": "write_memory_entry",
        "parameters": {
            "file": "progress_log.jsonl",
            "entry": json.dumps(entry)
        }
    })

    if response["success"]:
        print(f"Logged: {response['result']['bytes_written']} bytes")
```

---

## Example: Adding Best Practice

**Scenario**: Coach agent helps capture a learning.

```python
# Format the best practice entry
entry = """
### RAG Evaluation Order
**Category**: RAG | **Added**: 2026-03-15

Always evaluate retrieval quality before debugging generation. Poor retrieval is often the root cause of poor answers.

**When to apply**: Building or debugging RAG systems.

**Example**: Spent 2 hours debugging prompts when the real issue was retrieval returning irrelevant chunks.

---
"""

# Show to user for approval
print("Proposed best practice entry:")
print(entry)
approved = input("Add this entry? (yes/no): ")

if approved.lower() == "yes":
    response = mcp_client.call({
        "tool": "write_memory_entry",
        "parameters": {
            "file": "best_practices.md",
            "entry": entry
        }
    })
```

---

## Example: Recording a Decision

**Scenario**: Path adaptation decision needs to be recorded.

```python
import json
from datetime import datetime

decision = {
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "type": "path_adaptation",
    "adaptation": "project_swap",
    "details": {
        "from_project": "Custom NER System",
        "to_project": "Sentiment Analysis API",
        "month": 4
    },
    "rationale": "Better alignment with learner's work domain",
    "approved_by": "learner"
}

# Always require explicit approval for decisions
print("Recording decision:")
print(json.dumps(decision, indent=2))
approved = input("Confirm this decision record? (yes/no): ")

if approved.lower() == "yes":
    response = mcp_client.call({
        "tool": "write_memory_entry",
        "parameters": {
            "file": "decisions.jsonl",
            "entry": json.dumps(decision)
        }
    })
```

---

## Error Handling Pattern

```python
def safe_tool_call(tool_name, parameters):
    """Make a tool call with proper error handling."""
    try:
        response = mcp_client.call({
            "tool": tool_name,
            "parameters": parameters
        })

        if not response.get("success"):
            error = response.get("error", "Unknown error")
            print(f"Tool call failed: {error}")
            return None

        return response["result"]

    except ConnectionError:
        print("Could not connect to MCP server")
        return None
    except TimeoutError:
        print("Tool call timed out")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
```

---

## Agent Integration Pattern

```python
class EvaluatorAgent:
    def __init__(self, mcp_client):
        self.mcp = mcp_client

    def read_progress(self):
        """Read progress log via MCP."""
        result = self.mcp.call({
            "tool": "read_repo_file",
            "parameters": {"path": ".claude/memory/progress_log.jsonl"}
        })
        if result["success"]:
            return self._parse_jsonl(result["result"]["content"])
        return []

    def log_evaluation(self, evaluation, user_approved=False):
        """Log evaluation result with user approval."""
        if not user_approved:
            print("User approval required before logging")
            return False

        entry = json.dumps({
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "event": "evaluation",
            "scores": evaluation["scores"],
            "summary": evaluation["summary"]
        })

        result = self.mcp.call({
            "tool": "write_memory_entry",
            "parameters": {
                "file": "progress_log.jsonl",
                "entry": entry
            }
        })
        return result["success"]
```

---

## See Also

- [tool-contracts.md](tool-contracts.md) — Full tool specifications
- [safety.md](safety.md) — Security considerations
- [server_stub/server.py](server_stub/server.py) — Server implementation
- [client_examples/python_client.py](client_examples/python_client.py) — Client code
