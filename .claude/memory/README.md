# Memory System

This folder is the **source of truth** for your learning state. All memory files are append-only.

## Files

| File | Purpose | Format |
|------|---------|--------|
| [learner_profile.json](learner_profile.json) | Goals, constraints, preferences | JSON |
| [progress_log.jsonl](progress_log.jsonl) | Timestamped events | JSON Lines |
| [decisions.jsonl](decisions.jsonl) | Important decisions | JSON Lines |
| [best_practices.md](best_practices.md) | Accumulated learnings | Markdown |

## Important Principles

### 1. Append-Only
Memory files are append-only. Old entries are never deleted or modified. This provides a complete history of your learning journey.

### 2. Human Approval Required
Claude must show proposed memory updates to you and receive explicit approval before writing. Memory is for record-keeping, not for autonomous modifications.

### 3. Source of Truth
These files are the authoritative record. `paths/intermediate/tracker.md` is a derived artifact that `report.py` may regenerate.

## File Details

### learner_profile.json

Your learning configuration:
```json
{
  "level": "intermediate",
  "goals": ["list of learning goals"],
  "constraints": {
    "hours_per_week": 10,
    "preferred_times": ["evenings", "weekends"]
  },
  "preferences": {
    "learning_style": "project-based",
    "communication": "direct"
  }
}
```

### progress_log.jsonl

Event stream of your journey:
```json
{"timestamp": "2026-01-15T09:00:00Z", "event": "week_start", "week": "3"}
{"timestamp": "2026-01-15T18:30:00Z", "event": "milestone", "description": "Completed EDA"}
{"timestamp": "2026-01-19T17:00:00Z", "event": "week_end", "week": "3"}
```

### decisions.jsonl

Important choices recorded:
```json
{"timestamp": "2026-02-01T10:00:00Z", "type": "project_choice", "choice": "RAG over fine-tuning", "rationale": "Better fit for current skills"}
{"timestamp": "2026-03-15T14:00:00Z", "type": "path_adaptation", "adaptation": "month_reorder", "approved_by": "learner"}
```

### best_practices.md

Living document of learnings. Append new entries; don't modify old ones.

## How Memory is Used

1. **Claude reads** memory to understand context
2. **Claude proposes** updates based on activities
3. **You review** proposed updates
4. **You approve** (or reject/modify)
5. **Memory is written** only after approval

## Editing Memory

You have full control over memory files:
- Review and correct any inaccuracies
- Add context that Claude missed
- Remove truly erroneous entries (rare)

## Related Documentation

- [docs/memory-system.md](../../docs/memory-system.md) — Complete guide
- [path-engine/evaluate.py](../path-engine/evaluate.py) — Reads memory for evaluation
- [path-engine/report.py](../path-engine/report.py) — Generates tracker from memory
