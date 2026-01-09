# Command: /status

## Purpose

Get a snapshot of your current progress, identify blockers, and see recommended next steps.

## Inputs

None required. The command reads from:
- `.claude/memory/learner_profile.json`
- `.claude/memory/progress_log.jsonl`
- `paths/intermediate/tracker.md`
- Current month's README

## Outputs

- Current month and week position
- Recent progress summary
- Active blockers (if any)
- Today's recommended focus
- Upcoming milestones

## When to Use

- Daily check-in before starting work
- When returning after a break
- When context-switching between projects
- When feeling uncertain about priorities

## Agent Routing

**Primary**: Planner Agent

The Planner reads your progress log and learning profile to generate a contextual status report.

## Example Usage

```
/status
```

Or with context:

```
/status

I was working on the RAG pipeline yesterday but got stuck on the retrieval step.
```

## Output Format

```markdown
## Status Report — [Date]

### Current Position
- **Month**: 3 of 12
- **Week**: 2 of 4
- **Project**: RAG Service with Evaluations

### Recent Progress
- Completed: [list of recent completions]
- In Progress: [current work items]

### Blockers
- [Any identified blockers]

### Today's Focus
Recommended priority for today:
1. [Primary focus]
2. [Secondary if time permits]

### Upcoming
- This week: [milestones]
- This month: [deliverables due]
```
