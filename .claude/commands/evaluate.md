# Command: /evaluate

## Purpose

Assess progress and compute formal scores based on the rubric. This provides an objective measurement of your learning progress.

## Inputs

- Memory files (`.claude/memory/*`)
- Month DoD criteria
- Repo signals (commits, tests, docs)
- Rubric (`.claude/../docs/evaluation/rubric.md`)

## Outputs

- Evaluation report with category scores
- Overall score and threshold status
- Trend analysis
- Adaptation suggestions (if below threshold)
- **All assessments are for user review, not automatic action**

## When to Use

- End of each month (required)
- Mid-month check-in (optional)
- When unsure if you're on track
- Before requesting path changes

## Agent Routing

**Primary**: Evaluator Agent

The Evaluator computes scores using defined signals and presents analysis.

## Example Usage

**User Input**:
```
/evaluate
```

**Expected Output**:
```
## Evaluation Report: Month 03

### Scoring Summary

| Category | Weight | Score | Weighted |
|----------|--------|-------|----------|
| Completion | 40% | 85% | 34.0 |
| Quality | 25% | 90% | 22.5 |
| Velocity | 20% | 70% | 14.0 |
| Reflection | 15% | 95% | 14.3 |
| **Total** | 100% | | **84.8** |

**Threshold**: 70%
**Status**: ✅ PASSING

---

### Category Breakdown

#### Completion (85%)
- 4/5 DoD items complete
- Missing: Blog post (in progress)
- Bonus: Extra tests added

#### Quality (90%)
- All tests passing
- Code review: 0 critical, 2 suggestions
- Documentation complete

#### Velocity (70%)
- Planned: 20 tasks
- Completed: 14 tasks
- Note: Chunking research took longer than expected

#### Reflection (95%)
- 4/4 weekly journal entries
- 2 retrospectives completed
- 3 best practices added

---

### Trend Analysis

| Month | Score | Trend |
|-------|-------|-------|
| 01 | 78% | - |
| 02 | 82% | ↑ |
| 03 | 85% | ↑ |

**Observation**: Consistent improvement. Quality scores are strong.
Velocity could improve with better upfront research.

---

### Signals Used

```
commits_this_month: 12
tests_added: 7
tests_passing: 12/12
docs_updated: 4 files
journal_entries: 4
retros_completed: 2
blockers_logged: 2
blockers_resolved: 2
```

---

### Adaptation Suggestions

Score is above threshold, no mandatory adaptations.

**Optional suggestions**:
1. Consider front-loading research in Month 04
2. Blog post completion could carry over

**Run `/adapt-path` to see formal adaptation proposals.**
```

## Scoring Rubric Reference

See `docs/evaluation/rubric.md` for:
- Full category definitions
- Signal sources
- Threshold explanations
- Edge cases

## Related Commands

- `/adapt-path` - Act on evaluation results
- `/retro` - Reflect (different from evaluate)
- `/status` - Quick progress check
