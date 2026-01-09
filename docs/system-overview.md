# System Overview

The AI Practitioner Learning OS is an AI-assisted, project-based learning system for 2026.

## What This Is

A self-contained learning environment that:
- Guides you through a 12-month AI/ML curriculum
- Tracks your progress automatically
- Evaluates and adapts to your performance
- Keeps all decisions and learnings in the repo

## Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                         Learning OS                             │
├────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │   Learner    │───>│    Claude    │───>│   Actions    │      │
│  │   (You)      │<───│   Agents     │<───│   (Repo)     │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
│         │                   │                   │                │
│         │                   │                   │                │
│         v                   v                   v                │
│  ┌────────────────────────────────────────────────────────┐    │
│  │                    Memory System                        │    │
│  │  (progress_log, decisions, best_practices, profile)    │    │
│  └────────────────────────────────────────────────────────┘    │
│         │                                                        │
│         v                                                        │
│  ┌────────────────────────────────────────────────────────┐    │
│  │                    Path Engine                          │    │
│  │  (evaluate.py → adapt.py → report.py)                  │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
└────────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. Agents (`.claude/agents/`)

Advisory roles that help you learn:

| Agent | Role |
|-------|------|
| Planner | Plans weeks and schedules |
| Builder | Implements code and features |
| Reviewer | Reviews quality and security |
| Evaluator | Assesses progress and proposes adaptations |
| Coach | Helps when stuck |
| Researcher | Gathers information |

See [agents.md](agents.md) for details.

### 2. Commands (`.claude/commands/`)

Shortcuts for common actions:

| Command | Purpose |
|---------|---------|
| `/status` | Check progress |
| `/plan-week` | Plan the week |
| `/evaluate` | Assess progress |
| `/adapt-path` | Get recommendations |

See [commands.md](commands.md) for the full catalog.

### 3. Skills (`.claude/skills/`)

Playbooks for common tasks:
- EDA to Insight
- Baseline Model
- RAG with Evals
- API Shipping

See [skills-playbook.md](skills-playbook.md) for details.

### 4. Hooks (`.claude/hooks/`)

Automation scripts:
- `pre_week_start.sh` - Week initialization
- `post_week_review.sh` - Week wrap-up
- `pre_publish_check.sh` - Quality gates

See [hooks.md](hooks.md) for details.

### 5. Memory System (`.claude/memory/`)

Your learning record:
- `learner_profile.json` - Goals, constraints
- `progress_log.jsonl` - Event history
- `decisions.jsonl` - Important choices
- `best_practices.md` - Learned patterns

See [memory-system.md](memory-system.md) for details.

### 6. Path Engine (`.claude/path-engine/`)

The evaluation loop:
- `evaluate.py` - Compute scores
- `adapt.py` - Propose changes
- `report.py` - Update tracker

See [.claude/path-engine/README.md](../.claude/path-engine/README.md) for details.

## The End-to-End Loop

### 1. Evaluate

```bash
python .claude/path-engine/evaluate.py
```

Reads memory + repo signals → Computes scores → Outputs report.

### 2. Present Recommendations

Based on scores, the system proposes:
- Level changes
- Month reordering
- Remediation weeks
- Project swaps

### 3. User Approves

**Critical**: You review every proposal. Nothing changes automatically.

### 4. Execute Approved Changes

Only after your explicit approval:
- Update configuration files
- Adjust schedules
- Log the decision

## Human-in-the-Loop Requirement

This is not an autonomous system. It's an assistant.

| Action | Who Decides |
|--------|-------------|
| What to learn | You |
| How to structure weeks | Claude suggests, you approve |
| Code implementation | Claude proposes, you review |
| Path adaptations | Claude analyzes, you decide |
| All file writes | Require your confirmation |

## Tier System

Technologies are organized into tiers:

| Tier | Level | Focus |
|------|-------|-------|
| 1 | Beginner | Foundation (53 items) |
| 2 | Intermediate | Shipping (95 items) |
| 3 | Advanced | Scale & Performance (27 items) |

As an Advanced learner, you have access to all tiers (175 items).

## Monthly Structure

Each month has:
- Learning goals (from tier stack)
- Main project with deliverables
- Definition of Done checklist
- Stretch goals
- Claude prompts for guidance

See `paths/advanced/month-XX/README.md` for each month.

## Directory Structure

```
/
├── .claude/           # Claude capabilities (core)
│   ├── agents/        # Agent definitions
│   ├── commands/      # Command definitions
│   ├── skills/        # Skill playbooks
│   ├── hooks/         # Automation scripts
│   ├── memory/        # Learning memory
│   ├── mcp/           # Tool contracts
│   └── path-engine/   # Evaluation scripts
├── docs/              # Documentation
├── paths/advanced/    # Your learning path
├── stacks/            # Tier definitions
├── templates/         # Project templates
├── examples/          # Worked examples
└── .github/           # CI/CD
```

## Getting Started

1. Open dashboard: `paths/advanced/README.md`
2. Review current month: `paths/advanced/month-01/README.md`
3. Run `/status` to check position
4. Run `/plan-week` to create week plan
5. Start building!

## Further Reading

- [How to Use](how-to-use.md) - Daily/weekly workflows
- [Commands](commands.md) - Command reference
- [Evaluation](evaluation/rubric.md) - Scoring details
- [Claude README](../.claude/README.md) - Capabilities deep-dive
