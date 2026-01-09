# System Overview

How the AI Practitioner learning system works end-to-end.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        LEARNER (YOU)                            │
│                                                                 │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐           │
│   │ Plan    │→│ Build   │→│ Review  │→│ Reflect │           │
│   └─────────┘  └─────────┘  └─────────┘  └─────────┘           │
│        ↑                                       │                │
│        └───────────── APPROVE ←────────────────┘                │
└─────────────────────────────────────────────────────────────────┘
        ↑                                       │
        │         ┌───────────────────┐         │
        │         │   CLAUDE CODE     │         │
        │         │                   │         │
        │    ┌────┴────┐         ┌────┴────┐    │
        │    │ Agents  │         │Commands │    │
        │    └────┬────┘         └────┬────┘    │
        │         │                   │         │
        │    ┌────┴────┐         ┌────┴────┐    │
        │    │ Skills  │         │ Hooks   │    │
        │    └────┬────┘         └────┬────┘    │
        │         │                   │         │
        │         └───────┬───────────┘         │
        │                 │                     │
        │         ┌───────┴───────┐             │
        │         │    Memory     │             │
        │         │   (source of  │             │
        │         │    truth)     │             │
        │         └───────┬───────┘             │
        │                 │                     │
        │         ┌───────┴───────┐             │
        │         │  Path Engine  │             │
        │         │  evaluate.py  │             │
        │         │  adapt.py     │─────────────┘
        │         │  report.py    │
        │         └───────────────┘
        │                 │
        └─────────────────┘
            PROPOSALS
         (require approval)
```

## Core Loop

### 1. Execute
You work on month projects, complete deliverables, and write reflections.

### 2. Log
Progress is recorded in `.claude/memory/` files (with your approval).

### 3. Evaluate
`evaluate.py` reads memory and signals, computes scores.

### 4. Adapt
`adapt.py` proposes changes based on evaluation (you approve).

### 5. Report
`report.py` updates the tracker for visibility.

---

## Components

### .claude/ Directory

All Claude capabilities live under `.claude/`:

```
.claude/
├── README.md              # Overview
├── agents/                # AI advisor definitions
│   ├── planner.md
│   ├── builder.md
│   ├── reviewer.md
│   ├── evaluator.md
│   ├── coach.md
│   └── researcher.md
├── commands/              # Slash command specs
│   ├── catalog.md
│   ├── status.md
│   ├── plan-week.md
│   └── ...
├── skills/                # Reusable playbooks
│   ├── eda-to-insight.md
│   ├── rag-with-evals.md
│   └── ...
├── hooks/                 # Automation scripts
│   ├── pre_week_start.sh
│   ├── post_week_review.sh
│   └── pre_publish_check.sh
├── memory/                # Learning state
│   ├── learner_profile.json
│   ├── progress_log.jsonl
│   ├── decisions.jsonl
│   └── best_practices.md
├── mcp/                   # Tool contracts
│   ├── tool-contracts.md
│   ├── safety.md
│   └── server_stub/
└── path-engine/           # Evaluation logic
    ├── evaluate.py
    ├── adapt.py
    └── report.py
```

See [.claude/README.md](../.claude/README.md) for detailed documentation.

### Agents

Six specialized AI advisors:

| Agent | Role | Key Responsibility |
|-------|------|-------------------|
| **Planner** | Project Manager | Creates plans, breaks down tasks |
| **Builder** | Engineer | Implements features, writes code |
| **Reviewer** | QA | Reviews code, identifies issues |
| **Evaluator** | Assessor | Scores progress, measures outcomes |
| **Coach** | Mentor | Provides guidance, motivation |
| **Researcher** | Information Gatherer | Finds docs, examples, context |

All agents follow the human-in-the-loop principle: they recommend, you decide.

### Commands

Slash commands invoke specific workflows:

| Category | Commands |
|----------|----------|
| Planning | `/status`, `/plan-week`, `/start-week` |
| Building | `/ship-mvp`, `/harden`, `/publish` |
| Reflection | `/retro`, `/evaluate` |
| Adaptation | `/adapt-path`, `/add-best-practice`, `/debug-learning` |

See [commands.md](commands.md) for full reference.

### Memory System

Append-only files that record your journey:

| File | Content |
|------|---------|
| `learner_profile.json` | Your config (level, goals, constraints) |
| `progress_log.jsonl` | Event stream (milestones, completions) |
| `decisions.jsonl` | Important choices made |
| `best_practices.md` | Accumulated learnings |

**Important**: Memory files are the source of truth. `tracker.md` is derived.

### Path Engine

Python scripts for evaluation and adaptation:

```bash
# Compute scores
python .claude/path-engine/evaluate.py

