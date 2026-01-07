# System Overview

This document explains the end-to-end architecture of the AI Practitioner Learning OS.

## What This System Is

The AI Practitioner Learning OS is a **self-improving learning system** that:

1. **Guides** you through a structured 12-month curriculum
2. **Evaluates** your progress automatically
3. **Adapts** your path based on performance
4. **Coaches** you when you're stuck

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      LEARNER INTERFACE                          │
│  Dashboard (paths/Beginner/README.md) │ Commands (/status, etc) │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         AGENTS                                   │
│  Planner │ Builder │ Reviewer │ Evaluator │ Coach │ Researcher  │
│                     (.claude/agents/)                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       PATH ENGINE                                │
│           evaluate.py │ adapt.py │ report.py                     │
│                   (.claude/path-engine/)                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      MEMORY SYSTEM                               │
│  learner_profile.json │ progress_log.jsonl │ decisions.jsonl    │
│  best_practices.md                                               │
│                     (.claude/memory/)                            │
└─────────────────────────────────────────────────────────────────┘
```

## The Learning Loop

### 1. Execute

You work on the curriculum:
- Follow month-by-month learning path
- Complete projects and deliverables
- Log progress and reflections

### 2. Evaluate

The system scores your progress:
- Reads memory files
- Checks repo signals (commits, tests)
- Computes scores across categories

### 3. Adapt

Based on scores, the system proposes changes:
- Remediation weeks for struggling areas
- Acceleration for fast learners
- Project swaps for better fit

## Component Deep Dive

### Agents (.claude/agents/)

Six specialized agents handle different aspects:

| Agent | Role | Primary Commands |
|-------|------|------------------|
| **Planner** | Plans and tracks | `/status`, `/plan-week` |
| **Builder** | Implements code | `/ship-mvp`, `/harden` |
| **Reviewer** | Reviews quality | (internal) |
| **Evaluator** | Scores progress | `/evaluate`, `/adapt-path` |
| **Coach** | Guides and helps | `/retro`, `/debug-learning` |
| **Researcher** | Finds resources | (internal) |

See [agents.md](agents.md) for details.

### Commands (.claude/commands/)

Commands are the primary interface:

```
/status          → Planner checks current state
/plan-week       → Planner creates weekly plan
/ship-mvp        → Builder guides implementation
/evaluate        → Evaluator scores progress
/adapt-path      → Evaluator proposes changes
/retro           → Coach facilitates reflection
```

See [commands.md](commands.md) for the full catalog.

### Skills (.claude/skills/)

Step-by-step playbooks for common tasks:

- EDA to Insight
- Baseline Model and Card
- Experiment Planning
- Forecasting
- RAG with Evals
- API Shipping
- Observability

See [skills-playbook.md](skills-playbook.md) for details.

### Hooks (.claude/hooks/)

Automation scripts for key moments:

| Hook | Trigger | Purpose |
|------|---------|---------|
| `pre_week_start.sh` | Monday | Set up the week |
| `post_week_review.sh` | Friday | Reflect and log |
| `pre_publish_check.sh` | Before publish | Quality checks |

See [hooks.md](hooks.md) for details.

### Memory System (.claude/memory/)

Persistent storage for learning state:

| File | Purpose | Update Pattern |
|------|---------|----------------|
| `learner_profile.json` | Goals, constraints | Manual edit |
| `progress_log.jsonl` | Progress events | Append-only |
| `decisions.jsonl` | Important decisions | Append-only |
| `best_practices.md` | Accumulated wisdom | Append |

**Important**: Memory files are append-only sources of truth. The tracker is a derived artifact.

See [memory-system.md](memory-system.md) for details.

### Path Engine (.claude/path-engine/)

Python scripts implementing the evaluation loop:

```bash
python evaluate.py   # Score progress → progress_log.jsonl
python adapt.py      # Propose changes → decisions.jsonl
python report.py     # Update tracker → paths/Beginner/tracker.md
```

See [evaluation/](evaluation/) for rubric and rules.

### MCP (.claude/mcp/)

Model Context Protocol tools for programmatic access:

- `hello` - Test connectivity
- `read_repo_file` - Read files safely
- `write_memory_entry` - Append to memory

See the [MCP README](../.claude/mcp/README.md) for details.

## Curriculum Structure

### Tiers (Skill Levels)

| Tier | Focus | Skills |
|------|-------|--------|
| **Tier 1** | Foundation | Data science, ML basics, Python |
| **Tier 2** | Shipping | MLOps, DevOps, cloud deployment |
| **Tier 3** | Scale | Kubernetes, distributed systems |

### Pacing by Level

| Level | Tiers Covered | Pace |
|-------|---------------|------|
| **Beginner** | Tier 1 only | Foundation year |
| **Intermediate** | Tier 1 + 2 | Ship to production |
| **Advanced** | Tier 1 + 2 + 3 | Production at scale |

See [stacks/tiers.md](../stacks/tiers.md) for full details.

## Data Flow

```
User Action
    │
    ▼
Command (e.g., /evaluate)
    │
    ▼
Agent (Evaluator)
    │
    ├──► Read: .claude/memory/*
    │
    ├──► Process: path-engine/evaluate.py
    │
    ├──► Write: progress_log.jsonl (append)
    │
    └──► Output: Scores and recommendations
```

## Key Principles

### 1. Append-Only Memory

- Never delete or modify history
- Progress log is the source of truth
- Tracker is regenerated from memory

### 2. Allowed Adaptations Only

The system can only propose:
- Level changes (at month boundaries)
- Month reordering
- Remediation weeks
- Project swaps

No arbitrary changes - everything is constrained.

### 3. Learner Agency

- System proposes, learner decides
- All adaptations require consent
- Learner can override recommendations

### 4. Continuous Improvement

- Best practices accumulate over time
- Patterns emerge from progress data
- System gets better at helping you

## Where to Go Next

- [How to Use](how-to-use.md) - Day-to-day operations
- [Commands](commands.md) - Full command reference
- [Evaluation](evaluation/rubric.md) - How scoring works
- [.claude/ README](../.claude/README.md) - Claude capabilities
