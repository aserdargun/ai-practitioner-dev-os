# Command: /plan-week

## Purpose

Create a detailed week plan aligned with the current month's learning goals. The plan breaks down monthly deliverables into daily/weekly tasks.

## Inputs

- **Week number** (optional): Which week to plan (1-4). Defaults to current week.
- Context is read from:
  - Current month README (`paths/advanced/month-XX/README.md`)
  - Learner profile (`.claude/memory/learner_profile.json`)
  - Progress log (`.claude/memory/progress_log.jsonl`)
  - Tracker (`paths/advanced/tracker.md`)

## Outputs

A proposed week plan including:
- Weekly goals (subset of month deliverables)
- Daily task breakdown with time estimates
- Dependencies between tasks
- Risk callouts
- **Requires user approval before execution**

## When to Use

- Start of each week
- After completing a week (to plan next)
- After evaluation suggests re-planning
- When current plan isn't working

## Agent Routing

**Primary**: Planner Agent

The Planner analyzes month goals, your profile, and past velocity to create a realistic plan.

## Example Usage

**User Input**:
```
/plan-week
```

**Expected Output**:
```
## Proposed Week 2 Plan (Month 03: RAG Systems)

### Goals for This Week
Based on Month 03 deliverables and your profile:

1. [ ] Complete retrieval pipeline implementation
2. [ ] Write unit tests for retrieval (minimum 3)
3. [ ] Document chunking strategy decision
4. [ ] Start on answer generation module

### Daily Breakdown

| Day | Task | Est. Time | Dependencies |
|-----|------|-----------|--------------|
| Mon | Set up vector store connection | 2h | None |
| Tue | Implement chunking logic | 3h | Vector store |
| Wed | Build retrieval function | 3h | Chunking |
| Thu | Write unit tests | 2h | Retrieval |
| Fri | Documentation + answer module start | 3h | Tests |

### Risks
- Vector store setup might take longer if dependency conflicts occur
- Retrieval tuning often takes iteration

### Time Budget
- Total estimated: 13h
- Your available time (from profile): 15h/week
- Buffer: 2h ✅

---

**Do you approve this plan?** (yes / modify / no)

If you'd like to modify:
- "Move documentation to Thursday"
- "Reduce scope - skip answer module"
- "Add more time for retrieval"
```

## Plan Modification Examples

```
/plan-week week 3

/plan-week "I have less time this week, maybe 10 hours"

/plan-week "I want to focus only on testing this week"
```

## Related Commands

- `/status` - See current progress
- `/start-week` - Begin executing approved plan
- `/adapt-path` - Major path changes (month swaps, level changes)
