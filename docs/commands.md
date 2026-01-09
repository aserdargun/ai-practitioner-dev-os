# Commands Guide

A friendly guide to using slash commands in the learning system.

## Overview

Commands are typed in Claude Code as `/command-name`. They invoke specific workflows and route to appropriate agents.

For the complete technical reference, see [.claude/commands/catalog.md](../.claude/commands/catalog.md).

---

## Quick Reference

| Command | When to Use | Agent |
|---------|-------------|-------|
| `/status` | Check current state | Planner |
| `/plan-week` | Start of week | Planner |
| `/start-week` | Initialize week | Planner + Builder |
| `/ship-mvp` | MVP ready | Builder |
| `/harden` | Week 3 | Builder + Reviewer |
| `/publish` | Week 4 | Builder |
| `/retro` | End of week | Coach |
| `/evaluate` | After deliverables | Evaluator |
| `/adapt-path` | Path change needed | Evaluator + Coach |
| `/add-best-practice` | Capture learning | Coach |
| `/debug-learning` | When stuck | Coach + Researcher |

---

## Daily Commands

### /status

Get a snapshot of where you are.

```
/status
```

**Output**:
- Current month and week
- Recent progress
- Today's recommended focus
- Any blockers

**When to use**: Every day when starting work.

---

## Planning Commands

### /plan-week

Generate a detailed weekly plan.

```
/plan-week

I have about 10 hours this week. Focus on the data pipeline.
```

**Output**:
- Day-by-day task breakdown
- Learning objectives
- Resources needed

**When to use**: Start of each week.

### /start-week

Initialize a new week with setup tasks.

```
/start-week
```

**Output**:
- Week journal created
- Tracker updated
- Environment verified

**When to use**: First day of the week.

---

## Building Commands

### /ship-mvp

Get checklist for MVP completion.

```
/ship-mvp

I've finished the core features. What's missing for MVP?
```

**Output**:
- Completion checklist
- Gap analysis
- Implementation guidance

**When to use**: Mid-week, when core features are done.

### /harden

Focus on quality and testing.

```
/harden

Focus on error handling and edge cases.
```

**Output**:
- Quality assessment
- Test gaps
- Refactoring suggestions

**When to use**: Week 3, before publishing.

### /publish

Prepare demo and write-up.

```
/publish

I want to write a blog post about this project.
```

**Output**:
- Demo script
- Write-up outline
- Portfolio entry

**When to use**: Week 4, when project is complete.

---

## Reflection Commands

### /retro

Conduct weekly retrospective.

```
/retro

This week I finally got the pipeline working but struggled with tests.
```

**Output**:
- Structured reflection
- Learnings captured
- Process improvements

**When to use**: End of each week.

### /evaluate

Get performance assessment.

```
/evaluate

Evaluate my Month 3 deliverables.
```

**Output**:
- Score breakdown
- Evidence citations
- Recommendations

**When to use**: After completing deliverables.

---

## Adaptation Commands

### /adapt-path

Request or review path changes.

```
/adapt-path

I've been scoring 95%+ for three weeks. Should I consider upgrading?
```

**Output**:
- Path assessment
- Proposed adaptations
- Impact analysis

**When to use**: When you need a path change.

### /add-best-practice

Document a learning.

```
/add-best-practice

Always check retrieval quality before debugging RAG generation.
```

**Output**:
- Formatted entry
- Updated best_practices.md

**When to use**: After breakthroughs or lessons learned.

### /debug-learning

Troubleshoot blockers.

```
/debug-learning

I've been stuck on attention mechanisms for three days.
```

**Output**:
- Problem diagnosis
- Solution approaches
- Resources

**When to use**: When stuck for more than a session.

---

## Command Flow by Week

### Week 1
```
Monday:     /start-week → /plan-week
Daily:      /status
```

### Week 2
```
Monday:     /status → work
Mid-week:   /ship-mvp
Daily:      /status
```

### Week 3
```
Monday:     /status
Focus:      /harden
Daily:      Build + test
```

### Week 4
```
Early:      /publish
End:        /retro → /evaluate
```

---

## Tips

### Getting More from Commands

Add context to get better results:

```
# Basic
/plan-week

# Better - with constraints
/plan-week

I have 8 hours this week. I want to focus on the ML model
but also need to write some tests.

# Better - with blockers
/status

I was working on the API yesterday but got stuck on authentication.
```

### Combining Commands

```
# Full evaluation cycle
/evaluate
# Review results, then:
/adapt-path
# If approved, then:
python .claude/path-engine/report.py
```

### When Commands Don't Help

If a command doesn't give you what you need:
1. Try `/debug-learning` with specific context
2. Ask Claude directly: "Help me with [specific thing]"
3. Check the skill playbooks in `.claude/skills/`

---

## Related Documentation

- [.claude/commands/catalog.md](../.claude/commands/catalog.md) — Technical reference
- [.claude/commands/README.md](../.claude/commands/README.md) — Command system overview
- [agents.md](agents.md) — Agent capabilities
- [how-to-use.md](how-to-use.md) — Overall workflow
