# Evaluation Rubric

How progress is scored in the learning system.

## Overview

Evaluation measures four criteria, equally weighted:

| Criterion | Weight | What It Measures |
|-----------|--------|------------------|
| **Completeness** | 25% | Deliverables present and functional |
| **Quality** | 25% | Code quality, tests, documentation |
| **Learning** | 25% | Evidence of skill acquisition |
| **Reflection** | 25% | Thoughtful retrospectives and journaling |

---

## Scoring Scale

| Score | Assessment | Meaning |
|-------|------------|---------|
| 90-100 | Exceptional | Exceeds expectations significantly |
| 80-89 | Strong | Meets all expectations well |
| 70-79 | Satisfactory | Meets minimum expectations |
| 60-69 | Needs Improvement | Some gaps to address |
| Below 60 | At Risk | Significant intervention needed |

---

## Criteria Details

### Completeness (25%)

**What it measures**: Are the required deliverables present and working?

| Score | Description |
|-------|-------------|
| 90-100 | All deliverables complete with extras |
| 80-89 | All required deliverables complete |
| 70-79 | Core deliverables complete, some gaps |
| 60-69 | Major deliverables incomplete |
| Below 60 | Most deliverables missing |

**Signals evaluated**:
- Milestone events in progress_log
- Week completion events
- DoD checklist items (from month README)
- Code artifacts present

### Quality (25%)

**What it measures**: Is the work well-executed?

| Score | Description |
|-------|-------------|
| 90-100 | Excellent quality, production-ready |
| 80-89 | Good quality, minor improvements possible |
| 70-79 | Acceptable quality, some issues |
| 60-69 | Quality issues need addressing |
| Below 60 | Significant quality problems |

**Signals evaluated**:
- Test coverage and passing tests
- Linting status (ruff clean)
- Documentation completeness
- Error handling
- Code review feedback (if any)

### Learning (25%)

**What it measures**: Did you acquire new skills?

| Score | Description |
|-------|-------------|
| 90-100 | Deep understanding, can teach others |
| 80-89 | Solid understanding, can apply independently |
| 70-79 | Basic understanding, some gaps |
| 60-69 | Surface understanding, significant gaps |
| Below 60 | Minimal learning demonstrated |

**Signals evaluated**:
- Learning events in progress_log
- Experiments conducted
- Best practices added
- Technology decisions made
- Challenges overcome

### Reflection (25%)

**What it measures**: Are you thinking about your learning?

| Score | Description |
|-------|-------------|
| 90-100 | Deep, actionable reflections |
| 80-89 | Thoughtful reflections with insights |
| 70-79 | Regular reflections, some depth |
| 60-69 | Sparse or shallow reflections |
| Below 60 | Missing reflections |

**Signals evaluated**:
- Retrospective events
- Journal entries
- Reflection depth
- Action items from reflections
- Pattern recognition

---

## Evaluation Process

### 1. Data Collection

The evaluator reads:
- `.claude/memory/progress_log.jsonl` — Events
- `.claude/memory/decisions.jsonl` — Decisions
- `.claude/memory/best_practices.md` — Learnings
- Repository state — Code, tests, docs

### 2. Score Computation

Each criterion is scored independently:

```python
completeness_score = evaluate_completeness(progress, repo)
quality_score = evaluate_quality(progress, repo)
learning_score = evaluate_learning(progress, decisions)
reflection_score = evaluate_reflection(progress)

overall = (
    completeness_score * 0.25 +
    quality_score * 0.25 +
    learning_score * 0.25 +
    reflection_score * 0.25
)
```

### 3. Report Generation

Results are presented with:
- Score breakdown
- Evidence for each criterion
- Strengths identified
- Areas for improvement
- Recommendations

### 4. User Validation

**You review and validate the assessment.**

If you disagree with a score:
- Provide additional context
- Point to evidence Claude may have missed
- Request reconsideration

---

## Path Implications

Scores inform path recommendations:

| Pattern | Implication |
|---------|-------------|
| Consistent 90+ | Consider level upgrade |
| Consistent 60-70 | Consider remediation |
| Declining trend | Consider pace adjustment |
| Single low area | Focus improvement there |

See [adaptation-rules.md](adaptation-rules.md) for full rules.

---

## Tips for High Scores

### Completeness
- Check off DoD items explicitly
- Log milestones as you complete them
- Don't skip optional deliverables

### Quality
- Write tests for all features
- Run ruff before committing
- Document your code

### Learning
- Log when you learn something new
- Capture decisions and rationale
- Add best practices

### Reflection
- Journal weekly
- Do retrospectives honestly
- Connect learnings to actions

---

## Related Documentation

- [signals.md](signals.md) — Input signals for evaluation
- [scoring.md](scoring.md) — Score computation details
- [adaptation-rules.md](adaptation-rules.md) — How scores affect path
- [../.claude/path-engine/evaluate.py](../../.claude/path-engine/evaluate.py) — Evaluation script
