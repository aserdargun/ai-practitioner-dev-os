# Memory System

How learning state is tracked and managed.

---

## Overview

The memory system maintains all state about your learning journey. It uses simple, human-readable files that follow an append-only discipline.

---

## Memory Files

Located in `.claude/memory/`:

| File | Format | Purpose | Update Pattern |
|------|--------|---------|----------------|
| `learner_profile.json` | JSON | Configuration | Modify carefully |
| `progress_log.jsonl` | JSON Lines | Activity history | Append-only |
| `decisions.jsonl` | JSON Lines | Path decisions | Append-only |
| `best_practices.md` | Markdown | Learnings | Append-only |

---

## Learner Profile

**File**: `learner_profile.json`

**Purpose**: Stores your configuration and preferences.

**Structure**:
```json
{
  "learner_id": "learner-001",
  "level": "Advanced",
  "tier_scope": ["Tier1", "Tier2", "Tier3"],
  "start_date": "2026-01-01",
  "current_month": 1,
  "current_week": 1,
  "preferences": {
    "learning_style": "hands-on",
    "session_length_minutes": 120,
    "preferred_domains": ["ml-engineering"],
    "timezone": "UTC"
  },
  "goals": {
    "primary": "Become a production-ready AI practitioner",
    "secondary": ["Build portfolio", "Master MLOps"]
  },
  "background": {
    "programming_experience_years": 3,
    "ml_experience_level": "intermediate",
    "strongest_skills": ["python", "data-analysis"],
    "areas_to_improve": ["deployment", "system-design"]
  },
  "metadata": {
    "created_at": "2026-01-01T00:00:00Z",
    "last_updated": "2026-01-01T00:00:00Z",
    "version": "1.0"
  }
}
```

**When to Update**:
- Changing preferences
- Updating goals
- Recording level changes (after adaptation)

**Caution**: Changes affect evaluation and planning. Update thoughtfully.

---

## Progress Log

**File**: `progress_log.jsonl`

**Purpose**: Chronological record of all learning activities.

**Format**: JSON Lines (one JSON object per line)

**Entry Structure**:
```json
{"timestamp": "2026-01-15T10:30:00Z", "event": "task_completed", "message": "Finished data validation pipeline", "metadata": {"task_id": "week3-task2", "duration_minutes": 45}}
```

**Event Types**:

| Event | Description |
|-------|-------------|
| `system_initialized` | Learning system started |
| `month_started` | New month began |
| `week_started` | New week began |
| `task_started` | Started working on a task |
| `task_completed` | Finished a task |
| `task_blocked` | Hit a blocker |
| `blocker_resolved` | Resolved a blocker |
| `evaluation_completed` | Ran evaluation |
| `retro_completed` | Finished retrospective |
| `best_practice_added` | Captured a learning |

**Example Entries**:
```json
{"timestamp": "2026-01-08T09:00:00Z", "event": "week_started", "message": "Starting Week 2 of Month 01"}
{"timestamp": "2026-01-08T09:15:00Z", "event": "task_started", "message": "Beginning environment setup task"}
{"timestamp": "2026-01-08T11:30:00Z", "event": "task_completed", "message": "Environment setup complete", "metadata": {"duration_minutes": 135}}
{"timestamp": "2026-01-08T11:45:00Z", "event": "task_blocked", "message": "Can't install CUDA drivers", "metadata": {"blocker_type": "technical"}}
{"timestamp": "2026-01-08T14:00:00Z", "event": "blocker_resolved", "message": "Used CPU-only PyTorch instead"}
```

**Rules**:
- **Never delete entries** — history must be preserved
- **Always include timestamp** — ISO 8601 format with timezone
- **Include relevant metadata** — helps with analysis

---

## Decisions Log

**File**: `decisions.jsonl`

**Purpose**: Record of all path adaptation decisions.

**Format**: JSON Lines

**Entry Structure**:
```json
{"timestamp": "2026-01-15T18:00:00Z", "decision_type": "remediation_week", "value": true, "reason": "Quality scores below threshold", "approved": true, "applied": true}
```

**Decision Types**:

