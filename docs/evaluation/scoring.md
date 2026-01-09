# Scoring System

How evaluation scores are computed.

## Overview

The scoring system transforms signals into a weighted overall score.

```
Signals → Criterion Scores → Weighted Average → Overall Score
```

---

## Score Computation

### Formula

```
Overall = (Completeness × 0.25) +
          (Quality × 0.25) +
          (Learning × 0.25) +
          (Reflection × 0.25)
```

### Example

```
Completeness:  80 × 0.25 = 20.0
Quality:       75 × 0.25 = 18.75
Learning:      85 × 0.25 = 21.25
Reflection:    70 × 0.25 = 17.5
─────────────────────────────────
Overall:               = 77.5
```

---

## Criterion Scoring

### Completeness

Based on milestones and week completions:

| Milestones | Weeks | Score |
|------------|-------|-------|
| 4+ | 4 | 95 |
| 2-3 | 2-3 | 80 |
| 1 | 1 | 65 |
| 0 | 0 | 40 |

### Quality

Based on quality events:

```
Score = 50 + (reviews × 10) + (tests × 15) + (deployments × 20)
Max: 100
```

### Learning

Based on learning evidence:

```
Score = 50 + (learnings × 10) + (experiments × 8) +
        (best_practices × 12) + (decisions × 5)
Max: 100
```

### Reflection

Based on reflection activities:

```
Score = 40 + (retros × 15) + (journals × 10) + (reflections × 8)
Max: 100
```

---

## Time Windows

### Weekly Evaluation

- Looks at last 7 days of activity
- Good for progress check-ins
- Use: `/evaluate` during the week

### Monthly Evaluation

- Looks at last 30 days of activity
- Good for milestone assessment
- Use: End of month evaluation

### Trend Analysis

- Compares recent (7 days) to historical (90 days)
- Identifies patterns: improving, stable, declining
- Used by adapt.py for recommendations

---

## Score Interpretation

### Assessment Levels

| Overall | Assessment | Action |
|---------|------------|--------|
| 90-100 | Exceptional | Consider acceleration |
| 80-89 | Strong | On track, continue |
| 70-79 | Satisfactory | Minor adjustments |
| 60-69 | Needs Improvement | Focus on weak areas |
| Below 60 | At Risk | Consider remediation |

### Trend Analysis

| Pattern | Meaning | Recommendation |
|---------|---------|----------------|
| Improving | Scores rising | Continue, consider upgrade |
| Stable | Consistent scores | On track |
| Declining | Scores falling | Investigate, adjust |

---

## Memory and Scoring

**Important**: Memory files in `.claude/memory/` are the **source of truth**.

The file `paths/intermediate/tracker.md` is a **derived artifact** that `report.py` may regenerate at any time.

### Implications

- If tracker.md is outdated, regenerate with `report.py`
- To fix scores, fix the memory entries
- Tracker reflects memory, not the other way around

---

## Validation

### User Review

All evaluations are presented for your validation:

```
=== EVALUATION REPORT ===

Overall Score: 77.5
Assessment: Satisfactory

Scores by Criterion:
- Completeness: 80
- Quality: 75
- Learning: 85
- Reflection: 70

Evidence:
- Completeness: 2 milestones, 3 weeks completed
- Quality: 1 review, 2 test runs
- Learning: 3 learnings, 2 experiments
- Reflection: 2 retros, 3 journal entries

─────────────────────────────
Validate this evaluation? (yes/no/discuss)
```

### Disputing Scores

If you disagree:

1. **Provide context**: "I also completed X which wasn't logged"
2. **Add missing events**: Log the missing activity
3. **Re-evaluate**: Run evaluation again

---

## Running Evaluation

### Command Line

```bash
# Full evaluation
python .claude/path-engine/evaluate.py

# Specific month
python .claude/path-engine/evaluate.py --month 3

# JSON output
python .claude/path-engine/evaluate.py --json
```

### Via Claude

```
/evaluate

Evaluate my Month 3 deliverables.
```

---

## Score Impact

### On Adaptation

Scores inform adapt.py proposals:

| Score Pattern | Possible Proposal |
|---------------|-------------------|
| 90+ sustained | Level upgrade |
| Below 60 sustained | Level downgrade |
| Single criterion low | Targeted remediation |
| Declining trend | Pace adjustment |

### On Reporting

Scores appear in tracker.md:

```markdown
### Latest Evaluation
- Date: 2026-03-15
- Overall: 77.5
- Assessment: Satisfactory
```

---

## Related Documentation

- [rubric.md](rubric.md) — Scoring criteria
- [signals.md](signals.md) — Input signals
- [adaptation-rules.md](adaptation-rules.md) — How scores affect path
- [../.claude/path-engine/evaluate.py](../../.claude/path-engine/evaluate.py) — Implementation
