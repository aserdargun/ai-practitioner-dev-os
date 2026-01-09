# Command: /evaluate

## Purpose
Get detailed evaluation scores against the learning rubric, including progress by dimension, gap analysis, and trend indicators.

## Inputs
- **Period** (optional): Month or week to evaluate
- **Focus** (optional): Specific dimension to deep-dive

## Outputs
- **Scores by Dimension**: Completion, Quality, Velocity, Learning
- **Gap Analysis**: Where you're behind expectations
- **Trend Indicators**: Improving, stable, or declining
- **Rubric Comparison**: How you compare to expectations
- **Recommendations**: Suggested focus areas

## When to Use
- End of each week or month
- When feeling uncertain about progress
- Before making path adaptation decisions
- When preparing for a check-in

## Agent Routing
**Evaluator** — reads memory and repo signals to compute scores

## Example Usage

### Full Evaluation
```
/evaluate
```

### Month Evaluation
```
/evaluate Month 3
```

### Dimension Focus
```
/evaluate
Focus on the Quality dimension
```

## Sample Output

```
📊 EVALUATION REPORT — Month 3

Overall Score: 67/100 (On Track)

Dimension Breakdown:
┌─────────────┬───────┬─────────┬───────────────┐
│ Dimension   │ Score │ Target  │ Status        │
├─────────────┼───────┼─────────┼───────────────┤
│ Completion  │ 72    │ 70      │ ✓ On track    │
│ Quality     │ 58    │ 70      │ ⚠ Below       │
│ Velocity    │ 75    │ 65      │ ✓ Exceeding   │
│ Learning    │ 63    │ 70      │ → Approaching │
└─────────────┴───────┴─────────┴───────────────┘

Trends (Last 4 Weeks):
- Completion: ↗ Improving (+8)
- Quality: → Stable
- Velocity: ↗ Improving (+12)
- Learning: ↘ Declining (-5)

Gap Analysis:
1. Quality (Gap: 12 points)
   - Test coverage at 45% (target: 70%)
   - Documentation incomplete for 3 modules
   - 2 code review issues unresolved

2. Learning (Gap: 7 points)
   - Only 2 journal entries this month (target: 4)
   - No best practices captured recently
   - Retros skipped last 2 weeks

Strengths:
✓ Consistently completing tasks on time
✓ Good velocity — shipping faster than expected
✓ Blockers resolved quickly

Focus Recommendations:
1. Add tests to bring coverage to 70%
2. Complete pending documentation
3. Resume weekly retros and journaling

Run /adapt-path to see if any path changes are recommended.
```

## Scoring Details

### Completion (0-100)
- Tasks done vs. planned
- Deliverables shipped
- DoD items checked

### Quality (0-100)
- Test coverage
- Documentation completeness
- Code review feedback

### Velocity (0-100)
- Tasks per week trend
- Time to complete tasks
- Blocker resolution speed

### Learning (0-100)
- Journal entries
- Best practices captured
- Retros completed
- New skills demonstrated

## Related Commands
- `/status` — Quick progress check
- `/adapt-path` — See path recommendations
- `/retro` — Reflect and improve
