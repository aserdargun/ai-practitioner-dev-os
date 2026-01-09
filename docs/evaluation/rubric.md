# Evaluation Rubric

How progress is measured in the learning OS.

## Overview

The evaluation system measures four dimensions:
1. **Completion**: Are you finishing what you planned?
2. **Quality**: Is your work well-built?
3. **Velocity**: Are you maintaining momentum?
4. **Learning**: Are you growing and reflecting?

Each dimension is scored 0-100, with an overall weighted score.

---

## Dimensions

### Completion (Weight: 30%)

**What it measures**: Task and deliverable completion relative to plans.

| Score Range | Meaning |
|-------------|---------|
| 0-20 | Barely started, significant tasks incomplete |
| 21-40 | Some progress, but behind schedule |
| 41-60 | Moderate completion, some gaps |
| 61-80 | Good completion, minor gaps |
| 81-100 | Excellent completion, all planned work done |

**Signals**:
- Tasks completed vs. planned
- Weeks completed
- Deliverables shipped
- DoD checklist items checked

---

### Quality (Weight: 25%)

**What it measures**: Observable quality indicators in your work.

| Score Range | Meaning |
|-------------|---------|
| 0-20 | No quality practices evident |
| 21-40 | Minimal testing/docs |
| 41-60 | Basic quality practices |
| 61-80 | Good testing, docs, reviews |
| 81-100 | Excellent quality across the board |

**Signals**:
- Test coverage (when detectable)
- Documentation completeness
- Code review events
- Hardening activities
- Published/demo-ready projects

---

### Velocity (Weight: 25%)

**What it measures**: Rate of progress and momentum trends.

| Score Range | Meaning |
|-------------|---------|
| 0-20 | Very slow, stalled progress |
| 21-40 | Below expected pace |
| 41-60 | Moderate pace |
| 61-80 | Good pace, positive trend |
| 81-100 | Excellent pace, accelerating |

**Signals**:
- Tasks completed per week
- Events logged recently vs. historically
- Blockers encountered and resolved
- Trend direction (improving, stable, declining)

---

### Learning (Weight: 20%)

**What it measures**: Reflection and learning capture.

| Score Range | Meaning |
|-------------|---------|
| 0-20 | No reflection or learning capture |
| 21-40 | Minimal journaling |
| 41-60 | Some retrospectives done |
| 61-80 | Regular reflection, capturing learnings |
| 81-100 | Excellent reflection habits, rich best practices |

**Signals**:
- Retrospectives completed
- Journal entries logged
- Best practices captured
- Learning events documented

---

## Overall Score

The overall score is a weighted average:

```
Overall = (Completion × 0.30) + (Quality × 0.25) +
          (Velocity × 0.25) + (Learning × 0.20)
```

### Interpretation

| Overall Score | Status | Recommended Action |
|---------------|--------|-------------------|
| 0-40 | At Risk | Consider scope reduction or remediation |
| 41-60 | Needs Attention | Review blockers, adjust plan |
| 61-80 | On Track | Continue current approach |
| 81-100 | Exceeding | Consider stretch goals or acceleration |

---

## Target Scores

### Minimum Acceptable
To stay "on track," aim for:
- Completion: 60+
- Quality: 55+
- Velocity: 55+
- Learning: 50+
- Overall: 55+

### Ideal
For strong progress:
- Completion: 75+
- Quality: 70+
- Velocity: 70+
- Learning: 65+
- Overall: 70+

---

## Scoring Frequency

### Weekly
Quick score check to catch issues early:
```
/status
```

### Monthly
Full evaluation for path decisions:
```
/evaluate
python .claude/path-engine/evaluate.py
```

---

## What Affects Scores

### Increases Score
- Completing planned tasks
- Running retrospectives
- Capturing best practices
- Adding tests and documentation
- Publishing/demoing work
- Consistent activity

### Decreases Score
- Incomplete weeks
- Missing retrospectives
- No learning capture
- Gaps in activity
- Unresolved blockers

---

## Score Limitations

### What Scores DON'T Measure
- Code elegance
- Technical depth
- Creativity
- Real-world impact
- External feedback

### Scores Are Signals, Not Judgments
- Low scores mean "needs attention," not "failing"
- Scores help identify areas to focus on
- Your learning journey is more than a number

---

## Gaming Prevention

The system is designed to encourage real progress, not metric gaming:

1. **Multiple dimensions**: Can't just optimize one thing
2. **Trend detection**: Sudden spikes are suspicious
3. **Quality signals**: Not just quantity
4. **Self-reported with evidence**: Claims should match activity

---

## Using Scores

### When Scores Are Low
1. Don't panic — scores fluctuate
2. Identify the lowest dimension
3. Use `/debug-learning` if stuck
4. Consider `/adapt-path` for adjustments

### When Scores Are High
1. Celebrate progress!
2. Consider stretch goals
3. Help others if possible
4. Maintain momentum

---

## Related

- [Signals](signals.md) — What data is used
- [Scoring](scoring.md) — Technical details
- [Adaptation Rules](adaptation-rules.md) — How scores trigger changes
- [Path Engine](../../.claude/path-engine/) — Implementation
