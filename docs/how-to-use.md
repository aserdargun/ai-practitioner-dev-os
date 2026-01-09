# How to Use

A comprehensive guide to using the AI Practitioner learning system.

## Overview

This learning OS follows a structured cycle:

1. **Plan** — Define weekly goals
2. **Build** — Work on projects
3. **Review** — Get feedback
4. **Evaluate** — Measure progress
5. **Adapt** — Adjust path as needed

---

## Getting Started

### First-Time Setup

1. **Verify your profile**
   ```bash
   cat .claude/memory/learner_profile.json
   ```
   Update with your goals, constraints, and preferences.

2. **Run initial evaluation**
   ```bash
   python .claude/path-engine/evaluate.py
   python .claude/path-engine/report.py
   ```

3. **Open your dashboard**
   - Go to `paths/intermediate/README.md`
   - This is your main navigation hub

### Daily Workflow

| Time | Action |
|------|--------|
| **Start** | Run `/status` to see today's focus |
| **Work** | Build, code, experiment on your project |
| **End** | Log progress in your journal |

### Quick Commands

```
/status        # Where am I? What's next?
/plan-week     # Plan this week's work
/ship-mvp      # MVP completion checklist
/harden        # Code quality focus
/retro         # Weekly reflection
/evaluate      # Get scored assessment
```

---

## Weekly Cadence

### Week 1: Learn & Setup

**Focus**: Understand concepts, set up project structure

Activities:
- Review month's learning goals
- Research required technologies
- Set up project from template
- Create initial scaffolding

Commands:
```
/start-week
/plan-week
```

### Week 2: Build MVP

**Focus**: Implement core functionality

Activities:
- Code main features
- Write initial tests
- Get feedback early

Commands:
```
/ship-mvp
/status
```

### Week 3: Harden

**Focus**: Quality, tests, documentation

Activities:
- Add comprehensive tests
- Handle edge cases
- Write documentation
- Refactor if needed

Commands:
```
/harden
```

### Week 4: Ship & Reflect

**Focus**: Demo, write-up, retrospective

Activities:
- Prepare demo
- Write project summary
- Conduct retrospective
- Run evaluation

Commands:
```
/publish
/retro
/evaluate
```

---

## Running the System Loop

### Locally with Scripts

```bash
# From repository root

# 1. Evaluate current progress
python .claude/path-engine/evaluate.py

# 2. Get adaptation proposals
python .claude/path-engine/adapt.py

# 3. Update tracker
python .claude/path-engine/report.py
```

### With Claude

```
# Check status
/status

# Full evaluation cycle
/evaluate

# Request path review
/adapt-path
```

---

## Logging Progress

### Weekly Journal

Create entries in `paths/intermediate/journal/`:

```markdown
# Week X — YYYY-MM-DD

## Goals
- [ ] Goal 1
- [ ] Goal 2

## Daily Log
### Monday
- What I worked on
- What I learned

### Tuesday
...

## Blockers
- Any issues faced

## Learnings
- Key insights

## Reflection
End of week thoughts
```

### Progress Events

Events are logged to `.claude/memory/progress_log.jsonl`:

```json
{"timestamp": "2026-01-15T10:00:00Z", "event": "milestone", "description": "Completed EDA"}
{"timestamp": "2026-01-15T18:00:00Z", "event": "learning", "description": "Learned about attention mechanisms"}
```

Claude will propose logging events; you approve before they're saved.

---

## Requesting Path Changes

### When to Request

- Consistently scoring 90+ (consider upgrade)
- Struggling for multiple weeks (consider remediation)
- Project doesn't fit your goals (consider swap)
- Circumstances changed (adjust constraints)

### How to Request

```
/adapt-path

I've been scoring above 90% for three weeks and finding
the material comfortable. Should I consider upgrading to Advanced?
```

### What Happens

1. System analyzes your progress
2. Proposals are generated
3. You review each proposal
4. You explicitly approve or reject
5. Only approved changes are applied

---

## Capturing Best Practices

### When to Capture

- After solving a tricky problem
- When you discover a useful pattern
- After making a mistake worth remembering
- When a retrospective surfaces insights

### How to Capture

```
/add-best-practice

I learned that when debugging RAG systems, always check retrieval
quality first before looking at generation.
```

### Where They're Stored

`.claude/memory/best_practices.md` — Review this file before starting new projects.

---

## Human-in-the-Loop Principle

**Nothing changes without your approval.**

The system:
1. **Analyzes** your progress
2. **Proposes** recommendations
3. **Waits** for your decision
4. **Executes** only what you approve

You have full control over:
- Memory updates
- Path adaptations
- Project decisions
- Evaluation validation

---

## Troubleshooting

### "I'm stuck"

```
/debug-learning

I've been stuck on [topic] for [time]. I've tried [what you tried].
```

### "My scores are low"

- Review the evidence in evaluation report
- Check if journal entries are up to date
- Consider using `/adapt-path` for remediation

### "I want to change something"

- For project changes: `/adapt-path`
- For schedule changes: Update `learner_profile.json`
- For immediate help: `/debug-learning`

---

## Quick Reference

### Files to Know

| File | Purpose |
|------|---------|
| `paths/intermediate/README.md` | Your dashboard |
| `.claude/memory/learner_profile.json` | Your configuration |
| `.claude/memory/progress_log.jsonl` | Your activity log |
| `.claude/memory/best_practices.md` | Your learnings |

### Commands by Phase

| Phase | Commands |
|-------|----------|
| Planning | `/status`, `/plan-week`, `/start-week` |
| Building | `/ship-mvp`, `/harden` |
| Reflecting | `/retro`, `/evaluate` |
| Adapting | `/adapt-path`, `/add-best-practice` |
| Debugging | `/debug-learning` |

---

## Related Documentation

- [commands.md](commands.md) — Full command reference
- [agents.md](agents.md) — Agent capabilities
- [memory-system.md](memory-system.md) — How memory works
- [evaluation/rubric.md](evaluation/rubric.md) — Scoring criteria
