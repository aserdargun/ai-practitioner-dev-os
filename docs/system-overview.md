# System Overview

Architecture and design of the AI Practitioner Booster 2026 learning system.

---

## Introduction

This learning system operates as a continuous feedback loop that:

1. **Evaluates** your progress using multiple signals
2. **Adapts** your learning path based on performance
3. **Executes** weekly plans with AI assistance

The system is designed to be transparent, adaptable, and learner-centered.

---

## Core Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    LEARNING SYSTEM                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐                │
│  │ EVALUATE│───▶│  ADAPT  │───▶│ EXECUTE │                │
│  │         │    │         │    │         │                │
│  │ Score   │    │ Propose │    │ Work    │                │
│  │ progress│    │ changes │    │ on tasks│                │
│  └────▲────┘    └─────────┘    └────┬────┘                │
│       │                              │                      │
│       └──────────────────────────────┘                      │
│                  (continuous loop)                          │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐  │
│  │                    .claude/                          │  │
│  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐       │  │
│  │  │ agents │ │commands│ │ skills │ │ hooks  │       │  │
│  │  └────────┘ └────────┘ └────────┘ └────────┘       │  │
│  │  ┌────────┐ ┌────────┐ ┌────────────────────┐      │  │
│  │  │ memory │ │  mcp   │ │    path-engine     │      │  │
│  │  └────────┘ └────────┘ └────────────────────┘      │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Components

### 1. Agents (`.claude/agents/`)

Specialized AI roles that handle different aspects of the learning experience.

| Agent | Responsibility |
|-------|---------------|
| **Planner** | Creates weekly plans, sequences tasks |
| **Builder** | Writes code, ships features |
| **Reviewer** | Reviews code quality, suggests improvements |
| **Evaluator** | Scores progress, identifies gaps |
| **Coach** | Provides guidance, runs retrospectives |
| **Researcher** | Finds resources, investigates blockers |

**How it works**: When you invoke a command, Claude adopts the appropriate agent's role and follows its defined responsibilities.

### 2. Commands (`.claude/commands/`)

User-facing interface for interacting with the system.

```
User Request ──▶ Command Router ──▶ Agent ──▶ Action ──▶ Output
                      │
                      ▼
               catalog.md
            (source of truth)
```

Commands are documented in `catalog.md` with:
- Description
- Primary agent
- Input requirements
- Output artifacts
- Examples

### 3. Skills (`.claude/skills/`)

Reusable playbooks for common tasks.

| Skill | Use Case |
|-------|----------|
| **EDA to Insight** | Exploratory data analysis workflow |
| **Shipping APIs** | FastAPI service development |
| **RAG + Evals** | RAG system with evaluation |

Skills provide step-by-step guidance that can be referenced by any agent.

### 4. Hooks (`.claude/hooks/`)

Automation scripts triggered at specific points:

| Hook | Trigger | Purpose |
|------|---------|---------|
| `pre_week_start.sh` | `/start-week` | Environment validation |
| `post_week_review.sh` | `/retro` | Collect metrics |
| `pre_publish_check.sh` | `/publish` | Quality gates |

### 5. Memory (`.claude/memory/`)

Persistent storage for learning state.

```
memory/
├── learner_profile.json   # Configuration (read-mostly)
├── progress_log.jsonl     # Activity log (append-only)
├── decisions.jsonl        # Adaptation history (append-only)
└── best_practices.md      # Learnings (append-only)
```

**Key principle**: Memory files follow append-only discipline to maintain history integrity.

### 6. MCP (`.claude/mcp/`)

Model Context Protocol integrations for tool extensions.

- `tool_contracts.md` — Tool specifications
- `example_server.py` — Server implementation
- `example_client.py` — Client implementation

### 7. Path Engine (`.claude/path-engine/`)

Core logic for the evaluate-adapt-execute loop.

| Script | Function |
|--------|----------|
| `evaluate.py` | Read signals, compute scores |
| `adapt.py` | Propose path mutations |
| `report.py` | Generate reports, update tracker |

---

## Data Flow

### Evaluation Flow

```
┌─────────────────┐
│  Memory Files   │
│                 │
│ • progress_log  │
│ • profile       │
│ • best_practices│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Repo Signals  │
│                 │
│ • git commits   │
│ • test results  │
│ • file changes  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   evaluate.py   │
│                 │
│ Calculate scores│
│ per dimension   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Evaluation      │
│ Report          │
│                 │
│ • scores        │
│ • status        │
│ • recommendations│
└─────────────────┘
```

### Adaptation Flow

```
┌─────────────────┐
│   Evaluation    │
│   Result        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    adapt.py     │
│                 │
│ Check thresholds│
│ Apply rules     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Mutations     │
│                 │
│ • level_change  │
│ • month_reorder │
│ • remediation   │
│ • project_swap  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Approval      │
│                 │
│ Auto or Manual  │
└─────────────────┘
```

---

## Design Principles

### 1. Transparency

Everything is visible and documented:
- All scoring logic is in Python (no black boxes)
- Memory files are human-readable
- Adaptations are proposed, not forced

### 2. Learner Control

The system proposes, you decide:
- Manual approval for significant changes
- Can override any suggestion
- Profile is customizable

### 3. Continuous Improvement

The loop runs continuously:
- Weekly evaluations
- Frequent feedback
- Incremental adaptations

### 4. Simplicity

Built with constraints:
- Python stdlib only (no complex dependencies)
- Markdown for documentation
- JSON for structured data

---

## File Organization

```
ai-practitioner-dev-os/
├── .claude/                 # AI system components
│   ├── agents/              # Agent definitions
│   ├── commands/            # Command catalog
│   ├── skills/              # Skill playbooks
│   ├── hooks/               # Automation scripts
│   ├── memory/              # Learning state
│   ├── mcp/                 # Tool integrations
│   └── path-engine/         # Core logic
├── docs/                    # Documentation
├── stacks/                  # Technology tiers
├── paths/                   # Learning paths
│   └── Advanced/            # Your path
│       ├── month-01/        # Monthly modules
│       ├── journal/         # Weekly journals
│       └── tracker.md       # Progress tracker
├── templates/               # Project templates
├── examples/                # Example code
└── .github/                 # CI/CD
```

---

## Integration Points

### Claude Code Integration

Claude Code reads:
- `CLAUDE.md` for repository guidance
- `.claude/commands/catalog.md` for available commands
- `.claude/agents/` for role definitions
- `.claude/memory/` for context

### CI/CD Integration

GitHub Actions:
- Runs on PR and push
- Lints with ruff
- Tests with pytest

### Local Development

Works with:
- Any Python 3.11+ environment
- VS Code recommended
- Works on Linux, macOS, Windows (with WSL)

---

## Security Considerations

### Data Privacy

- All data stays in your repository
- No external services required
- Memory files are local

### Code Safety

- Hooks are shell scripts you can review
- Python scripts use stdlib only
- No arbitrary code execution

### Git Safety

- Pre-commit hooks for quality
- No force pushes in workflows
- History preserved
