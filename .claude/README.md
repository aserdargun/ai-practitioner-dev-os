# .claude/ — Claude Capabilities

This folder contains all Claude Code configurations, agents, commands, skills, hooks, memory, MCP tools, and the path-engine for the AI Practitioner Learning OS.

## Directory Structure

```
.claude/
├── README.md           # This file
├── agents/             # Agent definitions
│   ├── planner.md      # Plans weeks and milestones
│   ├── builder.md      # Implements and ships code
│   ├── reviewer.md     # Reviews code and provides feedback
│   ├── evaluator.md    # Scores progress and proposes adaptations
│   ├── coach.md        # Guides learner, runs retros
│   └── researcher.md   # Explores docs and finds examples
│
├── commands/           # Command catalog
│   ├── README.md
│   └── catalog.md      # Source of truth for all commands
│
├── skills/             # Skill playbooks
│   ├── README.md
│   ├── eda-to-insight.md
│   ├── baseline-model-and-card.md
│   ├── experiment-plan.md
│   ├── forecasting-checklist.md
│   ├── rag-with-evals.md
│   ├── api-shipping-checklist.md
│   ├── observability-starter.md
│   └── k8s-deploy-checklist.md  # Advanced only
│
├── hooks/              # Automation scripts
│   ├── README.md
│   ├── pre_week_start.sh
│   ├── post_week_review.sh
│   └── pre_publish_check.sh
│
├── memory/             # Learning state (append-only)
│   ├── README.md
│   ├── learner_profile.json
│   ├── progress_log.jsonl
│   ├── decisions.jsonl
│   └── best_practices.md
│
├── mcp/                # Model Context Protocol
│   ├── README.md
│   ├── tool-contracts.md
│   ├── examples.md
│   ├── safety.md
│   ├── server_stub/
│   │   ├── README.md
│   │   └── server.py
│   └── client_examples/
│       ├── README.md
│       └── python_client.py
│
└── path-engine/        # Evaluation and adaptation
    ├── README.md
    ├── evaluate.py
    ├── adapt.py
    └── report.py
```

## How It Works

### Agents

Each agent has a specific role in the learning process:

| Agent | Role | Primary Commands |
|-------|------|------------------|
| **Planner** | Plans weeks, tracks milestones | `/status`, `/plan-week`, `/start-week` |
| **Builder** | Implements features, ships code | `/ship-mvp`, `/harden`, `/publish` |
| **Reviewer** | Reviews code, provides feedback | (invoked by Builder) |
| **Evaluator** | Scores progress, adapts path | `/evaluate`, `/adapt-path`, `/report` |
| **Coach** | Guidance, retros, best practices | `/retro`, `/add-best-practice`, `/debug-learning` |
| **Researcher** | Explores docs, finds examples | (invoked by other agents) |

### Commands

Commands are the primary interface for learners. See [commands/catalog.md](commands/catalog.md) for the full reference.

### Skills

Skills are step-by-step playbooks for common tasks. Each skill includes:
- Trigger conditions
- Step-by-step instructions
- Artifacts produced
- Quality bar

### Hooks

Shell scripts that automate common workflows:
- `pre_week_start.sh` - Initialize a new week
- `post_week_review.sh` - End-of-week retrospective
- `pre_publish_check.sh` - Quality checks before publishing

### Memory

The memory system tracks:
- **learner_profile.json** - Goals, constraints, schedule
- **progress_log.jsonl** - Timestamped progress events
- **decisions.jsonl** - Important decisions made
- **best_practices.md** - Accumulated best practices

**Important**: Memory files are append-only. The tracker at `paths/Beginner/tracker.md` is a derived artifact.

### MCP (Model Context Protocol)

Tools for programmatic interaction with the learning system:
- Tool contracts and schemas
- Server stub implementation
- Client examples

### Path Engine

Python scripts (stdlib only) that implement the evaluation loop:
- `evaluate.py` - Reads memory and computes scores
- `adapt.py` - Proposes allowed modifications
- `report.py` - Updates the learner tracker

## Quick Links

- [Agents Documentation](../docs/agents.md)
- [Commands Guide](../docs/commands.md)
- [Skills Playbook](../docs/skills-playbook.md)
- [Hooks Documentation](../docs/hooks.md)
- [Memory System](../docs/memory-system.md)
- [Evaluation Rubric](../docs/evaluation/rubric.md)