| Type | Description |
|------|-------------|
| `level_selection` | Initial level choice |
| `level_change` | Upgrade or downgrade |
| `month_reorder` | Swap month order |
| `remediation_week` | Insert catch-up week |
| `project_swap` | Replace project |

**Example Entries**:
```json
{"timestamp": "2026-01-01T00:00:00Z", "decision_type": "level_selection", "value": "Advanced", "reason": "Learner selected Advanced level", "approved": true}
{"timestamp": "2026-02-01T18:00:00Z", "decision_type": "remediation_week", "value": true, "reason": "Quality score at 52%, below 60% threshold", "approved": true, "applied": true}
```

**Rules**:
- **Append-only** — decisions form an audit trail
- **Include approval status** — who/what approved
- **Include application status** — whether it was actually applied

---

## Best Practices

**File**: `best_practices.md`

**Purpose**: Accumulated learnings and patterns.

**Format**: Markdown with structured entries

**Entry Structure**:
```markdown
### 2026-01-15 - Always Validate at Boundaries

**Context**: When building APIs

**Practice**: Validate all input at API boundaries using Pydantic.

**Why**: Catches errors early, provides clear error messages.

**Example**:
```python
from pydantic import BaseModel, validator

class UserInput(BaseModel):
    name: str
    age: int

    @validator('age')
    def age_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('age must be positive')
        return v
```

---
```

**Adding Entries**:
- Use `/add-best-practice` command
- Or append manually following the format

**Rules**:
- **Append only** — never remove existing entries
- **Date each entry** — for historical context
- **Include examples** — makes practices actionable

---

## Memory Operations

### Reading Memory

The path-engine scripts read memory:

```python
# In evaluate.py
def read_progress_log():
    with open(MEMORY_DIR / "progress_log.jsonl") as f:
        return [json.loads(line) for line in f if line.strip()]
```

### Writing Memory

Always append, never overwrite:

```python
# In log_progress function
def append_to_log(entry):
    with open(MEMORY_DIR / "progress_log.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")
```

### Memory in Commands

Commands interact with memory automatically:

| Command | Reads | Writes |
|---------|-------|--------|
| `/status` | profile, progress_log | — |
| `/evaluate` | all | — |
| `/plan-week` | profile, progress_log | progress_log |
| `/retro` | progress_log | progress_log |
| `/add-best-practice` | — | best_practices.md |
| `/adapt-path` | all | decisions.jsonl |

---

## Memory Integrity

### Validation

The system validates memory files on startup:

1. Check files exist
2. Verify JSON validity
3. Check required fields

### Recovery

If memory is corrupted:

1. Check git history for last good version
2. Restore from backup
3. Re-initialize if necessary (loses history)

### Backup

Memory files are in git, providing:
- Version history
- Easy rollback
- Sync across machines

---

## Analyzing Memory

### Progress Patterns

```python
import json
from collections import Counter

with open(".claude/memory/progress_log.jsonl") as f:
    events = [json.loads(line) for line in f]

# Event frequency
event_counts = Counter(e["event"] for e in events)
print("Event counts:", event_counts)

# Completion rate
completed = sum(1 for e in events if "completed" in e["event"])
started = sum(1 for e in events if "started" in e["event"])
print(f"Completion rate: {completed}/{started}")
```

### Decision History

```python
with open(".claude/memory/decisions.jsonl") as f:
    decisions = [json.loads(line) for line in f]

# Group by type
by_type = {}
for d in decisions:
    t = d["decision_type"]
    by_type.setdefault(t, []).append(d)

for t, items in by_type.items():
    print(f"{t}: {len(items)} decisions")
```

---

## Best Practices for Memory

### Do

- Log progress frequently
- Include meaningful metadata
- Use consistent event names
- Back up regularly (git push)

### Don't

- Delete entries
- Modify historical entries
- Store sensitive data
- Ignore memory errors

---

## See Also

- [System Overview](system-overview.md) — Architecture
- [Evaluation Rubric](evaluation/rubric.md) — How memory is scored
- [How to Use](how-to-use.md) — Daily workflow
