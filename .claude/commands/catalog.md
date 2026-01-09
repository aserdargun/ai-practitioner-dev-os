# Command Catalog

Complete reference for all available slash commands.

---

## Planning & Progress

### /status
**Purpose**: Get a snapshot of current progress, blockers, and next steps.
**Agent**: Planner
**When**: Daily check-in, before starting work, when context-switching
**File**: [status.md](status.md)

### /plan-week
**Purpose**: Generate a detailed plan for the current week.
**Agent**: Planner
**When**: Start of each week, after completing a major milestone
**File**: [plan-week.md](plan-week.md)

### /start-week
**Purpose**: Initialize week with project setup and tracker updates.
**Agent**: Planner + Builder
**When**: First day of a new week
**File**: [start-week.md](start-week.md)

---

## Building & Quality

### /ship-mvp
**Purpose**: Checklist and guidance for completing the MVP.
**Agent**: Builder
**When**: Mid-week, when core features are ready
**File**: [ship-mvp.md](ship-mvp.md)

### /harden
**Purpose**: Focus on code quality, tests, and documentation.
**Agent**: Builder + Reviewer
**When**: Week 3 of monthly cycle, before publishing
**File**: [harden.md](harden.md)

### /publish
**Purpose**: Prepare demo and write-up for the project.
**Agent**: Builder
**When**: Week 4, when project is complete
**File**: [publish.md](publish.md)

---

## Reflection & Evaluation

### /retro
**Purpose**: Conduct weekly retrospective and log learnings.
**Agent**: Coach
**When**: End of each week
**File**: [retro.md](retro.md)

### /evaluate
**Purpose**: Assess deliverables against the evaluation rubric.
**Agent**: Evaluator
**When**: End of week/month, after completing deliverables
**File**: [evaluate.md](evaluate.md)

---

## Adaptation & Learning

### /adapt-path
**Purpose**: Request or review learning path adaptations.
**Agent**: Evaluator + Coach
**When**: When struggling, accelerating, or at month boundary
**File**: [adapt-path.md](adapt-path.md)

### /add-best-practice
**Purpose**: Document a learning or insight for future reference.
**Agent**: Coach
**When**: After a breakthrough, lesson learned, or pattern discovered
**File**: [add-best-practice.md](add-best-practice.md)

### /debug-learning
**Purpose**: Troubleshoot blockers and get unstuck.
**Agent**: Coach + Researcher
**When**: When stuck for more than a session, confused about concepts
**File**: [debug-learning.md](debug-learning.md)

---

## Command Quick Reference

| Command | Agent | Weekly Cadence |
|---------|-------|----------------|
| `/status` | Planner | Daily |
| `/plan-week` | Planner | Week 1 start |
| `/start-week` | Planner + Builder | Week 1 start |
| `/ship-mvp` | Builder | Week 2 |
| `/harden` | Builder + Reviewer | Week 3 |
| `/publish` | Builder | Week 4 |
| `/retro` | Coach | Weekly |
| `/evaluate` | Evaluator | Weekly/Monthly |
| `/adapt-path` | Evaluator + Coach | As needed |
| `/add-best-practice` | Coach | As discovered |
| `/debug-learning` | Coach + Researcher | As needed |

---

## Typical Week Flow

```
Monday:    /start-week → /plan-week → /status
Daily:     /status → work → log progress
Mid-week:  /ship-mvp (when MVP ready)
Week 3:    /harden
Week 4:    /publish → /evaluate
Friday:    /retro
Monthly:   /evaluate → /adapt-path (if needed)
```
