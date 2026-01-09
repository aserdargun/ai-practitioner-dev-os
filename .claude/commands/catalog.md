# Command Catalog

Complete reference of all available slash commands.

---

## Progress & Planning

### /status
**Purpose**: Display current progress snapshot
**Agent**: Evaluator
**Outputs**: Progress summary, blockers, next actions
**Usage**: `/status`

### /plan-week
**Purpose**: Create a detailed weekly plan
**Agent**: Planner
**Inputs**: Available hours, focus areas (optional)
**Outputs**: Day-by-day task breakdown
**Usage**: `/plan-week I have 10 hours, focus on the API project`

### /start-week
**Purpose**: Initialize structure for a new week
**Agent**: Planner
**Outputs**: Week plan file, updated tracker
**Usage**: `/start-week`

---

## Building & Shipping

### /ship-mvp
**Purpose**: Finalize MVP to demo-ready state
**Agent**: Builder
**Inputs**: MVP requirements
**Outputs**: Working MVP, demo script
**Usage**: `/ship-mvp for the forecasting dashboard`

### /harden
**Purpose**: Add tests, docs, and error handling
**Agent**: Builder + Reviewer
**Inputs**: Code to harden
**Outputs**: Tests, improved error handling, docs
**Usage**: `/harden the DataProcessor class`

### /publish
**Purpose**: Prepare demo and write-up for portfolio
**Agent**: Builder
**Outputs**: Demo guide, Medium post draft, screenshots
**Usage**: `/publish Month 3 project`

---

## Reflection & Learning

### /retro
**Purpose**: Run a structured retrospective
**Agent**: Coach + Reviewer
**Inputs**: Week or month to review
**Outputs**: Retrospective notes, action items
**Usage**: `/retro for Week 2`

### /add-best-practice
**Purpose**: Capture a learning to best practices
**Agent**: Coach
**Inputs**: The learning or insight
**Outputs**: Entry in best_practices.md
**Usage**: `/add-best-practice always validate input data before processing`

### /debug-learning
**Purpose**: Diagnose why you're stuck
**Agent**: Coach
**Inputs**: Description of blocker
**Outputs**: Diagnosis, suggested actions
**Usage**: `/debug-learning I can't understand decorators`

---

## Evaluation & Adaptation

### /evaluate
**Purpose**: Get evaluation scores against rubric
**Agent**: Evaluator
**Outputs**: Scores by dimension, gaps, trends
**Usage**: `/evaluate`

### /adapt-path
**Purpose**: See proposed path adaptations
**Agent**: Evaluator
**Outputs**: Adaptation proposals (require approval)
**Usage**: `/adapt-path`

---

## Quick Reference

```
/status              → See where you are
/plan-week           → Plan what's next
/start-week          → Begin a new week
/ship-mvp            → Finish MVP
/harden              → Improve quality
/publish             → Prepare for portfolio
/retro               → Reflect on progress
/evaluate            → Get scores
/adapt-path          → See recommendations
/add-best-practice   → Capture learning
/debug-learning      → Get unstuck
```

---

## Command Chaining

For common workflows, chain commands:

### Weekly Cycle
```
1. /start-week
2. [do the work]
3. /retro
4. /evaluate
```

### Ship & Publish
```
1. /ship-mvp
2. /harden
3. /publish
```

### Course Correct
```
1. /status
2. /debug-learning
3. /adapt-path
4. /plan-week
```
