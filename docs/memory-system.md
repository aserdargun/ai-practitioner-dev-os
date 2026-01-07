# Memory System Guide

The memory system is how the AI Practitioner Learning OS tracks your progress, decisions, and accumulated wisdom. This guide explains how it works and how to use it.

For the actual memory files, see [.claude/memory/](../.claude/memory/).

## Overview

The memory system consists of four files:

| File | Purpose | Format | Update Pattern |
|------|---------|--------|----------------|
| `learner_profile.json` | Your goals and constraints | JSON | Manual edit |
| `progress_log.jsonl` | Progress events | JSONL | Append-only |
| `decisions.jsonl` | Important decisions | JSONL | Append-only |
| `best_practices.md` | Accumulated wisdom | Markdown | Append |

## Key Principle: Append-Only

**Memory files are append-only sources of truth.**

- Never delete or modify existing entries
- Only append new entries
- History is preserved for learning and analysis

The tracker at `paths/Beginner/tracker.md` is a **derived artifact** that can be regenerated from memory files at any time using `report.py`.

---

## learner_profile.json

Your personal profile and constraints.

### Structure

```json
{
  "level": "Beginner",
  "started": "2026-01-01",
  "current_month": 1,
  "current_week": 1,
  "goals": [
    "Master Python data science fundamentals",
    "Build a portfolio of ML projects"
  ],
  "constraints": {
    "hours_per_week": 10,
    "preferred_days": ["Monday", "Tuesday", "Wednesday"],
    "timezone": "UTC"
  },
  "interests": ["NLP", "time series"],
  "background": "Software developer with 2 years experience"
}
```

### When to Edit

Edit this file manually when:
- Starting the learning journey (initial setup)
- Changing your available time
- Updating goals
- Changing level (after adaptation approval)

### How to Edit

1. Open `.claude/memory/learner_profile.json`
2. Make changes
3. Save the file

Or ask Claude:
```
Please update my learner profile:
- Change hours_per_week to 15
- Add "computer vision" to interests
```

---

## progress_log.jsonl

A chronological log of all progress events.

### Format

One JSON object per line (JSONL format):

```json
{"timestamp": "2026-01-07T09:00:00Z", "event": "week_start", "week": 2, "month": 1}
{"timestamp": "2026-01-07T14:00:00Z", "event": "task_completed", "task": "EDA notebook", "duration_hours": 2}
{"timestamp": "2026-01-10T17:00:00Z", "event": "week_end", "week": 2, "reflection": {"went_well": "...", "to_improve": "..."}}
{"timestamp": "2026-01-10T18:00:00Z", "event": "evaluation", "overall_score": 75, "categories": {...}}
```

### Event Types

| Event | When Logged | Fields |
|-------|-------------|--------|
| `journey_start` | Initial setup | level, message |
| `week_start` | Monday | week, month |
| `week_end` | Friday | week, reflection |
| `task_completed` | After tasks | task, duration_hours |
| `mvp_shipped` | After shipping | project, deliverables |
| `evaluation` | After /evaluate | scores, recommendations |

### How Events Are Added

**Automatically** by:
- `pre_week_start.sh` → week_start
- `post_week_review.sh` → week_end
- `evaluate.py` → evaluation

**Manually** by you or Claude:
```
I just finished the EDA notebook. It took 2 hours.
Please log this to my progress.
```

---

## decisions.jsonl

A log of important decisions and adaptations.

### Format

```json
{"timestamp": "2026-01-01T00:00:00Z", "decision": "level_selection", "selected": "Beginner", "rationale": "Starting fresh"}
{"timestamp": "2026-01-15T10:00:00Z", "decision": "project_swap", "from": "sentiment-analysis", "to": "topic-modeling", "rationale": "Better fit"}
{"timestamp": "2026-02-01T09:00:00Z", "decision": "remediation_week", "focus": "pandas", "rationale": "Struggling with groupby"}
```

### Decision Types

| Decision | When Made | Fields |
|----------|-----------|--------|
| `level_selection` | Initial setup | selected, rationale |
| `level_change` | After adaptation | from, to, rationale |
| `month_reorder` | After adaptation | swap (array), rationale |
| `remediation_week` | After adaptation | month, week, focus, rationale |
| `project_swap` | After adaptation | month, from, to, rationale |

### How Decisions Are Added

**By adapt.py** when adaptations are proposed
**By you** when making significant choices

---

## best_practices.md

A living document of accumulated wisdom.

### Format

```markdown
## [Category]

### [Practice Name]
**Context**: When this applies
**Practice**: What to do
**Why**: Why it works
**Added**: Date

### [Another Practice]
...
```

### How to Add Practices

**Using command**:
```
/add-best-practice

I learned that writing tests before implementing helps me catch edge cases early.
This works especially well for data validation functions.
```

**Manually**:
1. Open `.claude/memory/best_practices.md`
2. Add new practice following the template
3. Save

---

## How Memory Affects the System

### Evaluation

`evaluate.py` reads:
- `progress_log.jsonl` - Counts events, checks patterns
- `decisions.jsonl` - Considers past adaptations
- `learner_profile.json` - Gets current level and constraints

### Adaptation

`adapt.py` uses memory to:
- Avoid proposing recent changes again
- Consider learner context
- Make appropriate recommendations

### Reporting

`report.py` generates `tracker.md` from:
- Latest evaluation scores
- Recent progress events
- Decision history

---

## Reviewing Your Memory

### View Progress Log

```bash
# Last 10 entries
tail -10 .claude/memory/progress_log.jsonl

# Count events by type
grep -o '"event": "[^"]*"' .claude/memory/progress_log.jsonl | sort | uniq -c
```

### View Decisions

```bash
cat .claude/memory/decisions.jsonl | python -m json.tool --json-lines
```

### View Profile

```bash
cat .claude/memory/learner_profile.json | python -m json.tool
```

---

## Best Practices for Memory

### Do

- Log progress regularly
- Write honest reflections
- Update profile when circumstances change
- Capture best practices as you learn them

### Don't

- Delete or modify past entries
- Edit `tracker.md` directly (it's regenerated)
- Put secrets in memory files
- Log work-specific confidential information

### Keep It Clean

- Entries should be concise but informative
- Timestamps should be ISO 8601 format
- Categories should be consistent

---

## Troubleshooting

### "Invalid JSON in progress_log.jsonl"

One of the lines has a JSON syntax error. Find it:

```bash
python -c "
import json
with open('.claude/memory/progress_log.jsonl') as f:
    for i, line in enumerate(f, 1):
        try:
            json.loads(line)
        except:
            print(f'Error on line {i}: {line[:50]}...')
"
```

### "Tracker doesn't match my progress"

Regenerate it:
```bash
python .claude/path-engine/report.py
```

### "Lost my progress log"

Unfortunately, if deleted, historical data is gone. Start fresh:
```json
{"timestamp": "2026-01-15T00:00:00Z", "event": "recovery", "message": "Progress log recovered"}
```

## Technical Details

### File Locations

```
.claude/memory/
├── learner_profile.json    # Single JSON object
├── progress_log.jsonl      # Newline-delimited JSON
├── decisions.jsonl         # Newline-delimited JSON
└── best_practices.md       # Markdown
```

### Timestamp Format

Always use ISO 8601 with UTC timezone:
```
2026-01-07T14:30:00Z
```

### Entry Size Limits

Keep entries under 10KB each for performance.
