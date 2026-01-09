# Command: /status

## Purpose
Display a comprehensive snapshot of current learning progress, including completed tasks, active work, blockers, and recommended next actions.

## Inputs
None required. Optionally specify a focus area:
- `/status` — Full status
- `/status month` — Focus on current month
- `/status week` — Focus on current week

## Outputs
- **Progress Summary**: Tasks completed vs. planned
- **Current Focus**: What you're working on now
- **Blockers**: Any identified obstacles
- **Next Actions**: Recommended next steps
- **Quick Stats**: Hours logged, streak, velocity

## When to Use
- Start of each work session to orient yourself
- When feeling lost or unsure what to do next
- Before planning a new week
- When reporting progress to yourself

## Agent Routing
**Evaluator** — reads memory files and repo signals to generate status

## Example Usage

### Basic Status
```
/status
```

### Month Focus
```
/status month
Show me where I stand for Month 3 goals
```

### Week Focus
```
/status week
What did I accomplish this week?
```

## Sample Output

```
📊 STATUS REPORT — Week 2, Month 3

Progress: 7/12 tasks completed (58%)
Hours Logged: 8.5 hours
Velocity: On track

Current Focus:
- Building data validation module

Completed This Week:
✓ Set up project structure
✓ Implemented data ingestion
✓ Wrote initial tests

Blockers:
⚠ Struggling with datetime parsing edge cases

Next Actions:
1. Finish validation module (2h estimated)
2. Add error handling (1h)
3. Update documentation (30min)

Quick Wins Available:
- Add docstrings to completed functions
- Run linter and fix warnings
```

## Related Commands
- `/plan-week` — Create a plan based on status
- `/evaluate` — Get detailed evaluation scores
- `/debug-learning` — Investigate blockers
