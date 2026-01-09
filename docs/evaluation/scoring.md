# Scoring System

Detailed mechanics of the evaluation scoring.

## Overview

The scoring system converts signals into category scores, then weights them into an overall score.

## Scoring Formula

```
Overall = Σ (Category_Score × Category_Weight)
```

Where:
- Completion × 0.40
- Quality × 0.25
- Velocity × 0.20
- Reflection × 0.15

## Category Scoring

### Completion Score

**Formula**:
```python
if total_dod > 0:
    completion = (completed_dod / total_dod) * 100
else:
    completion = 50  # Default if no DoD items
```

**Example**:
```
DoD: 4/5 items complete
Completion = (4/5) * 100 = 80%
```

### Quality Score

**Formula**:
```python
if tests_exist:
    base = 70
    bonus = min(30, test_count * 3)
    quality = base + bonus
else:
    quality = 50
```

**Example**:
```
Tests exist: Yes
Test count: 10
Quality = 70 + min(30, 10*3) = 70 + 30 = 100%
```

### Velocity Score

**Formula**:
```python
activity = task_completions + commits

if activity >= 20:
    velocity = 100
elif activity >= 10:
    velocity = 80
elif activity >= 5:
    velocity = 60
else:
    velocity = 40
```

**Example**:
```
Task completions: 8
Commits: 6
Activity = 14
Velocity = 80%
```

### Reflection Score

**Formula**:
```python
journal_count = count_journal_entries()
retro_count = count_week_ends()  # proxy for retros

if journal_count >= 4 and retro_count >= 2:
    reflection = 100
elif journal_count >= 2 or retro_count >= 1:
    reflection = 70
else:
    reflection = 40
```

**Example**:
```
Journal entries: 4
Retrospectives: 2
Reflection = 100%
```

## Overall Calculation

**Formula**:
```python
overall = (
    completion * 0.40 +
    quality * 0.25 +
    velocity * 0.20 +
    reflection * 0.15
)
```

**Example**:
```
Completion: 80 × 0.40 = 32.0
Quality: 100 × 0.25 = 25.0
Velocity: 80 × 0.20 = 16.0
Reflection: 100 × 0.15 = 15.0
Overall = 32.0 + 25.0 + 16.0 + 15.0 = 88.0%
```

## Score Interpretation

| Score Range | Status | Meaning |
|-------------|--------|---------|
| 90-100% | Excellent | Exceeding expectations |
| 80-89% | Strong | Above average |
| 70-79% | Passing | Meeting expectations |
| 60-69% | At Risk | Below threshold |
| 50-59% | Struggling | Needs intervention |
| <50% | Critical | Major issues |

## Thresholds

**Passing Threshold**: 70%

This is configurable in `evaluate.py`:
```python
PASSING_THRESHOLD = 70
```

## Score Caps

Scores are capped at 0-100:
```python
score = max(0, min(100, calculated_score))
```

## Weighted Contributions

At default weights:

| Category | Max Contribution |
|----------|------------------|
| Completion | 40 points |
| Quality | 25 points |
| Velocity | 20 points |
| Reflection | 15 points |
| **Total** | **100 points** |

## Sensitivity Analysis

**Impact of each category**:

| Change | Overall Impact |
|--------|----------------|
| Completion ±10% | ±4 points |
| Quality ±10% | ±2.5 points |
| Velocity ±10% | ±2 points |
| Reflection ±10% | ±1.5 points |

**Example**: Improving Completion from 70% to 80% adds 4 points to overall.

## Memory System Note

**IMPORTANT**: Memory files (`.claude/memory/*`) are append-only sources of truth.

The tracker at `paths/advanced/tracker.md` is a derived artifact that `report.py` may regenerate at any time (with user confirmation).

Don't edit the tracker directly for scoring purposes. Instead:
1. Update memory files (progress_log, etc.)
2. Run `report.py` to regenerate tracker

## Edge Cases

### New Month (No Activity)

Early in a month, most signals are zero:
- Completion: low (few DoD items checked)
- Quality: baseline 50-70
- Velocity: low
- Reflection: depends on journaling

**Recommendation**: Don't over-interpret Week 1 scores.

### End of Year

For Month 12:
- All previous months should be complete
- Overall journey review
- Comprehensive evaluation

### Level Changes

After a level change:
- Scores reset context (new tier scope)
- Previous month scores still valid
- New expectations apply

## Customizing Weights

To change weights:

1. Edit `evaluate.py`:
   ```python
   WEIGHTS = {
       "completion": 0.40,
       "quality": 0.25,
       "velocity": 0.20,
       "reflection": 0.15,
   }
   ```

2. Ensure weights sum to 1.0

3. Log the change:
   ```json
   {"decision": "Changed weights", "rationale": "..."}
   ```

4. Update this documentation

## Running Scoring

```bash
# Full evaluation
python .claude/path-engine/evaluate.py

# JSON output for programmatic use
python .claude/path-engine/evaluate.py --json
```

## Related Docs

- [Rubric](rubric.md) - Category definitions
- [Signals](signals.md) - Data collection
- [Adaptation Rules](adaptation-rules.md) - What happens based on scores
