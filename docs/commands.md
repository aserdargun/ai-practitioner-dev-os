# Commands Guide

Friendly guide to using slash commands in the AI Practitioner Learning OS.

## Overview

Commands are shortcuts you type in Claude Code to invoke specific functionality. Each command routes to an appropriate agent and produces useful output.

## Command Catalog

For the complete technical reference, see [.claude/commands/catalog.md](../.claude/commands/catalog.md).

## Quick Reference

| Command | What It Does | When to Use |
|---------|--------------|-------------|
| `/status` | Check current progress | Start of day, feeling lost |
| `/plan-week` | Create week plan | Start of week |
| `/start-week` | Begin execution | After plan approved |
| `/ship-mvp` | Finalize deliverable | Core features done |
| `/harden` | Quality review | Before shipping |
| `/publish` | Prepare for sharing | Ready to demo |
| `/retro` | Reflect on week/month | End of period |
| `/evaluate` | Compute scores | End of month |
| `/adapt-path` | Get recommendations | After evaluation |
| `/add-best-practice` | Capture learning | After solving problem |
| `/debug-learning` | Get unstuck | When confused |

## Planning Commands

### /status

**What it does**: Shows where you are - current month, week, progress, blockers.

**Example output**:
```
## Status Report

### Current Position
- Month: 03 (RAG Systems)
- Week: 2 of 4
- Progress: 45%

### This Week
- [x] Set up vector store
- [ ] Implement retrieval (in progress)
- [ ] Write tests

### Recommended Action
Continue with retrieval implementation.
```

**When to use**: Every morning, when feeling lost, before planning.

### /plan-week

**What it does**: Creates a detailed week plan aligned with month goals.

**Example output**:
```
## Week 2 Plan

### Goals
1. Complete retrieval pipeline
2. Write 5 unit tests
3. Document chunking strategy

### Daily Tasks
| Day | Task | Time |
|-----|------|------|
| Mon | Chunking logic | 3h |
| Tue | Retrieval | 3h |
...

**Approve?** (yes/modify/no)
```

**When to use**: Start of each week, after evaluation.

## Building Commands

### /start-week

**What it does**: Kicks off the approved week plan with initial scaffolding.

**Example output**:
```
## Starting Week 2

### First Task: Chunking Logic

I'll create:
- rag/chunking.py
- tests/test_chunking.py

**Approve?** (yes/modify/no)
```

**When to use**: After approving a week plan.

### /ship-mvp

**What it does**: Checks DoD, finalizes deliverable, prepares for demo.

**Example output**:
```
## Ship MVP Check

### Definition of Done
- [x] Retrieval works
- [x] 5 tests pass
- [ ] Demo script (missing)

### Action
Create demo.py

**Proceed?** (yes/no)
```

**When to use**: Core functionality is working.

## Quality Commands

### /harden

**What it does**: Reviews code for quality, security, performance issues.

**Example output**:
```
## Code Review

### 🔴 Critical (1)
- Line 45: SQL injection risk

### 🟠 Important (2)
- Missing error handling
- No input validation

### 🟡 Suggestions (3)
- Add type hints
...
```

**When to use**: Before shipping, when concerned about quality.

### /publish

**What it does**: Prepares work for external sharing - demo script, blog template.

**Example output**:
```
## Publish Checklist

- [x] Tests passing
- [x] Docs complete
- [ ] Demo script

### Demo Outline
1. Intro (30s)
2. Problem (30s)
3. Solution (2m)
...
```

**When to use**: Ready to share externally.

## Reflection Commands

### /retro

**What it does**: Facilitates week/month retrospective.

**Example output**:
```
## Week 2 Retrospective

### What went well?
> (your input)

### What didn't?
> (your input)

### Best practice to capture?
> Test chunking with real data first

**Add to best_practices.md?** (yes/no)
```

**When to use**: End of week, end of month.

### /evaluate

**What it does**: Computes formal scores against the rubric.

**Example output**:
```
## Evaluation Report

| Category | Score |
|----------|-------|
| Completion | 85% |
| Quality | 90% |
| Velocity | 70% |
| Reflection | 95% |
| **Overall** | 84% |

Status: ✅ PASSING (threshold: 70%)
```

**When to use**: End of month, milestone reached.

### /adapt-path

**What it does**: Proposes path changes based on evaluation.

**Example output**:
```
## Adaptation Proposals

### Proposal 1: Remediation Week
Insert 1 week after Month 03 for catching up.

**Approve?** (yes/no)
```

**When to use**: After evaluation, when scores are concerning.

## Help Commands

### /add-best-practice

**What it does**: Adds a learned pattern to best practices.

**Example**:
```
/add-best-practice "Test with real data before committing"
```

**When to use**: After learning something valuable.

### /debug-learning

**What it does**: Helps diagnose and resolve learning blockers.

**Example output**:
```
## Debug Learning

### Questions
1. What are you trying to do?
2. What have you tried?
3. Where does it break?

### Common issues at this stage
- Embedding dimension mismatch
- Chunking strategy confusion
...
```

**When to use**: When stuck, confused, frustrated.

## Command Workflows

### Daily Workflow
```
/status → work → /status
```

### Weekly Workflow
```
/plan-week → /start-week → [work] → /harden → /retro
```

### Monthly Workflow
```
/evaluate → /adapt-path → /publish → /retro
```

### When Stuck
```
/debug-learning → [try suggestions] → /status
```

## Tips

1. **Use /status often** - It's your compass
2. **Plan before building** - /plan-week first
3. **Reflect weekly** - /retro cements learning
4. **Evaluate monthly** - /evaluate tracks progress
5. **Capture patterns** - /add-best-practice compounds

## Technical Details

Commands are defined in `.claude/commands/`:
- Each command has its own `.md` file
- Commands route to agents
- All state changes require approval

See [.claude/commands/README.md](../.claude/commands/README.md) for implementation details.
