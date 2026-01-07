# Command Catalog

This is the **source of truth** for all commands in the AI Practitioner Learning OS.

---

## Planning Commands

### `/status`

**Purpose**: Check current progress and blockers

**Agent**: Planner

**Inputs**: None

**Outputs**:
- Current month and week
- Completion percentage
- Active tasks
- Blockers (if any)
- Next actions

**When to use**: Start of day, before planning, when feeling lost

**Example**:
```
/status
```

---

### `/plan-week`

**Purpose**: Generate a weekly learning plan

**Agent**: Planner

**Inputs**:
- Optional: Focus areas
- Optional: Time constraints

**Outputs**:
- Day-by-day task breakdown
- Learning objectives
- Deliverables due
- Time estimates

**When to use**: Monday, start of each week

**Example**:
```
/plan-week

I have 10 hours this week. Focus on data cleaning.
```

---

### `/start-week`

**Purpose**: Initialize a new week with pre-flight checks

**Agent**: Planner

**Inputs**: None

**Outputs**:
- Week plan stub created
- Tracker updated
- Pre-week hook triggered
- Blockers identified

**When to use**: Monday morning

**Example**:
```
/start-week
```

---

## Building Commands

### `/ship-mvp`

**Purpose**: Guide through shipping a minimal viable product

**Agent**: Builder

**Inputs**:
- Feature/project description
- Optional: Constraints

**Outputs**:
- MVP scope definition
- Implementation steps
- Working code
- Basic tests

**When to use**: Starting a new feature or project

**Example**:
```
/ship-mvp

Build a CSV cleaning pipeline that handles missing values.
```

---

### `/harden`

**Purpose**: Add tests, error handling, and documentation

**Agent**: Builder

**Inputs**:
- Code/module to harden
- Optional: Focus areas

**Outputs**:
- Additional tests
- Error handling
- Updated documentation
- Quality report

**When to use**: After MVP works, before publishing

**Example**:
```
/harden

Add error handling and tests to the data pipeline.
```

---

### `/publish`

**Purpose**: Prepare work for demo and write-up

**Agent**: Builder

**Inputs**:
- Project to publish
- Target audience

**Outputs**:
- Demo script
- README updates
- Write-up outline
- Portfolio entry

**When to use**: End of month, deliverable complete

**Example**:
```
/publish

Prepare a demo and LinkedIn post for my sentiment analysis project.
```

---

## Coaching Commands

### `/retro`

**Purpose**: Run a retrospective on the week

**Agent**: Coach

**Inputs**:
- Optional: Topics to reflect on

**Outputs**:
- What went well
- What could improve
- Action items
- Lessons learned

**When to use**: Friday, end of week

**Example**:
```
/retro

Reflect on this week. I completed EDA but struggled with visualization.
```

---

### `/add-best-practice`

**Purpose**: Capture a new best practice

**Agent**: Coach

**Inputs**:
- Practice description
- Context
- Why it works

**Outputs**:
- Entry added to best_practices.md
- Confirmation

**When to use**: When discovering something that works well

**Example**:
```
/add-best-practice

Writing tests before implementing helps me think through edge cases.
```

---

### `/debug-learning`

**Purpose**: Diagnose why you're stuck

**Agent**: Coach

**Inputs**:
- Description of struggle
- What you've tried

**Outputs**:
- Root cause analysis
- Recommendations
- Resources
- Adjusted approach

**When to use**: Stuck for more than an hour

**Example**:
```
/debug-learning

My model accuracy is stuck at 60%. I've tried different features and hyperparameters.
```

---

## Evaluation Commands

### `/evaluate`

**Purpose**: Run evaluation engine on progress

**Agent**: Evaluator

**Inputs**: None (reads from memory)

**Outputs**:
- Overall score (0-100)
- Category scores
- Strengths
- Gaps
- Recommendations

**When to use**: End of week, end of month, when uncertain

**Example**:
```
/evaluate
```

---

### `/adapt-path`

**Purpose**: Propose path modifications based on evaluation

**Agent**: Evaluator

**Inputs**:
- Optional: Specific concern

**Outputs**:
- Adaptation proposal
- Rationale
- Expected impact
- Approval request

**When to use**: After evaluation shows need for change

**Example**:
```
/adapt-path

I'm struggling with time series. What changes would help?
```

---

### `/report`

**Purpose**: Generate or update tracker report

**Agent**: Evaluator

**Inputs**:
- Optional: Report type (summary, detailed)

**Outputs**:
- Updated tracker.md
- Progress visualization
- Key metrics

**When to use**: Weekly, for record-keeping

**Example**:
```
/report
```

---

## Command Routing Summary

| Command | Primary Agent | Supporting Agents |
|---------|---------------|-------------------|
| `/status` | Planner | - |
| `/plan-week` | Planner | - |
| `/start-week` | Planner | - |
| `/ship-mvp` | Builder | Reviewer |
| `/harden` | Builder | Reviewer |
| `/publish` | Builder | Reviewer |
| `/retro` | Coach | Evaluator |
| `/evaluate` | Evaluator | - |
| `/adapt-path` | Evaluator | Coach |
| `/add-best-practice` | Coach | - |
| `/debug-learning` | Coach | Researcher |
| `/report` | Evaluator | - |

---

## Using Commands Effectively

### Daily Workflow
1. `/status` - Start of day
2. Work on tasks
3. Log progress

### Weekly Workflow
1. **Monday**: `/start-week`, `/plan-week`
2. **Tue-Thu**: Build, iterate
3. **Friday**: `/evaluate`, `/retro`, `/report`

### Monthly Workflow
1. **End of month**: `/evaluate`, `/adapt-path`
2. **Publish**: `/publish`
3. **New month**: `/plan-week` for first week
