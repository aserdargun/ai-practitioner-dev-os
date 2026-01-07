# ai-practitioner-dev-os

**AI Practitioner Booster 2026 — AI-driven, project-based learning system**

A public, forkable GitHub repository that provides a complete 12-month AI/ML learning curriculum with built-in evaluation, adaptation, and coaching powered by Claude.

---

## What This Repo Is

This is a **Learning Operating System** for AI practitioners. It combines:

- **Structured curriculum**: 12 months of projects organized by skill tiers
- **AI-driven coaching**: Claude agents that plan, build, review, evaluate, and coach
- **Adaptive learning**: Automatic path adjustments based on your progress
- **Memory system**: Persistent tracking of goals, progress, and best practices
- **Real templates**: Production-ready starter code for common AI/ML patterns

**Current Learner Level: Beginner** (Tier 1 only in 2026)

---

## How to Use (From Zero)

1. **Fork this repository** to your GitHub account
2. **Connect Claude Code** to your forked repository
3. **Open [SETUP.md](SETUP.md)**, copy the "Repository Generator Prompt" block, and paste it into Claude Code
4. **Claude Code generates** the full repo structure and commits it to your fork
5. **Clone your generated repository** to your local dev environment
6. **Recommended IDE**: VS Code with Python and Jupyter extensions

---

## Quickstart (5 Minutes)

Run your first learning cycle in Claude Code:

```
# 1. Check your current status
/status

# 2. Plan your week
/plan-week

# 3. Run evaluation
/evaluate

# 4. Generate your progress report
/report
```

Or run the path-engine scripts directly:

```bash
python .claude/path-engine/evaluate.py
python .claude/path-engine/adapt.py
python .claude/path-engine/report.py
```

---

## How the AI-Driven Loop Works

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  EVALUATE   │ ──► │    ADAPT    │ ──► │   EXECUTE   │
│             │     │             │     │             │
│ Check your  │     │ Adjust your │     │ Work on     │
│ progress &  │     │ path based  │     │ projects &  │
│ scores      │     │ on results  │     │ learning    │
└─────────────┘     └─────────────┘     └─────────────┘
       ▲                                       │
       └───────────────────────────────────────┘
```

1. **Evaluate**: The system reads your memory files and repo signals to score progress
2. **Adapt**: Based on scores, it proposes modifications (remediation, acceleration, project swaps)
3. **Execute**: You work through the adapted plan with Claude's help

---

## Your Learning Dashboard

**Current Level: Beginner**

👉 **[Go to Your Dashboard](paths/Beginner/README.md)** 👈

Your dashboard contains:
- Current month and weekly checklists
- Commands cheat-sheet
- Evaluation snapshots
- "If you're stuck" playbook
- Upgrade/downgrade rules

---

## Daily Workflow

1. Open your dashboard: `paths/Beginner/README.md`
2. Check today's tasks in your week plan
3. Use `/status` to see where you are
4. Work on your project with Claude's help
5. Log progress in your journal

## Weekly Workflow

| Day | Activity |
|-----|----------|
| **Monday** | Run `/plan-week`, set goals |
| **Tue-Thu** | Build, learn, iterate |
| **Friday** | Run `/evaluate`, reflect |
| **Weekend** | Optional: publish, write-up |

---

## How to Ask Claude for Help

Use commands to invoke Claude's capabilities:

| Command | What It Does |
|---------|--------------|
| `/status` | Check current progress and blockers |
| `/plan-week` | Generate this week's learning plan |
| `/start-week` | Initialize week with pre-flight checks |
| `/ship-mvp` | Guide you through shipping a minimal viable product |
| `/harden` | Add tests, error handling, documentation |
| `/publish` | Prepare your work for demo and write-up |
| `/retro` | Run a retrospective on your week |
| `/evaluate` | Run the evaluation engine on your progress |
| `/adapt-path` | Propose path modifications based on evaluation |
| `/add-best-practice` | Capture a new best practice |
| `/debug-learning` | Diagnose why you're stuck |
| `/report` | Generate/update your tracker report |

See full command reference: [docs/commands.md](docs/commands.md)

---

## Where Claude Capabilities Live

All Claude-specific configurations live in the `.claude/` folder:

```
.claude/
├── agents/       # Agent definitions (Planner, Builder, Reviewer, etc.)
├── commands/     # Command catalog and routing
├── skills/       # Skill playbooks (EDA, RAG, deployment, etc.)
├── hooks/        # Automation scripts (pre-week, post-review, etc.)
├── memory/       # Your learning state (profile, progress, decisions)
├── mcp/          # Model Context Protocol tools and examples
└── path-engine/  # Evaluation and adaptation scripts
```

See [.claude/README.md](.claude/README.md) for full documentation.

---

## Repository Structure

```
/
├── README.md                 # This file
├── CLAUDE.md                 # Claude Code instructions
├── SETUP.md                  # Generator prompt (canonical source)
├── LICENSE                   # MIT License
├── CODE_OF_CONDUCT.md        # Contributor Covenant
├── CONTRIBUTING.md           # How to contribute
├── SECURITY.md               # Security policy
│
├── .claude/                  # Claude capabilities
│   ├── agents/               # Agent definitions
│   ├── commands/             # Command catalog
│   ├── skills/               # Skill playbooks
│   ├── hooks/                # Automation scripts
│   ├── memory/               # Learning state
│   ├── mcp/                  # MCP tools
│   └── path-engine/          # Evaluation scripts
│
├── docs/                     # Documentation
│   ├── how-to-use.md
│   ├── system-overview.md
│   ├── commands.md
│   ├── agents.md
│   ├── skills-playbook.md
│   ├── hooks.md
│   ├── memory-system.md
│   ├── evaluation/           # Evaluation docs
│   └── publishing/           # Publishing guides
│
├── stacks/                   # Tier definitions
│   ├── tiers.md
│   ├── tier-1-beginner.md
│   ├── tier-2-intermediate.md
│   └── tier-3-advanced.md
│
├── paths/Beginner/           # Your learning path
│   ├── README.md             # Dashboard
│   ├── tracker.md            # Progress tracker
│   ├── journal/              # Weekly/monthly journals
│   └── month-01..12/         # Monthly curriculum
│
├── templates/                # Starter project templates
│   ├── template-fastapi-service/
│   ├── template-data-pipeline/
│   ├── template-rag-service/
│   └── template-eval-harness/
│
├── examples/                 # Example implementations
│   └── mini-example/
│
└── .github/                  # GitHub templates and CI
    ├── ISSUE_TEMPLATE/
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/ci.yml
```

---

## Key Links

- [How to Use This System](docs/how-to-use.md)
- [System Overview](docs/system-overview.md)
- [Tier Definitions](stacks/tiers.md)
- [Evaluation Rubric](docs/evaluation/rubric.md)
- [Best Practices](.claude/memory/best_practices.md)
- [Commands Catalog](.claude/commands/catalog.md)

---

## Generator Prompt

The canonical generator prompt lives in [SETUP.md](SETUP.md). Do not duplicate it here to avoid drift.

---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

**Ready to start?** Go to your [Learning Dashboard](paths/Beginner/README.md) and run `/status`!
