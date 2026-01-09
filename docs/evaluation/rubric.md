# Evaluation Rubric

How progress is measured in the learning OS.

## Overview

The evaluation system uses four categories to assess your learning progress. Each category has defined signals and weights.

## Scoring Categories

| Category | Weight | Focus |
|----------|--------|-------|
| Completion | 40% | DoD items, deliverables |
| Quality | 25% | Tests, code review |
| Velocity | 20% | Tasks completed vs planned |
| Reflection | 15% | Journals, retrospectives |

## Category Details

### Completion (40%)

**What it measures**: How much of the defined work is done.

**Signals**:
- DoD checklist items completed
- Deliverables present in repo
- Month milestones achieved

**Scoring**:
| Completion % | Score |
|--------------|-------|
| 90-100% | 100 |
| 70-89% | 80 |
| 50-69% | 60 |
| 30-49% | 40 |
| <30% | 20 |

**Example**:
- Month DoD has 5 items
- 4 items checked
- Completion = 80%
- Score = 80

### Quality (25%)

**What it measures**: How well the work meets standards.

**Signals**:
- Tests exist and pass
- Code review feedback (via `/harden`)
- Documentation completeness
- Security issues (none = better)

**Scoring**:
| Condition | Score |
|-----------|-------|
| All tests pass + good review | 90-100 |
| Tests pass, minor issues | 70-89 |
| Some tests fail or missing | 50-69 |
| No tests or critical issues | <50 |

**Example**:
- 10 tests, all passing
- Code review: 0 critical, 2 minor
- Docs complete
- Quality = 90

### Velocity (20%)

**What it measures**: How well you're tracking to plan.

**Signals**:
- Tasks completed vs planned
- Progress log activity
- Git commit frequency
- Blockers logged and resolved

**Scoring**:
| Tasks/Activity | Score |
|----------------|-------|
| On or ahead of plan | 90-100 |
| 1-2 tasks behind | 70-89 |
| 3+ tasks behind | 50-69 |
| Significantly behind | <50 |

**Example**:
- Planned 10 tasks
- Completed 8
- Velocity = 80

### Reflection (15%)

**What it measures**: How actively you're reflecting and learning.

**Signals**:
- Weekly journal entries
- Retrospectives completed
- Best practices added
- Coach interactions logged

**Scoring**:
| Reflection Activity | Score |
|---------------------|-------|
| Weekly entries + retros | 90-100 |
| Some entries, some retros | 70-89 |
| Sparse entries | 50-69 |
| No reflection activity | <50 |

**Example**:
- 4 journal entries (weekly)
- 2 retrospectives
- 3 best practices added
- Reflection = 95

## Overall Score Calculation

```
Overall = (Completion × 0.40) + (Quality × 0.25) + (Velocity × 0.20) + (Reflection × 0.15)
```

**Example**:
- Completion: 80 × 0.40 = 32.0
- Quality: 90 × 0.25 = 22.5
- Velocity: 80 × 0.20 = 16.0
- Reflection: 95 × 0.15 = 14.25
- **Overall: 84.75%**

## Thresholds

| Overall Score | Status | Action |
|---------------|--------|--------|
| ≥85% | Excellent | Consider acceleration |
| 70-84% | Passing | Continue as planned |
| 55-69% | Needs Attention | Consider remediation |
| <55% | Struggling | Level change or major adaptation |

The default passing threshold is **70%**.

## Running Evaluation

```bash
# Run evaluation
python .claude/path-engine/evaluate.py

# Evaluate specific month
python .claude/path-engine/evaluate.py --month 3

# Get JSON output
python .claude/path-engine/evaluate.py --json
```

## Interpreting Results

### High Scores (≥85%)

- You're ahead of pace
- Consider stretch goals
- May be ready for acceleration

### Passing (70-84%)

- On track
- Continue current approach
- Minor adjustments if desired

### Needs Attention (55-69%)

- Below threshold
- Review blockers
- Consider remediation week
- May need plan adjustment

### Struggling (<55%)

- Significant issues
- Consider level change
- Review constraints
- May need major adaptation

## Edge Cases

### No DoD Items Found

If the month README has no checkable items:
- Completion defaults to 50%
- Add DoD items to month README

### No Tests

If no test files exist:
- Quality defaults to 50%
- Add tests before next evaluation

### No Progress Log Entries

If progress log is empty:
- Velocity defaults to 40%
- Use hooks to log consistently

### New Month (Week 1)

Early in a month:
- Scores may be artificially low
- Wait until Week 2-3 for meaningful evaluation

## Customizing the Rubric

The rubric is defined in:
- `evaluate.py` → scoring logic
- This file → documentation

To adjust:
1. Modify weights in `evaluate.py`
2. Update this documentation
3. Note the change in decisions.jsonl

## Related Docs

- [Signals](signals.md) - How signals are collected
- [Scoring](scoring.md) - Detailed scoring mechanics
- [Adaptation Rules](adaptation-rules.md) - What happens based on scores
- [Path Engine](../../.claude/path-engine/README.md) - Technical implementation
