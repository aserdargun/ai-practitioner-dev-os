# .claude/ — Claude Code Capabilities

This folder contains all Claude Code capabilities for the AI Practitioner Booster 2026 learning system.

## Overview

The `.claude/` directory is the brain of your learning OS. It contains:

| Folder | Purpose |
|--------|---------|
| `agents/` | AI advisor personas (Planner, Builder, Reviewer, Evaluator, Coach, Researcher) |
| `commands/` | Slash commands you invoke with `/command-name` |
| `skills/` | Reusable playbooks for common tasks (EDA, modeling, RAG, deployment) |
| `hooks/` | Shell scripts that run at lifecycle events (week start, review, publish) |
| `memory/` | Local storage for learner profile, progress, decisions, and best practices |
| `mcp/` | Model Context Protocol tools and server stubs |
| `path-engine/` | Python scripts for evaluation, adaptation, and reporting |

## Human-in-the-Loop Principle

**All Claude capabilities operate in advisory mode.** Claude provides recommendations, suggestions, and proposals — but no changes are applied without your explicit approval.

The workflow is always:
1. **Evaluate** — Claude analyzes your progress and context
2. **Recommend** — Claude proposes actions, changes, or adaptations
3. **You Approve** — You review and decide what to accept
4. **Execute** — Only approved changes are applied

## Quick Start

### Check Your Status
```
/status
```

### Plan Your Week
```
/plan-week
```

### Get Evaluation Scores
```
python .claude/path-engine/evaluate.py
```

### See Adaptation Proposals
```
python .claude/path-engine/adapt.py
```

## Folder Details

### agents/
Six specialized AI personas, each with defined responsibilities and constraints:
- **Planner**: Creates week/month plans, proposes timelines
- **Builder**: Writes code, implements features
- **Reviewer**: Reviews code, provides feedback
- **Evaluator**: Assesses progress, generates scores
- **Coach**: Offers learning guidance, motivation
- **Researcher**: Gathers information, explores topics

### commands/
Slash commands for common workflows:
- `/status` — See current progress snapshot
- `/plan-week` — Generate weekly plan
- `/start-week` — Initialize a new week
- `/ship-mvp` — Finalize MVP deliverables
- `/harden` — Add tests, error handling, docs
- `/publish` — Prepare demo and write-up
- `/retro` — Run retrospective
- `/evaluate` — Get evaluation scores
- `/adapt-path` — See adaptation proposals
- `/add-best-practice` — Capture a learning
- `/debug-learning` — Diagnose learning blockers

### skills/
Detailed playbooks for specific technical tasks:
- EDA to Insight
- Baseline Model and Card
- Experiment Planning
- Forecasting Checklist
- RAG with Evals
- API Shipping Checklist
- Observability Starter
- K8s Deploy Checklist (Advanced only)

### hooks/
Shell scripts for lifecycle automation:
- `pre_week_start.sh` — Prepare week structure
- `post_week_review.sh` — Capture retrospective
- `pre_publish_check.sh` — Validate before publishing

### memory/
Your learning memory store (append-only):
- `learner_profile.json` — Your goals, constraints, schedule
- `progress_log.jsonl` — Timestamped events
- `decisions.jsonl` — Important decisions
- `best_practices.md` — Living doc of learnings

### mcp/
Model Context Protocol integration:
- Tool contracts and schemas
- Safety guidelines
- Server stub for custom tools
- Client examples

### path-engine/
Python scripts for the evaluation loop:
- `evaluate.py` — Compute scores from memory
- `adapt.py` — Propose path adaptations
- `report.py` — Generate tracker report

## Integration with docs/

The `docs/` folder provides human-friendly guides that reference these capabilities:
- `docs/commands.md` → `.claude/commands/`
- `docs/agents.md` → `.claude/agents/`
- `docs/skills-playbook.md` → `.claude/skills/`
- `docs/hooks.md` → `.claude/hooks/`
- `docs/memory-system.md` → `.claude/memory/`
- `docs/evaluation/` → `.claude/path-engine/`

## Extending Claude Capabilities

You can add new commands, skills, or agents by creating new `.md` files in the appropriate folders. Follow the existing file formats as templates.

For custom MCP tools, see `.claude/mcp/server_stub/` for examples.
