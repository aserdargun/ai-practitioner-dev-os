# Evaluation Rubric

How your progress is measured and scored.

---

## Overview

The evaluation system scores your progress across five dimensions, each with specific signals and weights. The overall score determines your status and triggers potential adaptations.

---

## Scoring Dimensions

### 1. Completion (30%)

**What It Measures**: Task completion rate

**Signals**:
- Tasks marked completed in progress log
- Deliverables shipped
- Monthly objectives met

**Scoring**:
| Score | Criteria |
|-------|----------|
| 100% | All planned tasks completed |
| 80% | Most tasks completed, minor items remaining |
| 60% | Core tasks done, some objectives missed |
| 40% | Less than half completed |
| 20% | Minimal progress |
| 0% | No tasks completed |

**How to Improve**:
- Break large tasks into smaller, completable items
- Focus on finishing before starting new tasks
- Log completions as they happen

---

### 2. Quality (25%)

**What It Measures**: Code quality and test coverage

**Signals**:
- Test pass rate (pytest results)
- Linting pass rate (ruff results)
- Code review feedback
- Documentation completeness

**Scoring**:
| Score | Criteria |
|-------|----------|
| 100% | All tests pass, no lint errors, docs complete |
| 80% | Tests pass, minor lint issues, good docs |
| 60% | Most tests pass, some lint issues |
| 40% | Many test failures or major issues |
| 20% | Significant quality problems |
| 0% | No tests or mostly failing |

**How to Improve**:
- Write tests as you code
- Run linting before commits
- Use `/harden` command regularly
- Document as you build

---

### 3. Consistency (20%)

**What It Measures**: Regular engagement and activity

**Signals**:
- Commit frequency
- Progress log entry frequency
- Daily/weekly engagement patterns

**Scoring**:
| Score | Criteria |
|-------|----------|
| 100% | Daily commits, frequent log entries |
| 80% | Regular commits (4-5 days/week) |
| 60% | Moderate activity (3-4 days/week) |
| 40% | Sporadic activity (1-2 days/week) |
| 20% | Very irregular |
| 0% | No recent activity |

**How to Improve**:
- Commit small changes frequently
- Log progress daily
- Establish a routine

---

### 4. Growth (15%)

**What It Measures**: Learning and skill development

**Signals**:
- Best practices captured
- Skills applied from previous months
- Complexity of work over time

**Scoring**:
| Score | Criteria |
|-------|----------|
| 100% | Many best practices, clear skill growth |
| 80% | Regular learnings captured |
| 60% | Some best practices recorded |
| 40% | Few learnings captured |
| 20% | Minimal evidence of growth |
| 0% | No best practices recorded |

**How to Improve**:
- Use `/add-best-practice` after each learning
- Apply patterns from previous months
- Reflect on what you've learned

---

### 5. Engagement (10%)

**What It Measures**: Active participation in the learning process

**Signals**:
- Questions asked
- Blockers reported and resolved
- Retrospective participation
- Feedback given

**Scoring**:
| Score | Criteria |
|-------|----------|
| 100% | Active questions, blockers resolved, full retros |
| 80% | Regular engagement with system |
| 60% | Moderate interaction |
| 40% | Limited engagement |
| 20% | Minimal interaction |
| 0% | No engagement signals |

**How to Improve**:
- Ask questions when stuck
- Report blockers promptly
- Complete weekly retrospectives
- Use `/debug-learning` command

---

## Overall Score Calculation

```
Overall = (Completion × 0.30) +
          (Quality × 0.25) +
          (Consistency × 0.20) +
          (Growth × 0.15) +
          (Engagement × 0.10)
```

---

## Status Levels

| Overall Score | Status | Description |
|---------------|--------|-------------|
| 90% - 100% | Excellent | Exceeding expectations |
| 70% - 89% | On Track | Meeting objectives |
| 50% - 69% | Needs Attention | Some areas struggling |
| 0% - 49% | At Risk | Significant intervention needed |

---

## Adaptation Triggers

### Level Downgrade Consideration
- Triggered when: Overall < 40%
- Action: Propose moving to lower level
- Requires: Manual approval

### Remediation Week
- Triggered when: 40% ≤ Overall < 60%
- Action: Insert catch-up week
- Requires: Usually auto-approved

### On Track
- Triggered when: 60% ≤ Overall < 80%
- Action: No changes
- Requires: N/A

### Acceleration Consideration
- Triggered when: Overall ≥ 90%
- Action: Propose advanced challenges
- Requires: Manual approval

---

## Evaluation Frequency

| Type | Frequency | Scope |
|------|-----------|-------|
| Status Check | Daily | Current week |
| Weekly Evaluation | End of week | Last 7 days |
| Monthly Evaluation | End of month | Full month |
| Full Evaluation | On demand | All history |

---

## Running Evaluation

### Via Command
```
/evaluate
```

### Via Script
```bash
python .claude/path-engine/evaluate.py
python .claude/path-engine/evaluate.py --scope month
python .claude/path-engine/evaluate.py --output json
```

---

## Understanding Your Report

### Sample Report

```
EVALUATION REPORT
══════════════════════════════════════════

Learner: learner-001 (Advanced)
Scope: week
Status: ON TRACK

SCORES
──────────────────────────────
  completion   [████████░░] 82%
  quality      [███████░░░] 75%
  consistency  [█████████░] 88%
  growth       [███████░░░] 70%
  engagement   [████████░░] 80%

  OVERALL      [79%]

RECOMMENDATIONS
──────────────────────────────
  • Add more tests to improve quality score
  • Capture learnings as best practices
```

### Reading the Report

1. **Status**: Quick indicator of overall progress
2. **Scores**: Visual breakdown by dimension
3. **Recommendations**: Specific actions to improve

---

## Improving Scores

### Quick Wins

| Dimension | Quick Action |
|-----------|--------------|
| Completion | Complete one pending task |
| Quality | Run `/harden` on existing code |
| Consistency | Make a commit today |
| Growth | Add one best practice |
| Engagement | Run `/retro` |

### Long-term Improvement

1. **Establish routines**: Daily commits, weekly retros
2. **Build habits**: Test as you code, document as you build
3. **Reflect regularly**: Use retrospectives meaningfully
4. **Ask for help**: Don't let blockers persist

---

## See Also

- [Adaptation Rules](adaptation-rules.md) — What happens after evaluation
- [How to Use](../how-to-use.md) — Daily workflow
- [Memory System](../memory-system.md) — How data is stored
