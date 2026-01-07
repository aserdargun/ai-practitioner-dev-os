# Evaluation Rubric

This document defines how progress is evaluated in the AI Practitioner Learning OS.

## Overview

The evaluation system scores your progress across four categories, then combines them into an overall score (0-100).

## Categories

### 1. Completion (30% weight)

Measures what you've delivered.

| Score | Description |
|-------|-------------|
| 90-100 | 5+ tasks completed, MVPs shipped, ahead of schedule |
| 70-89 | 3-4 tasks completed, on track with deliverables |
| 50-69 | 1-2 tasks completed, behind but progressing |
| Below 50 | No tasks completed, significantly behind |

**Signals**:
- `task_completed` events in progress log
- `mvp_shipped` events in progress log
- Deliverables mentioned in reflections

### 2. Quality (25% weight)

Measures how well you're building.

| Score | Description |
|-------|-------------|
| 90-100 | Tests written, code reviewed, well-documented |
| 70-89 | Some tests, documentation present |
| 50-69 | Basic functionality works, minimal tests |
| Below 50 | Code works but no tests or docs |

**Signals**:
- Mentions of "test" in progress events
- `code_reviewed` events
- Documentation updates mentioned
- Mentions of "README", "docs", "docstring"

### 3. Understanding (25% weight)

Measures depth of learning.

| Score | Description |
|-------|-------------|
| 90-100 | Regular reflections, decisions documented, clear explanations |
| 70-89 | Weekly reflections done, some decisions documented |
| 50-69 | Occasional reflections, few decisions documented |
| Below 50 | No reflections, no documented decisions |

**Signals**:
- Reflection content in week_end events
- Entries in decisions.jsonl
- "learned" mentions in progress log
- Best practices added

### 4. Consistency (20% weight)

Measures habit formation and regular progress.

| Score | Description |
|-------|-------------|
| 90-100 | Active 5+ days/week, following week structure |
| 70-89 | Active 3-4 days/week, mostly following structure |
| 50-69 | Active 2 days/week, inconsistent structure |
| Below 50 | Active <2 days/week, no structure |

**Signals**:
- Days with logged events
- week_start and week_end events present
- Regular timestamps in progress log
- Following Monday start / Friday end pattern

## Overall Score Calculation

```
overall = completion × 0.30
        + quality × 0.25
        + understanding × 0.25
        + consistency × 0.20
```

## Score Interpretation

| Score Range | Status | Recommendation |
|-------------|--------|----------------|
| 90-100 | Excellent | Consider acceleration/upgrade |
| 70-89 | On Track | Continue as planned |
| 50-69 | Struggling | Consider remediation |
| Below 50 | At Risk | Remediation recommended |

## Thresholds

| Threshold | Value | Triggers |
|-----------|-------|----------|
| Accelerate | 90+ | Level upgrade consideration |
| Remediate | <60 | Remediation week proposal |
| At Risk | <50 | Urgent intervention |

## Example Evaluation

```
Evaluation Results:
==================
Level: Beginner
Overall Score: 72/100

Category Scores:
  completion      [████████░░] 80
  quality         [███████░░░] 70
  understanding   [███████░░░] 65
  consistency     [████████░░] 75

Calculation:
  80 × 0.30 = 24
  70 × 0.25 = 17.5
  65 × 0.25 = 16.25
  75 × 0.20 = 15
  Total: 72.75 → 72

Status: On Track
```

## Improving Your Score

### To improve Completion:
- Break work into smaller tasks
- Log task completions as you go
- Aim for 3-5 tasks per week

### To improve Quality:
- Write at least one test per feature
- Add docstrings to functions
- Request code review

### To improve Understanding:
- Complete weekly retros
- Document decisions when you make them
- Note what you learned

### To improve Consistency:
- Set specific learning times
- Use `/start-week` on Mondays
- Use `/retro` on Fridays

## Related Documentation

- [Signals](signals.md) - Detailed signal definitions
- [Scoring](scoring.md) - Technical scoring details
- [Adaptation Rules](adaptation-rules.md) - What happens based on scores
- [Path Engine](../../.claude/path-engine/README.md) - Implementation details
