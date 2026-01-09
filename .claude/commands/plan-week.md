# Command: /plan-week

## Purpose

Generate a detailed plan for the current week, breaking down the month's project into actionable daily tasks.

## Inputs

Optional context you can provide:
- Available hours this week
- Specific constraints or priorities
- Blockers from previous week

The command reads from:
- Current month's README (`paths/intermediate/month-XX/README.md`)
- `.claude/memory/learner_profile.json`
- `.claude/memory/progress_log.jsonl`
- `paths/intermediate/tracker.md`

## Outputs

- Day-by-day task breakdown
- Learning objectives for the week
- Key milestones and checkpoints
- Resources to prepare

**Note**: Plan is proposed for your approval before being saved.

## When to Use

- Start of each week
- After completing a major milestone
- When replanning due to changes

## Agent Routing

**Primary**: Planner Agent

The Planner considers your schedule constraints, current progress, and monthly objectives to create a realistic week plan.

## Example Usage

```
/plan-week
```

Or with constraints:

```
/plan-week

I have about 8 hours this week. I need to focus on the data pipeline
but also want to make progress on tests.
```

## Output Format

```markdown
## Week Plan — Month X, Week Y

### Week Objectives
- [ ] Primary objective
- [ ] Secondary objective

### Daily Breakdown

#### Monday
- [ ] Task 1 (est. 1h)
- [ ] Task 2 (est. 30m)

#### Tuesday
- [ ] Task 3 (est. 2h)

[... continues for each day]

### Key Milestones
- By Wednesday: [milestone]
- By Friday: [milestone]

### Resources
- [Link to relevant skill playbook]
- [Link to template]

### Notes
Any special considerations for this week.

---
**Approve this plan?** (yes/no/modify)
```

## Approval Workflow

1. Planner generates the proposed plan
2. You review the plan
3. Options:
   - Approve: Plan is saved and tracker updated
   - Modify: Provide feedback for revision
   - Reject: Start fresh with new constraints
