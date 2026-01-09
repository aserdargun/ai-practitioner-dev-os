# .claude/ — Claude Capabilities

This folder contains all AI-assisted features that power the learning operating system.

## Overview

```
.claude/
├── agents/          # AI advisor role definitions
├── commands/        # Slash command specifications
├── skills/          # Reusable workflow playbooks
├── hooks/           # Automation scripts
├── memory/          # Learning state storage
├── mcp/             # Model Context Protocol tools
└── path-engine/     # Evaluation and adaptation logic
```

## Components

### Agents (`agents/`)

Six specialized AI advisors, each with defined responsibilities:

| Agent | Role |
|-------|------|
| **Planner** | Suggests plans; you approve before execution |
| **Builder** | Proposes implementations; you review and approve |
| **Reviewer** | Provides feedback; you decide what to act on |
| **Evaluator** | Generates assessments; you validate results |
| **Coach** | Offers guidance; you choose which advice to follow |
| **Researcher** | Gathers information; you direct research focus |

All agents follow the **human-in-the-loop** principle: they recommend, you decide.

### Commands (`commands/`)

Slash commands you can invoke in Claude Code:

- `/status` — Current progress snapshot
- `/plan-week` — Generate weekly plan
- `/start-week` — Begin week with setup
- `/ship-mvp` — MVP completion checklist
- `/harden` — Code quality focus
- `/publish` — Demo and write-up prep
- `/retro` — Weekly retrospective
- `/evaluate` — Performance assessment
- `/adapt-path` — Request path change
- `/add-best-practice` — Document a learning
- `/debug-learning` — Troubleshoot blockers

See [catalog.md](commands/catalog.md) for full reference.

### Skills (`skills/`)

Reusable playbooks for common AI/ML tasks:

- EDA to Insight
- Baseline Model and Card
- Experiment Planning
- Forecasting Checklist
- RAG with Evals
- API Shipping Checklist
- Observability Starter
- K8s Deploy Checklist (Advanced only)

Each skill defines: trigger conditions, step-by-step process, artifacts produced, and quality bar.

### Hooks (`hooks/`)

Shell scripts that automate workflow events:

- `pre_week_start.sh` — Creates week plan stub, updates tracker
- `post_week_review.sh` — Prompts retrospective, updates progress log
- `pre_publish_check.sh` — Runs tests, lints, checks docs links

### Memory (`memory/`)

Your learning state, stored as append-only files:

- `learner_profile.json` — Goals, constraints, schedule
- `progress_log.jsonl` — Timestamped events
- `decisions.jsonl` — Important decisions made
- `best_practices.md` — Living document of learnings

**Important**: Claude proposes memory updates; you approve before any write.

### MCP (`mcp/`)

Model Context Protocol definitions for tool safety:

- Tool contracts and schemas
- Usage examples
- Safety guidelines
- Server stub implementation
- Client examples

### Path Engine (`path-engine/`)

Python scripts for evaluation and adaptation:

```bash
# Compute performance scores
python .claude/path-engine/evaluate.py

# Generate adaptation proposals (you approve)
python .claude/path-engine/adapt.py

# Update tracker report
python .claude/path-engine/report.py
```

## Human-in-the-Loop Workflow

```
┌──────────────────────────────────────────────┐
│                                              │
│  Claude Reads Memory → Analyzes Progress     │
│              ↓                               │
│  Claude Generates Recommendations            │
│              ↓                               │
│  YOU REVIEW AND APPROVE/REJECT               │
│              ↓                               │
│  Only Approved Changes Are Applied           │
│                                              │
└──────────────────────────────────────────────┘
```

No files are modified, no paths are changed, no levels are adjusted without your explicit approval.

## Related Documentation

- [docs/system-overview.md](../docs/system-overview.md) — End-to-end system explanation
- [docs/commands.md](../docs/commands.md) — Command usage guide
- [docs/agents.md](../docs/agents.md) — Agent invocation guide
- [docs/memory-system.md](../docs/memory-system.md) — Memory management guide
