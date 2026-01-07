# Scoring Details

This document explains the technical details of how scores are calculated.

## Score Calculation

### Overall Formula

```
overall_score = Σ (category_score × category_weight)
```

Where:
- `category_score` is 0-100 for each category
- `category_weight` is the percentage weight

### Category Weights

| Category | Weight | Rationale |
|----------|--------|-----------|
| Completion | 0.30 | Delivery matters most |
| Quality | 0.25 | Good habits are important |
| Understanding | 0.25 | Deep learning is the goal |
| Consistency | 0.20 | Habits compound over time |

### Example Calculation

```python
scores = {
    "completion": 80,
    "quality": 70,
    "understanding": 65,
    "consistency": 75
}

weights = {
    "completion": 0.30,
    "quality": 0.25,
    "understanding": 0.25,
    "consistency": 0.20
}

overall = sum(scores[cat] * weights[cat] for cat in scores)
# = 80*0.30 + 70*0.25 + 65*0.25 + 75*0.20
# = 24 + 17.5 + 16.25 + 15
# = 72.75 → 72 (rounded)
```

## Category Score Formulas

### Completion Score

```python
def score_completion(events, days=7):
    recent = filter_recent(events, days)
    tasks = count_event(recent, "task_completed")
    mvps = count_event(recent, "mvp_shipped")

    # Base score from tasks
    if tasks >= 5:
        base = 100
    elif tasks >= 3:
        base = 80
    elif tasks >= 1:
        base = 60
    else:
        base = 30

    # Bonus for MVPs (capped at 100)
    bonus = mvps * 10
    return min(100, base + bonus)
```

### Quality Score

```python
def score_quality(events, days=14):
    recent = filter_recent(events, days)

    score = 50  # Base score

    # Test signals (+20)
    if has_keyword(recent, "test"):
        score += 20

    # Review signals (+15)
    if has_event(recent, "code_reviewed"):
        score += 15

    # Documentation signals (+15)
    if has_keyword(recent, ["doc", "readme"]):
        score += 15

    return min(100, score)
```

### Understanding Score

```python
def score_understanding(progress, decisions, days=14):
    recent_progress = filter_recent(progress, days)
    recent_decisions = filter_recent(decisions, days)

    score = 50  # Base score

    # Reflection signals (+25)
    if any(e.get("reflection") for e in recent_progress):
        score += 25

    # Decision signals (+15)
    if len(recent_decisions) > 0:
        score += 15

    # Learning mentions (+10)
    if has_keyword(recent_progress, "learn"):
        score += 10

    return min(100, score)
```

### Consistency Score

```python
def score_consistency(events, profile, days=14):
    active_days = count_active_days(events, days)
    has_structure = has_week_structure(events)

    score = 50  # Base score

    # Active days bonus
    if active_days >= 8:  # 4+/week for 2 weeks
        score += 30
    elif active_days >= 4:  # 2+/week
        score += 15

    # Structure bonus
    if has_structure:
        score += 20

    return min(100, score)
```

## Derived Metrics

### Trend Analysis

```python
def calculate_trend(scores_history, window=4):
    """Calculate score trend over last N evaluations."""
    if len(scores_history) < 2:
        return "stable"

    recent = scores_history[-window:]
    first_half = sum(recent[:len(recent)//2]) / (len(recent)//2)
    second_half = sum(recent[len(recent)//2:]) / (len(recent) - len(recent)//2)

    diff = second_half - first_half
    if diff > 5:
        return "improving"
    elif diff < -5:
        return "declining"
    return "stable"
```

### Velocity

```python
def calculate_velocity(events, days=7):
    """Calculate tasks per day."""
    recent = filter_recent(events, days)
    tasks = count_event(recent, "task_completed")
    return tasks / days
```

## Score Boundaries

All scores are bounded:

```python
def bound_score(score):
    return max(0, min(100, int(score)))
```

## Important Notes

### Memory Files as Source of Truth

**IMPORTANT**: Memory files (`.claude/memory/*`) are append-only sources of truth.

The tracker at `paths/Beginner/tracker.md` is a **derived artifact** that `report.py` may overwrite/regenerate at any time.

Never edit the tracker directly - it will be overwritten. Instead:
1. Update memory files
2. Run `report.py` to regenerate tracker

### Timestamp Requirements

All events should have timestamps for accurate scoring:

```json
{"timestamp": "2026-01-07T14:00:00Z", "event": "task_completed", "task": "EDA"}
```

Events without timestamps may be:
- Excluded from recent filters
- Given reduced weight
- Flagged as low quality

### Score Persistence

Evaluation scores are logged to progress_log.jsonl:

```json
{
  "timestamp": "2026-01-10T18:00:00Z",
  "event": "evaluation",
  "overall_score": 72,
  "categories": {
    "completion": 80,
    "quality": 70,
    "understanding": 65,
    "consistency": 75
  }
}
```

This creates a history of scores for trend analysis.

## Implementation

The scoring logic is implemented in:
- `.claude/path-engine/evaluate.py`

To run evaluation:
```bash
python .claude/path-engine/evaluate.py
```

## Related Documentation

- [Rubric](rubric.md) - Scoring framework
- [Signals](signals.md) - Input signals
- [Adaptation Rules](adaptation-rules.md) - What scores trigger
