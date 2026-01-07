# CLAUDE.md

This file provides instructions for Claude Code when working with this repository.

## Repository Overview

This is the **AI Practitioner Booster 2026** - an AI-driven, project-based learning system. The current learner level is **Beginner** (Tier 1 curriculum only).

## Key Directories

- `.claude/` - Claude capabilities (agents, commands, skills, hooks, memory, MCP, path-engine)
- `docs/` - Documentation for the learning system
- `stacks/` - Tier definitions and technology stacks
- `paths/Beginner/` - The learner's dashboard and 12-month curriculum
- `templates/` - Starter project templates (FastAPI, data pipeline, RAG, eval harness)
- `examples/` - Example implementations

## Memory System

The memory system lives in `.claude/memory/`:

- `learner_profile.json` - Goals, constraints, schedule
- `progress_log.jsonl` - Timestamped progress events (append-only)
- `decisions.jsonl` - Important decisions made (append-only)
- `best_practices.md` - Living document of best practices

**Important**: Memory files are append-only sources of truth. The tracker at `paths/Beginner/tracker.md` is a derived artifact that can be regenerated.

## Commands

When the user invokes a command, route it to the appropriate handler:

| Command | Handler | Description |
|---------|---------|-------------|
| `/status` | Planner Agent | Check current progress and blockers |
| `/plan-week` | Planner Agent | Generate weekly learning plan |
| `/start-week` | Planner Agent | Initialize week with pre-flight checks |
| `/ship-mvp` | Builder Agent | Guide MVP shipping |
| `/harden` | Builder Agent | Add tests, error handling, docs |
| `/publish` | Builder Agent | Prepare for demo and write-up |
| `/retro` | Coach Agent | Run retrospective |
| `/evaluate` | Evaluator Agent | Run evaluation engine |
| `/adapt-path` | Evaluator Agent | Propose path modifications |
| `/add-best-practice` | Coach Agent | Capture best practice |
| `/debug-learning` | Coach Agent | Diagnose learning blockers |
| `/report` | Evaluator Agent | Generate tracker report |

See `.claude/commands/catalog.md` for full details.

## Agents

Agents are defined in `.claude/agents/`:

- **Planner** - Plans weeks, sets goals, tracks milestones
- **Builder** - Implements features, ships code
- **Reviewer** - Reviews code, provides feedback
- **Evaluator** - Scores progress, proposes adaptations
- **Coach** - Provides guidance, runs retros, captures best practices
- **Researcher** - Explores documentation, finds examples

## Skills

Skill playbooks in `.claude/skills/` provide step-by-step guidance for common tasks:

- `eda-to-insight.md` - Exploratory data analysis
- `baseline-model-and-card.md` - Building baseline models
- `experiment-plan.md` - Planning experiments
- `forecasting-checklist.md` - Time series forecasting
- `rag-with-evals.md` - RAG systems with evaluation
- `api-shipping-checklist.md` - Shipping APIs
- `observability-starter.md` - Adding observability
- `k8s-deploy-checklist.md` - Kubernetes deployment (Advanced only)

## Path Engine

The evaluation and adaptation loop is implemented in `.claude/path-engine/`:

```bash
python .claude/path-engine/evaluate.py   # Score progress
python .claude/path-engine/adapt.py      # Propose modifications
python .claude/path-engine/report.py     # Update tracker
```

## Allowed Adaptations

The system can only make these modifications:

1. **Level change** - Upgrade/downgrade learner level (at month boundaries)
2. **Month reorder** - Swap upcoming month modules
3. **Remediation week** - Insert 1-week remediation block
4. **Project swap** - Replace project with equivalent scope

See `docs/evaluation/adaptation-rules.md` for the full schema.

## Working with This Repo

### When helping the learner:

1. Always check their current progress in `.claude/memory/progress_log.jsonl`
2. Refer to the current month's README in `paths/Beginner/month-XX/`
3. Use skill playbooks for specific tasks
4. Log important events to memory files (append-only)

### When running evaluations:

1. Read all memory files
2. Check repo signals (commits, tests, etc.)
3. Score using the rubric in `docs/evaluation/rubric.md`
4. Propose only allowed adaptations

### Code style:

- Python: Follow PEP 8, use type hints
- Use ruff for linting
- Write tests for new functionality
- Keep dependencies minimal

## Quick Reference

- Dashboard: `paths/Beginner/README.md`
- Commands: `docs/commands.md` or `.claude/commands/catalog.md`
- Evaluation rubric: `docs/evaluation/rubric.md`
- Best practices: `.claude/memory/best_practices.md`
