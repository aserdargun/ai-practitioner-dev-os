# Memory System

How the learning OS stores and uses your learning history.

## Overview

The memory system stores your learning journey in local files:
- **Append-only**: New entries added, never overwritten
- **Human-readable**: JSON and Markdown formats
- **Your control**: You can read, edit, or delete anything

Memory files live in: [.claude/memory/](../.claude/memory/)

---

## Memory Files

| File | Purpose | Format |
|------|---------|--------|
| `learner_profile.json` | Goals, constraints, preferences | JSON |
| `progress_log.jsonl` | Timestamped events | JSON Lines |
| `decisions.jsonl` | Important decisions | JSON Lines |
| `best_practices.md` | Captured learnings | Markdown |

---

## Learner Profile

**File**: `learner_profile.json`

Stores your configuration and preferences:

```json
{
  "level": "beginner",
  "goals": [
    "Build AI/ML portfolio",
    "Develop practical skills"
  ],
  "constraints": {
    "hours_per_week": 10,
    "preferred_schedule": "evenings"
  },
  "learning_style": {
    "prefers": ["hands-on projects", "visual learning"],
    "challenges": ["time management"]
  },
  "start_date": "2026-01-01"
}
```

### Editing
You can edit this file directly to update:
- Available hours
- Learning preferences
- Goals
- Schedule constraints

---

## Progress Log

**File**: `progress_log.jsonl`

Timestamped events, one JSON object per line:

```json
{"timestamp": "2026-01-15T09:00:00Z", "event": "week_started", "month": 1, "week": 2}
{"timestamp": "2026-01-15T18:30:00Z", "event": "task_completed", "task": "Set up Python environment"}
{"timestamp": "2026-01-19T20:00:00Z", "event": "week_completed", "month": 1, "week": 2, "rating": 4}
```

### Event Types
| Event | When Logged |
|-------|-------------|
| `week_started` | Starting a new week |
| `week_completed` | Finishing a week |
| `task_completed` | Completing a task |
| `retro_completed` | Finishing retrospective |
| `evaluation_run` | Running evaluation |

### Reading
```bash
# View all events
cat .claude/memory/progress_log.jsonl

# Count events
wc -l .claude/memory/progress_log.jsonl

# Filter by event type
grep "week_completed" .claude/memory/progress_log.jsonl
```

---

## Decisions Log

**File**: `decisions.jsonl`

Important decisions with rationale:

```json
{"timestamp": "2026-02-01T10:00:00Z", "decision": "Skip Week 3 project", "rationale": "Sick this week, will catch up", "approved_by": "learner"}
{"timestamp": "2026-03-01T09:00:00Z", "decision": "Insert remediation week", "rationale": "Quality score below target", "approved_by": "learner"}
```

### When Logged
- Path adaptations (approved)
- Level changes
- Project swaps
- Significant schedule changes

---

## Best Practices

**File**: `best_practices.md`

Living document of your learnings:

```markdown
# Best Practices

## Data Engineering

### Always validate input data types before processing
*Captured: 2026-03-15 | Source: Month 3 project*

Before processing any DataFrame, verify column types match expectations.

## Testing

### Write one failing test before implementing a feature
*Captured: 2026-02-20 | Source: Code review feedback*

TDD helps clarify requirements and catch bugs early.
```

### Adding Entries
Via command:
```
/add-best-practice
Always check for null values before aggregations
```

Or edit the file directly.

---

## Human Oversight

### Claude's Access
Claude reads memory to:
- Understand your context
- See recent progress
- Recall past decisions
- Reference your learnings

### Your Control
- Claude must ask before writing to memory
- You review and approve all updates
- You can edit or delete any entry
- Memory files are just text files

### Approval Flow
```
Claude: "I'd like to log this to progress_log.jsonl:
        {'event': 'task_completed', 'task': 'Finish EDA'}
        Approve? (y/n)"

You: "y"

Claude: [writes entry]
```

---

## How Memory Is Used

### By Commands

| Command | Reads | May Write (with approval) |
|---------|-------|---------------------------|
| `/status` | All files | - |
| `/plan-week` | profile, progress | progress_log |
| `/evaluate` | All files | progress_log |
| `/adapt-path` | All files | decisions |
| `/retro` | progress_log | progress_log, best_practices |
| `/add-best-practice` | best_practices | best_practices |

### By Path Engine

```bash
# Reads memory, outputs scores
python .claude/path-engine/evaluate.py

# Reads memory, proposes changes
python .claude/path-engine/adapt.py

# Reads memory, updates tracker
python .claude/path-engine/report.py
```

---

## Tracker vs Memory

**Important distinction**:

| Memory Files | Tracker |
|--------------|---------|
| Source of truth | Derived artifact |
| Append-only | Can be regenerated |
| Manual edits OK | Report.py overwrites |

`paths/beginner/tracker.md` is generated from memory files by `report.py`. If you edit tracker.md directly, your changes may be overwritten.

**Always edit memory files for permanent changes.**

---

## Backup

Memory files are safe to commit to git:
```bash
git add .claude/memory/
git commit -m "Update learning memory"
```

Manual backup:
```bash
cp -r .claude/memory .claude/memory-backup-$(date +%Y%m%d)
```

---

## Privacy

Memory stays local:
- Not sent to external services
- Stored only in your repository
- You control what's logged
- Delete anything you want

---

## Troubleshooting

### "Memory seems empty"
Run a few commands to populate:
```
/start-week
[do some work]
/retro
```

### "Want to reset memory"
Delete contents (keep files):
```bash
echo '[]' > .claude/memory/progress_log.jsonl
echo '[]' > .claude/memory/decisions.jsonl
```

### "Tracker is wrong"
Regenerate from memory:
```bash
python .claude/path-engine/report.py
```

---

## Best Practices for Memory

1. **Log regularly**: Small, frequent entries beat big batches
2. **Be specific**: "Finished API endpoint" beats "Did stuff"
3. **Capture learnings**: Best practices compound over time
4. **Review monthly**: Read through your progress log occasionally
5. **Keep it honest**: Memory helps you, not judges you
