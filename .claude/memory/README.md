# Memory System

This folder is the local "memory store" for the learning OS. It contains append-only files that track your learning journey.

## Files

| File | Purpose | Format |
|------|---------|--------|
| `learner_profile.json` | Your goals, constraints, and schedule | JSON |
| `progress_log.jsonl` | Timestamped events (tasks, completions, etc.) | JSON Lines |
| `decisions.jsonl` | Important decisions and their rationale | JSON Lines |
| `best_practices.md` | Living document of learnings | Markdown |

## Human Oversight Requirement

**All memory updates require your explicit approval.**

Claude reads memory to provide context-aware suggestions, but:
- Claude must show proposed memory updates to you
- You review and approve before any write
- You have full control to edit memory files directly
- Memory is for record-keeping, not for autonomously changing behavior

## How Memory Works

### Reading Memory
Claude reads memory at the start of interactions to:
- Understand your goals and constraints
- See recent progress and patterns
- Recall previous decisions
- Reference best practices you've captured

### Proposing Updates
When Claude suggests a memory update:
```
I'd like to log this event to progress_log.jsonl:
{"timestamp": "2026-03-15T10:30:00", "event": "task_completed", "task": "Finish EDA notebook"}

Approve? (y/n)
```

You decide whether to accept, modify, or reject.

### Your Control
You can always:
- Edit any memory file directly
- Delete entries
- Reorganize content
- Export for backup

## File Details

### learner_profile.json
Your personal configuration:
```json
{
  "level": "beginner",
  "goals": ["Build ML portfolio", "Get first AI job"],
  "constraints": {
    "hours_per_week": 10,
    "preferred_schedule": "evenings"
  },
  "start_date": "2026-01-01"
}
```

### progress_log.jsonl
Timestamped events, one per line:
```json
{"timestamp": "2026-01-15T09:00:00", "event": "week_started", "month": 1, "week": 2}
{"timestamp": "2026-01-15T18:30:00", "event": "task_completed", "task": "Set up Python environment"}
{"timestamp": "2026-01-19T20:00:00", "event": "week_completed", "month": 1, "week": 2, "rating": 4}
```

### decisions.jsonl
Important decisions with context:
```json
{"timestamp": "2026-02-01T10:00:00", "decision": "Skip Week 3 project", "rationale": "Sick this week, will catch up next month", "approved_by": "learner"}
{"timestamp": "2026-03-01T09:00:00", "decision": "Stay at Beginner level", "rationale": "Evaluation shows gaps in fundamentals", "approved_by": "learner"}
```

### best_practices.md
Living document of learnings:
```markdown
# Best Practices

## Data Engineering

### Always validate input data types before processing
*Captured: 2026-03-15 | Source: Month 3 project*

Check types before processing to catch issues early...

## Testing

### Write one failing test before implementing a feature
*Captured: 2026-02-20 | Source: Code review feedback*

TDD helps clarify requirements...
```

## Important Notes

### Append-Only Design
Memory files are designed to be **append-only**:
- New events are added, not overwritten
- History is preserved
- You can always see the full journey

### tracker.md is Different
The file `paths/beginner/tracker.md` is a **derived artifact**:
- Generated from memory files by `report.py`
- Can be regenerated anytime
- Not a source of truth (memory files are)

### Privacy
These files stay in your repository:
- Not sent to external services
- You control what's logged
- Delete anything you want

## Commands That Use Memory

| Command | Reads | Writes (with approval) |
|---------|-------|------------------------|
| `/status` | All files | - |
| `/plan-week` | profile, progress | progress_log |
| `/evaluate` | All files | progress_log |
| `/adapt-path` | All files | decisions |
| `/add-best-practice` | best_practices | best_practices |
| `/retro` | progress_log | progress_log, best_practices |

## Backup Recommendation

Periodically backup your memory folder:
```bash
cp -r .claude/memory .claude/memory-backup-$(date +%Y%m%d)
```

Or commit to git regularly — memory files are safe to version control.
