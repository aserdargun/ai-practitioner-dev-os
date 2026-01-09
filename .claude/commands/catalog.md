# Command Catalog

Complete index of all available slash commands.

---

## Planning Commands

### /status
**Purpose**: Check current progress, blockers, and next steps
**Agent**: Planner
**Inputs**: None (reads from memory + tracker)
**Outputs**: Status report with progress, blockers, recommendations
**File**: [status.md](status.md)

### /plan-week
**Purpose**: Create a detailed week plan aligned with month goals
**Agent**: Planner
**Inputs**: Current week number (optional)
**Outputs**: Proposed week plan for approval
**File**: [plan-week.md](plan-week.md)

---

## Building Commands

### /start-week
**Purpose**: Begin executing the approved week plan
**Agent**: Builder
**Inputs**: Approved week plan
**Outputs**: Initial scaffolding, first task implementation
**File**: [start-week.md](start-week.md)

### /ship-mvp
**Purpose**: Finalize and ship the minimum viable deliverable
**Agent**: Builder + Reviewer
**Inputs**: Current implementation state
**Outputs**: Completed MVP with tests and docs
**File**: [ship-mvp.md](ship-mvp.md)

---

## Review Commands

### /harden
**Purpose**: Review and improve code quality, security, performance
**Agent**: Reviewer
**Inputs**: Files to review (or current project)
**Outputs**: Feedback with severity levels, suggested fixes
**File**: [harden.md](harden.md)

### /publish
**Purpose**: Prepare deliverable for external publishing
**Agent**: Reviewer
**Inputs**: Deliverable to publish
**Outputs**: Publish checklist, demo script, write-up template
**File**: [publish.md](publish.md)

---

## Reflection Commands

### /retro
**Purpose**: Run a retrospective on the week/month
**Agent**: Coach
**Inputs**: Period to reflect on (week/month)
**Outputs**: Retrospective notes, best practice candidates
**File**: [retro.md](retro.md)

### /add-best-practice
**Purpose**: Add a learned best practice to memory
**Agent**: Coach
**Inputs**: Best practice description
**Outputs**: Proposed addition to best_practices.md
**File**: [add-best-practice.md](add-best-practice.md)

### /debug-learning
**Purpose**: Get help when stuck on a concept or task
**Agent**: Coach
**Inputs**: Description of blocker
**Outputs**: Targeted advice, resources, experiments to try
**File**: [debug-learning.md](debug-learning.md)

---

## Evaluation Commands

### /evaluate
**Purpose**: Assess progress and compute scores
**Agent**: Evaluator
**Inputs**: None (reads from memory + repo signals)
**Outputs**: Evaluation report with scores and analysis
**File**: [evaluate.md](evaluate.md)

### /adapt-path
**Purpose**: Propose path adaptations based on evaluation
**Agent**: Evaluator
**Inputs**: Evaluation results
**Outputs**: Proposed adaptations for user approval
**File**: [adapt-path.md](adapt-path.md)

---

## Command Workflows

### Daily Workflow
```
/status → /start-week (continue) → work → /status
```

### Weekly Workflow
```
/plan-week → /start-week → work → /harden → /retro → /evaluate
```

### Monthly Workflow
```
/evaluate → /adapt-path → /publish → /retro → /plan-week (next month)
```

### When Stuck
```
/debug-learning → /status → continue or /plan-week (revise)
```

---

## Quick Reference

| Command | When to Use |
|---------|-------------|
| `/status` | Start of day, feeling lost, before planning |
| `/plan-week` | Start of week, after evaluation |
| `/start-week` | After plan approved, ready to build |
| `/ship-mvp` | Core functionality done, ready to finalize |
| `/harden` | Before shipping, quality concerns |
| `/publish` | Ready to share externally |
| `/retro` | End of week/month |
| `/evaluate` | End of month, milestone reached |
| `/adapt-path` | After evaluation, scores concerning |
| `/add-best-practice` | Learned something valuable |
| `/debug-learning` | Stuck, confused, frustrated |
