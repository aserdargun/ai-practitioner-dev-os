# Command: /plan-week

## Purpose
Create a detailed weekly learning plan with day-by-day task breakdown, aligned with current month goals and available time.

## Inputs
- **Available hours** (recommended): How much time you have this week
- **Focus areas** (optional): Specific topics or tasks to prioritize
- **Constraints** (optional): Days off, meetings, energy levels

Example:
```
/plan-week I have 12 hours this week, focus on the ML model, I'm off Wednesday
```

## Outputs
- **Weekly Goals**: 2-3 key outcomes for the week
- **Day-by-Day Breakdown**: Tasks mapped to days with time estimates
- **Dependencies**: What needs to happen before what
- **Definition of Done**: How you'll know the week was successful
- **Contingency**: What to cut if time runs short

## When to Use
- Start of each week (Sunday/Monday)
- After completing a week to plan the next
- When you need to re-plan mid-week due to changes

## Agent Routing
**Planner** — reads learner profile, current month goals, and progress to create plan

## Example Usage

### Basic Planning
```
/plan-week
I have 10 hours available
```

### Focused Planning
```
/plan-week
15 hours available
Focus on shipping the API endpoint and writing tests
I work best in mornings
```

### Constrained Planning
```
/plan-week
Only 6 hours this week due to travel
What's the minimum viable progress I can make?
```

## Sample Output

```
📅 WEEK PLAN — Month 3, Week 2

Weekly Goals:
1. Complete data pipeline MVP
2. Write core tests (>80% coverage)
3. Document the API

Available: 10 hours

Day-by-Day:
┌─────────────┬──────────────────────────────────┬───────┐
│ Day         │ Tasks                            │ Hours │
├─────────────┼──────────────────────────────────┼───────┤
│ Monday      │ Finish validation module         │ 2.0   │
│ Tuesday     │ Add error handling, edge cases   │ 2.0   │
│ Wednesday   │ Write unit tests                 │ 2.0   │
│ Thursday    │ Integration tests, fix bugs      │ 2.0   │
│ Friday      │ Documentation, cleanup           │ 1.5   │
│ Buffer      │ Contingency for overruns         │ 0.5   │
└─────────────┴──────────────────────────────────┴───────┘

Dependencies:
- Validation → Error handling → Tests

Definition of Done:
☐ Pipeline processes sample data end-to-end
☐ All tests pass
☐ README documents usage
☐ Code reviewed and cleaned

If Time Runs Short:
1. Cut: Extended documentation (do minimum)
2. Keep: Core tests (non-negotiable)
3. Move to next week: Edge case handling

Ready to start? Run /start-week to initialize.
```

## Related Commands
- `/status` — Check current state before planning
- `/start-week` — Initialize the week after planning
- `/retro` — Review last week before planning new one
