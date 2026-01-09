# Command: /start-week

## Purpose
Initialize structure and artifacts for a new learning week, including creating the week plan file, updating the tracker, and setting up the work environment.

## Inputs
- Week number (optional, defaults to next week)
- Approved plan from `/plan-week` (optional)

## Outputs
- **Week Plan File**: `paths/beginner/journal/week-XX.md`
- **Updated Tracker**: Entry in `paths/beginner/tracker.md`
- **Progress Log Entry**: Event in `.claude/memory/progress_log.jsonl`
- **Checklist**: Tasks ready to work on

## When to Use
- After `/plan-week` to formalize the plan
- Start of each week to create structure
- When beginning a new month

## Agent Routing
**Planner** — creates week structure, updates tracker

## Example Usage

### Start Next Week
```
/start-week
```

### Start Specific Week
```
/start-week Week 3 of Month 2
```

### Start with Context
```
/start-week
Using the plan we just created
Focus on API development
```

## Sample Output

```
🚀 WEEK STARTED — Month 3, Week 2

Created Files:
✓ paths/beginner/journal/month-03-week-02.md
✓ Updated paths/beginner/tracker.md
✓ Logged event to progress_log.jsonl

This Week's Focus:
→ Complete data pipeline MVP

Checklist Ready:
☐ Finish validation module
☐ Add error handling
☐ Write unit tests
☐ Integration tests
☐ Documentation

Daily Standup Prompt:
"What did I do yesterday? What will I do today? Any blockers?"

Quick Start:
1. Review today's tasks in your journal
2. Start with the first unchecked item
3. Log progress as you go
4. Ask Claude for help anytime

Commands for this week:
- /status — Check progress
- /debug-learning — If stuck
- /retro — End of week review

Good luck! 💪
```

## Week File Template

The created week file follows this structure:

```markdown
# Month 3 — Week 2

## Goals
- [ ] Complete data pipeline MVP
- [ ] Write core tests
- [ ] Document the API

## Daily Log

### Monday
- [ ] Finish validation module (2h)
Notes:

### Tuesday
- [ ] Add error handling (2h)
Notes:

...

## Reflections
(Fill in at end of week)

## Blockers Encountered

## Best Practices Learned
```

## Related Commands
- `/plan-week` — Create plan before starting
- `/status` — Check progress during the week
- `/retro` — End the week with reflection