# Generate proposals (user approves)
python .claude/path-engine/adapt.py

# Update tracker
python .claude/path-engine/report.py
```

---

## Data Flow

### Reading

```
Claude reads:
├── .claude/memory/learner_profile.json  (your config)
├── .claude/memory/progress_log.jsonl    (your events)
├── .claude/memory/decisions.jsonl       (your decisions)
├── paths/intermediate/month-XX/         (curriculum)
└── your code and project files
```

### Writing (requires approval)

```
Claude proposes writes to:
├── .claude/memory/progress_log.jsonl    (new events)
├── .claude/memory/decisions.jsonl       (new decisions)
├── .claude/memory/best_practices.md     (new learnings)
└── paths/intermediate/tracker.md        (derived report)
```

---

## Human-in-the-Loop

### Principle

No changes happen without explicit approval.

### Implementation

1. **Memory Updates**: Claude shows proposed entry → you approve → write happens
2. **Adaptations**: adapt.py outputs proposals → you approve each one → changes applied
3. **Code Changes**: Builder proposes → you review → you approve → applied
4. **Path Changes**: Only at your request, only with your approval

### Verification

- All memory files are human-readable
- You can edit memory directly
- adapt.py never auto-applies
- Tracker is regeneratable from memory

---

## Tier System

### Cumulative Scope

| Level | Tiers | Technologies |
|-------|-------|--------------|
| Beginner | Tier 1 | 53 items |
| **Intermediate** | Tier 1 + 2 | **148 items** |
| Advanced | All | 175 items |

### Intermediate Focus

As an Intermediate learner, you work with:
- **Tier 1**: Foundation (Python, SQL, basic ML, etc.)
- **Tier 2**: Shipping (FastAPI, Docker, cloud basics, LLM frameworks, etc.)

See [../stacks/tiers.md](../stacks/tiers.md) for full list.

---

## Allowed Adaptations

The system can only propose these changes:

| Adaptation | Description | When |
|------------|-------------|------|
| Level Change | Beginner ↔ Intermediate ↔ Advanced | Consistent over/under performance |
| Month Reorder | Swap upcoming months | Better prerequisite ordering |
| Remediation | Insert 1-week review | Struggling with concepts |
| Project Swap | Replace with equivalent | Better fit for goals |

These are enforced in [evaluation/adaptation-rules.md](evaluation/adaptation-rules.md).

---

## Getting Help

### Commands
- `/status` — Quick orientation
- `/debug-learning` — When stuck

### Documentation
- [how-to-use.md](how-to-use.md) — Daily/weekly workflow
- [commands.md](commands.md) — Command reference
- [agents.md](agents.md) — Agent capabilities

### Memory
- Review `.claude/memory/best_practices.md` for past learnings
- Check `decisions.jsonl` for context on past choices

---

## Related Documentation

- [.claude/README.md](../.claude/README.md) — Claude capabilities root
- [how-to-use.md](how-to-use.md) — User workflow guide
- [evaluation/rubric.md](evaluation/rubric.md) — Scoring details
- [../paths/intermediate/README.md](../paths/intermediate/README.md) — Your dashboard
