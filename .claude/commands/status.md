# Command: /status

## Purpose

Check current progress, blockers, and recommended next steps. This is your "where am I?" command.

## Inputs

None required. The command reads from:
- `.claude/memory/progress_log.jsonl`
- `.claude/memory/learner_profile.json`
- `paths/advanced/tracker.md`
- Current month README

## Outputs

A status report including:
- Current month and week
- Progress against week plan (% complete)
- Active blockers (if any)
- Recent activity summary
- Recommended next action

## When to Use

- Start of each day
- When you feel lost or unsure what to do next
- Before planning a new week
- After a break to get re-oriented

## Agent Routing

**Primary**: Planner Agent

The Planner reads your context and synthesizes a status report.

## Example Usage

**User Input**:
```
/status
```

**Expected Output**:
```
## Status Report

### Current Position
- **Month**: 03 (RAG Systems)
- **Week**: 2 of 4
- **Day**: Wednesday

### Week 2 Progress: 45%
- [x] Set up vector store connection
- [x] Implement document chunking
- [ ] Build retrieval function (in progress)
- [ ] Write unit tests
- [ ] Documentation

### Blockers
- None identified

### Recent Activity (last 48h)
- Completed chunking implementation
- Added 2 entries to progress log
- 1 commit to main branch

### Recommended Next Action
Continue with "Build retrieval function" - you're on track.

---
Run `/plan-week` to see full week plan.
Run `/debug-learning` if you're stuck on retrieval.
```

## Related Commands

- `/plan-week` - Create/view detailed week plan
- `/evaluate` - Get formal evaluation scores
- `/debug-learning` - Get help if stuck
