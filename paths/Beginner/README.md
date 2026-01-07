# Beginner Dashboard

**Your AI Practitioner Learning OS Control Center**

---

## Your Level: Beginner

**Tier Coverage**: Tier 1 (Foundation) only
**Duration**: 12 months
**Focus**: Master Python, data science, and ML fundamentals

---

## Current Position

| Metric | Value |
|--------|-------|
| **Month** | 1 of 12 |
| **Week** | 1 of 4 |
| **Focus** | Python & Environment Setup |

> Update `current_month` and `current_week` in `.claude/memory/learner_profile.json` as you progress.

---

## This Week's Plan

```markdown
## Week Goals
- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

## Daily Tasks

### Monday
- [ ] Task 1
- [ ] Task 2

### Tuesday
- [ ] Task 1
- [ ] Task 2

### Wednesday
- [ ] Task 1
- [ ] Task 2

### Thursday
- [ ] Task 1
- [ ] Task 2

### Friday
- [ ] Task 1
- [ ] Run /evaluate
- [ ] Run /retro
```

**To generate your actual plan**: Run `/plan-week` in Claude.

---

## Commands Cheat Sheet

| Command | What It Does | When to Use |
|---------|--------------|-------------|
| `/status` | Check where you are | Daily |
| `/plan-week` | Create weekly plan | Monday |
| `/start-week` | Initialize the week | Monday |
| `/ship-mvp` | Build something | Starting features |
| `/harden` | Add tests & docs | After MVP works |
| `/publish` | Prepare for sharing | End of month |
| `/retro` | Weekly reflection | Friday |
| `/evaluate` | Get your scores | Weekly |
| `/adapt-path` | Adjust your path | After evaluation |
| `/add-best-practice` | Capture learning | Anytime |
| `/debug-learning` | Get unstuck | When stuck |
| `/report` | Update tracker | Weekly |

**Full command reference**: [docs/commands.md](../../docs/commands.md)

---

## Evaluation Snapshot

Run `/evaluate` to get your current scores:

| Category | What It Measures | Target |
|----------|------------------|--------|
| **Completion** (30%) | Tasks done, MVPs shipped | 3-5 tasks/week |
| **Quality** (25%) | Tests, docs, clean code | Tests on new code |
| **Understanding** (25%) | Reflections, decisions | Weekly retros |
| **Consistency** (20%) | Regular progress | 4-5 days/week |

### Score Interpretation

| Score | Status | What to Do |
|-------|--------|------------|
| 90-100 | Excellent | Consider upgrade to Intermediate |
| 70-89 | On Track | Keep going! |
| 50-69 | Struggling | Consider remediation |
| <50 | At Risk | Remediation recommended |

**How to run**: `python .claude/path-engine/evaluate.py` or `/evaluate`

**Update tracker**: `python .claude/path-engine/report.py` or `/report`

---

## Monthly Curriculum

| Month | Focus | Link |
|-------|-------|------|
| 1 | Python & Environment | [month-01/](month-01/README.md) |
| 2 | Data Fundamentals | [month-02/](month-02/README.md) |
| 3 | Statistics & Probability | [month-03/](month-03/README.md) |
| 4 | Data Visualization | [month-04/](month-04/README.md) |
| 5 | ML Basics | [month-05/](month-05/README.md) |
| 6 | ML Intermediate | [month-06/](month-06/README.md) |
| 7 | Time Series | [month-07/](month-07/README.md) |
| 8 | NLP Basics | [month-08/](month-08/README.md) |
| 9 | Deep Learning Intro | [month-09/](month-09/README.md) |
| 10 | Web Development | [month-10/](month-10/README.md) |
| 11 | Integration Projects | [month-11/](month-11/README.md) |
| 12 | Portfolio & Review | [month-12/](month-12/README.md) |

---

## If You're Stuck

### Step 1: Use `/debug-learning`

```
/debug-learning

I've been stuck on [topic] for [time]. I've tried [approaches].
```

### Step 2: Check Resources

- Skill playbooks: [docs/skills-playbook.md](../../docs/skills-playbook.md)
- Best practices: [.claude/memory/best_practices.md](../../.claude/memory/best_practices.md)

### Step 3: Ask for Help

Describe your problem clearly:
- What you're trying to do
- What you've tried
- Where you're stuck

### Step 4: Take a Break

Sometimes stepping away helps. Come back fresh.

---

## Upgrade/Downgrade Rules

### Upgrade to Intermediate

**Trigger**: Score ≥ 90 for 2+ consecutive evaluations

**Requirements**:
- Consistent high performance
- Strong understanding demonstrated
- Ready for Tier 2 content

**Process**:
1. System proposes upgrade
2. You approve
3. Takes effect at next month boundary

### Downgrade from Intermediate

**Trigger**: Score < 50 for 2+ consecutive evaluations

**Requirements**:
- Struggling with current pace
- Need more foundation time

**Process**:
1. System proposes downgrade
2. You approve
3. Takes effect at next month boundary

### Requesting Changes

You can request changes anytime:

```
I'd like to discuss changing my level. I'm [struggling/excelling] because [reason].
```

See [adaptation rules](../../docs/evaluation/adaptation-rules.md) for full details.

---

## Quick Links

### Documentation
- [How to Use](../../docs/how-to-use.md)
- [System Overview](../../docs/system-overview.md)
- [Commands](../../docs/commands.md)
- [Evaluation Rubric](../../docs/evaluation/rubric.md)

### Claude Capabilities
- [.claude/README.md](../../.claude/README.md)
- [Path Engine](../../.claude/path-engine/report.py)
- [Best Practices](../../.claude/memory/best_practices.md)

### Resources
- [Tier 1 Stack](../../stacks/tier-1-beginner.md)
- [All Tiers](../../stacks/tiers.md)

---

## Daily Workflow

```
Morning:
  1. /status - See where you are
  2. Check today's tasks
  3. Start working

During work:
  - Use skill playbooks for guidance
  - Ask Claude for help when stuck
  - Log significant completions

End of day:
  - Note progress in journal
  - Plan tomorrow
```

## Weekly Workflow

```
Monday:
  - /start-week
  - /plan-week
  - Set goals for the week

Tuesday-Thursday:
  - Build, learn, iterate
  - Use /ship-mvp, /harden as needed

Friday:
  - /evaluate
  - /retro
  - /report
  - Plan next week
```

---

## Your Progress

**Tracker**: [tracker.md](tracker.md) (auto-generated)
**Journal**: [journal/](journal/README.md)

---

**Ready to start?** Run `/status` to see where you are, then `/plan-week` to plan your first week!
