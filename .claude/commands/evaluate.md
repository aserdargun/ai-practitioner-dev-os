# Command: /evaluate

## Purpose

Assess your deliverables against the evaluation rubric and get a performance report.

## Inputs

Optional context:
- Specific deliverables to evaluate
- Self-assessment to include

The command reads from:
- Your completed work
- `.claude/memory/progress_log.jsonl`
- `docs/evaluation/rubric.md`
- `docs/evaluation/signals.md`
- Current month's Definition of Done

## Outputs

- Score breakdown by criterion
- Evidence citations
- Strengths identified
- Areas for improvement
- Recommendations

**Note**: Evaluation is presented for your validation.

## When to Use

- End of each week
- End of each month
- After completing major deliverables
- When considering path adaptation

## Agent Routing

**Primary**: Evaluator Agent

The Evaluator assesses your work against objective criteria and provides a detailed report.

## Example Usage

```
/evaluate
```

Or with scope:

```
/evaluate

Evaluate my Month 3 project. I completed the RAG service
and wrote tests but didn't finish the documentation.
```

## Output Format

```markdown
## Evaluation Report — Month X, Week Y

### Overall Score: [X/100]

### Scores by Criterion

| Criterion | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Completeness | 80/100 | 25% | 20 |
| Quality | 75/100 | 25% | 18.75 |
| Learning | 85/100 | 25% | 21.25 |
| Reflection | 70/100 | 25% | 17.5 |
| **Total** | | | **77.5** |

### Evidence

#### Completeness (80/100)
- ✅ Core functionality implemented
- ✅ Tests present
- ⚠️ Documentation incomplete
- Evidence: [links to files]

#### Quality (75/100)
- ✅ Tests passing
- ✅ ruff clean
- ⚠️ Some error handling missing
- Evidence: [specific observations]

#### Learning (85/100)
- ✅ New skills demonstrated
- ✅ Applied curriculum concepts
- Evidence: [what was learned]

#### Reflection (70/100)
- ✅ Weekly retros completed
- ⚠️ Journal entries sparse
- Evidence: [journal/log entries]

### Strengths
- [Strength 1]
- [Strength 2]

### Areas for Improvement
- [Area 1]: [specific suggestion]
- [Area 2]: [specific suggestion]

### Recommendations
1. [Recommendation]
2. [Recommendation]

### Path Implications
Based on this evaluation:
- Current level appropriate: [yes/no]
- Adaptation suggested: [if applicable]

---
**Validate this evaluation?** (yes/no/discuss)
```

## Scoring Reference

From `docs/evaluation/rubric.md`:

| Score Range | Meaning |
|-------------|---------|
| 90-100 | Exceptional |
| 80-89 | Strong |
| 70-79 | Satisfactory |
| 60-69 | Needs Improvement |
| Below 60 | At Risk |

## Integration with Path Engine

This command wraps `.claude/path-engine/evaluate.py`:
```bash
python .claude/path-engine/evaluate.py
```

Results inform `/adapt-path` recommendations.
