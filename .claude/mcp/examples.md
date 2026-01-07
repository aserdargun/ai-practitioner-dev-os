# MCP Examples

This document shows how agents and scripts use MCP tools in the AI Practitioner Learning OS.

---

## Example 1: Status Check

The Planner Agent uses MCP to read current progress:

```python
# Read learner profile
profile = mcp.call_tool("read_repo_file", {
    "path": ".claude/memory/learner_profile.json"
})

# Read recent progress
progress = mcp.call_tool("read_repo_file", {
    "path": ".claude/memory/progress_log.jsonl"
})

# Parse and analyze
import json
profile_data = json.loads(profile["content"])
progress_lines = [json.loads(line) for line in progress["content"].strip().split("\n")]

# Generate status
current_month = profile_data["current_month"]
recent_events = progress_lines[-10:]  # Last 10 events
```

---

## Example 2: Logging Progress

The Builder Agent logs task completion:

```python
from datetime import datetime

# Log task completion
mcp.call_tool("write_memory_entry", {
    "file": "progress_log.jsonl",
    "entry": {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": "task_completed",
        "task": "Implement data cleaning pipeline",
        "duration_hours": 3,
        "artifacts": ["pipeline/clean.py", "tests/test_clean.py"]
    }
})
```

---

## Example 3: Recording Decisions

The Evaluator Agent records adaptation decisions:

```python
from datetime import datetime

# Record level change decision
mcp.call_tool("write_memory_entry", {
    "file": "decisions.jsonl",
    "entry": {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "decision": "remediation_week",
        "month": 3,
        "week": 3,
        "focus": "pandas fundamentals",
        "rationale": "Struggling with groupby and merge operations",
        "triggered_by": "evaluation_score < 60"
    }
})
```

---

## Example 4: Reading Documentation

The Researcher Agent reads skill documentation:

```python
# Read a skill playbook
skill = mcp.call_tool("read_repo_file", {
    "path": ".claude/skills/eda-to-insight.md"
})

# Extract steps (simple parsing)
content = skill["content"]
steps = []
in_steps = False
for line in content.split("\n"):
    if line.startswith("### Step"):
        in_steps = True
        steps.append(line)
    elif in_steps and line.startswith("###"):
        steps.append(line)

print(f"Found {len(steps)} steps in EDA skill")
```

---

## Example 5: Weekly Report Generation

The report script reads all memory files:

```python
def generate_weekly_report(week_num):
    # Read all relevant data
    profile = json.loads(
        mcp.call_tool("read_repo_file", {"path": ".claude/memory/learner_profile.json"})["content"]
    )

    progress_raw = mcp.call_tool("read_repo_file", {"path": ".claude/memory/progress_log.jsonl"})["content"]
    progress = [json.loads(line) for line in progress_raw.strip().split("\n") if line]

    # Filter to current week
    week_events = [e for e in progress if e.get("week") == week_num]

    # Calculate metrics
    tasks_completed = len([e for e in week_events if e.get("event") == "task_completed"])
    total_hours = sum(e.get("duration_hours", 0) for e in week_events)

    return {
        "week": week_num,
        "level": profile["level"],
        "tasks_completed": tasks_completed,
        "hours_logged": total_hours
    }
```

---

## Example 6: Full Evaluation Flow

```python
# 1. Read memory
profile = read_profile()
progress = read_progress()
decisions = read_decisions()

# 2. Calculate scores
scores = calculate_scores(progress)

# 3. Log evaluation event
mcp.call_tool("write_memory_entry", {
    "file": "progress_log.jsonl",
    "entry": {
        "timestamp": now(),
        "event": "evaluation",
        "overall_score": scores["overall"],
        "categories": scores["categories"],
        "recommendations": generate_recommendations(scores)
    }
})

# 4. Check if adaptation needed
if scores["overall"] < 60:
    adaptation = propose_adaptation(scores, progress)

    # 5. Log adaptation decision
    mcp.call_tool("write_memory_entry", {
        "file": "decisions.jsonl",
        "entry": {
            "timestamp": now(),
            "decision": adaptation["type"],
            **adaptation["details"],
            "rationale": adaptation["rationale"]
        }
    })
```

---

## Error Handling

Always handle potential errors:

```python
try:
    result = mcp.call_tool("read_repo_file", {"path": "some/path.md"})
    content = result["content"]
except MCPError as e:
    if e.code == "FILE_NOT_FOUND":
        print(f"File not found: {e.message}")
        content = ""
    elif e.code == "PATH_NOT_ALLOWED":
        print(f"Access denied: {e.message}")
        raise
    else:
        raise
```

---

## Best Practices

1. **Always include timestamps** in entries
2. **Keep entries small** (< 10KB)
3. **Use structured events** with consistent schemas
4. **Handle errors gracefully** - don't crash on missing files
5. **Validate before writing** - ensure entries have required fields
