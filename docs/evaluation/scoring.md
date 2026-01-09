# Scoring Details

Technical details of how evaluation scores are calculated.

## Overview

Scoring is implemented in `.claude/path-engine/evaluate.py`:
- Python stdlib only (no external dependencies)
- Deterministic (same input → same output)
- Transparent (can trace any score)

---

## Score Calculation

### Overall Formula

```python
overall = (
    completion_score * 0.30 +
    quality_score * 0.25 +
    velocity_score * 0.25 +
    learning_score * 0.20
)
```

---

## Completion Score

### Formula
```python
def evaluate_completion(progress, profile):
    completed_tasks = count_events(progress, "task_completed")
    completed_weeks = count_events(progress, "week_completed")
    recent_tasks = count_recent_events(progress, "task_completed", days=30)

    # Component scores
    task_score = min(completed_tasks * 5, 50)      # Up to 50 pts
    week_score = min(completed_weeks * 10, 30)    # Up to 30 pts
    recency_score = min(recent_tasks * 2, 20)     # Up to 20 pts

    return min(task_score + week_score + recency_score, 100)
```

### Components
| Component | Max Points | Per Unit |
|-----------|------------|----------|
| Tasks completed | 50 | 5 per task |
| Weeks completed | 30 | 10 per week |
| Recent activity | 20 | 2 per recent task |

---

## Quality Score

### Formula
```python
def evaluate_quality(progress, profile):
    hardening = count_events_containing(progress, "harden")
    reviews = count_events_containing(progress, "review")
    publishes = count_events_containing(progress, "publish")

    # Start at baseline
    base_score = 50

    # Add bonuses
    hardening_bonus = min(hardening * 10, 20)
    review_bonus = min(reviews * 5, 15)
    publish_bonus = min(publishes * 15, 30)

    return min(base_score + hardening_bonus + review_bonus + publish_bonus, 100)
```

### Components
| Component | Max Bonus | Per Unit |
|-----------|-----------|----------|
| Baseline | 50 | - |
| Hardening events | 20 | 10 each |
| Review events | 15 | 5 each |
| Publish events | 30 | 15 each |

---

## Velocity Score

### Formula
```python
def evaluate_velocity(progress, profile):
    recent = get_events(progress, last_14_days)
    older = get_events(progress, days_14_to_28)

    recent_count = len(recent)
    older_count = len(older) - recent_count

    # Calculate trend
    if older_count > 0:
        trend = (recent_count - older_count) / older_count
    else:
        trend = 0 if recent_count == 0 else 1

    # Score components
    activity_score = min(recent_count * 5, 60)
    trend_score = 20 + int(trend * 20)  # -20 to +40
    trend_score = max(0, min(40, trend_score))

    return min(activity_score + trend_score, 100)
```

### Components
| Component | Max Points | Calculation |
|-----------|------------|-------------|
| Recent activity | 60 | 5 per event (14 days) |
| Trend bonus | 40 | Based on 2-week comparison |

### Trend Interpretation
| Trend Value | Direction | Score Impact |
|-------------|-----------|--------------|
| > 0.1 | Improving | +10 to +20 |
| -0.1 to 0.1 | Stable | 0 |
| < -0.1 | Declining | -10 to -20 |

---

## Learning Score

### Formula
```python
def evaluate_learning(progress, best_practices_count, profile):
    retros = count_events_containing(progress, "retro")
    journals = count_events_containing(progress, "journal", "reflection")

    # Score components
    retro_score = min(retros * 15, 30)
    journal_score = min(journals * 10, 30)
    practice_score = min(best_practices_count * 5, 40)

    return min(retro_score + journal_score + practice_score, 100)
```

### Components
| Component | Max Points | Per Unit |
|-----------|------------|----------|
| Retros completed | 30 | 15 each |
| Journal entries | 30 | 10 each |
| Best practices | 40 | 5 each |

---

## Score Bounds

All scores are bounded:
- Minimum: 0
- Maximum: 100

```python
score = max(0, min(score, 100))
```

---

## Data Sources

### What Gets Read
```python
# Memory files
progress = load_jsonl(".claude/memory/progress_log.jsonl")
profile = load_json(".claude/memory/learner_profile.json")
decisions = load_jsonl(".claude/memory/decisions.jsonl")

# Best practices (count headers)
best_practices_count = count_markdown_headers(".claude/memory/best_practices.md")
```

### Event Counting
```python
def count_events(progress, event_type):
    return sum(1 for e in progress if e.get("event") == event_type)

def count_events_containing(progress, *keywords):
    return sum(1 for e in progress
               if any(kw in e.get("event", "").lower() for kw in keywords))
```

---

## Running Evaluation

### Command Line
```bash
# Human-readable output
python .claude/path-engine/evaluate.py

# JSON output
python .claude/path-engine/evaluate.py --json

# Specific month
python .claude/path-engine/evaluate.py --month 3
```

### Via Claude
```
/evaluate
```

---

## Output Format

### Human-Readable
```
OVERALL SCORE: 67/100 (On Track)

DIMENSION SCORES
------------------------------------------------
Completion   ████████████░░░░░░░░  72/100 ✓
Quality      ███████████░░░░░░░░░  58/100 ⚠
Velocity     ███████████████░░░░░  75/100 ✓
Learning     ████████████░░░░░░░░  63/100 →
```

### JSON
```json
{
  "timestamp": "2026-03-15T10:00:00",
  "overall_score": 67,
  "dimensions": {
    "completion": {"score": 72, "explanation": "..."},
    "quality": {"score": 58, "explanation": "..."},
    "velocity": {"score": 75, "trend_direction": "improving"},
    "learning": {"score": 63, "explanation": "..."}
  }
}
```

---

## Important Notes

### Memory is Source of Truth
`paths/beginner/tracker.md` is a **derived artifact**. It can be regenerated from memory files at any time using `report.py`.

**Do not rely on tracker.md for scoring** — it's for human reading.

### Reproducibility
Given the same memory files, `evaluate.py` produces identical scores.

### No External Dependencies
The path engine uses Python stdlib only:
- `json` for parsing
- `datetime` for time calculations
- `pathlib` for file paths

---

## Related

- [Rubric](rubric.md) — Score interpretation
- [Signals](signals.md) — What data is used
- [Adaptation Rules](adaptation-rules.md) — How scores trigger changes
- [evaluate.py](../../.claude/path-engine/evaluate.py) — Implementation
