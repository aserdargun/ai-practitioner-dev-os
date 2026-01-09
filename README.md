# ai-practitioner-dev-os

**AI Practitioner Booster 2026 — AI-driven, project-based learning system**

An intelligent learning operating system that guides you through a comprehensive AI/ML curriculum with personalized pacing, continuous evaluation, and adaptive recommendations.

---

## What Is This?

This repository is your **personal AI learning environment** that:
- Provides a structured 12-month curriculum tailored to your level
- Uses Claude as an AI assistant to help plan, build, review, and evaluate your work
- Tracks your progress and adapts recommendations based on your performance
- Emphasizes **human-in-the-loop** decision making — you always approve changes

**Current Learner Level: Intermediate**

Your dashboard: [paths/intermediate/README.md](paths/intermediate/README.md)

---

## How to Use (From Zero)

### Initial Setup

1. **Fork this repository** to your GitHub account
2. **Connect Claude Code** to your forked repository
3. **Run the generator** (if starting fresh): Copy the prompt from [SETUP.md](SETUP.md) and paste into Claude Code
4. **Clone your repository** to your local development environment
5. **Recommended IDE**: VS Code with Python extensions

### Quick Verification

```bash
# Verify your setup
python .claude/path-engine/evaluate.py
python .claude/path-engine/report.py
```

---

## Quickstart (5 Minutes)

Run your first learning cycle:

```bash
# 1. Check your current status
# In Claude Code, type:
/status

# 2. Plan your week
/plan-week

# 3. Run evaluation
python .claude/path-engine/evaluate.py

# 4. Generate your progress report
python .claude/path-engine/report.py
```

The system will show you:
- Where you are in the curriculum
- What to focus on this week
- How you're performing
- Recommended adaptations (which you approve before applying)

---

## The AI-Assisted Loop

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│    EVALUATE  →  RECOMMEND  →  USER APPROVES  →  EXECUTE    │
│        ↑                                            │       │
│        └────────────────────────────────────────────┘       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Critical principle**: No changes happen without your explicit approval.

1. **Evaluate**: System analyzes your progress, commits, and reflections
2. **Recommend**: Claude proposes adaptations (level change, project swap, remediation)
3. **User Approves**: You review and explicitly approve or reject each proposal
4. **Execute**: Only approved changes are applied

---

## Daily Workflow

| Time | Action |
|------|--------|
| Start | `/status` — see today's focus |
| Work | Build, code, experiment on your project |
| End | Log progress in `paths/intermediate/journal/` |

## Weekly Workflow

| Week | Focus |
|------|-------|
| **Week 1** | Learn concepts, set up project structure |
| **Week 2** | Build MVP, implement core features |
| **Week 3** | Harden — tests, docs, edge cases |
| **Week 4** | Ship — demo, write-up, retrospective |

**Weekly Commands**:
```
/plan-week    # Start of week
/ship-mvp     # Mid-week checkpoint
/harden       # Week 3 focus
/retro        # End of week reflection
/evaluate     # Get performance assessment
```

---

## Asking Claude for Help

Use slash commands to invoke Claude's capabilities:

| Command | Purpose |
|---------|---------|
| `/status` | Current progress and next steps |
| `/plan-week` | Generate weekly plan |
| `/start-week` | Begin a new week with setup |
| `/ship-mvp` | Checklist for MVP completion |
| `/harden` | Code quality and testing focus |
| `/publish` | Prepare demo and write-up |
| `/retro` | Weekly retrospective |
| `/evaluate` | Performance assessment |
| `/adapt-path` | Request path adaptation |
| `/add-best-practice` | Document a learning |
| `/debug-learning` | Troubleshoot blockers |

Full command reference: [docs/commands.md](docs/commands.md)

---

## Where Claude Capabilities Live

All AI-assisted features are in the `.claude/` folder:

```
.claude/
├── agents/          # AI advisor roles (Planner, Builder, Reviewer, etc.)
├── commands/        # Slash command definitions
├── skills/          # Reusable playbooks (EDA, RAG, API shipping, etc.)
├── hooks/           # Automation scripts for workflow events
├── memory/          # Your learning profile, progress, and decisions
├── mcp/             # Model Context Protocol tools and safety
└── path-engine/     # Evaluation and adaptation logic
```

Learn more: [.claude/README.md](.claude/README.md)

---

## Repository Structure

```
/
├── README.md                    # You are here
├── CLAUDE.md                    # Instructions for Claude Code
├── SETUP.md                     # Generator prompt (canonical source)
├── STACK.md                     # Technology stack reference
│
├── .claude/                     # Claude capabilities
│   ├── agents/                  # AI advisor definitions
│   ├── commands/                # Slash commands
│   ├── skills/                  # Reusable playbooks
│   ├── hooks/                   # Workflow automation
│   ├── memory/                  # Learning state
│   ├── mcp/                     # Tool contracts
│   └── path-engine/             # Evaluation logic
│
├── docs/                        # System documentation
│   ├── how-to-use.md
│   ├── system-overview.md
│   ├── evaluation/              # Rubric, scoring, adaptation rules
│   └── publishing/              # Demo and write-up guides
│
├── stacks/                      # Technology tier definitions
│   ├── tiers.md
│   ├── tier-1-beginner.md
│   ├── tier-2-intermediate.md
│   └── tier-3-advanced.md
│
├── paths/intermediate/          # Your learning dashboard
│   ├── README.md                # Main dashboard
│   ├── tracker.md               # Progress tracker
│   ├── journal/                 # Weekly/monthly reflections
│   └── month-01..12/            # 12-month curriculum
│
├── templates/                   # Starter project templates
│   ├── template-fastapi-service/
│   ├── template-data-pipeline/
│   ├── template-rag-service/
│   └── template-eval-harness/
│
├── examples/                    # Reference implementations
│   └── mini-example/
│
└── .github/                     # GitHub templates and CI
    ├── ISSUE_TEMPLATE/
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/ci.yml
```

---

## Key Links

- **Your Dashboard**: [paths/intermediate/README.md](paths/intermediate/README.md)
- **How to Use**: [docs/how-to-use.md](docs/how-to-use.md)
- **Commands Reference**: [docs/commands.md](docs/commands.md)
- **Evaluation Rubric**: [docs/evaluation/rubric.md](docs/evaluation/rubric.md)
- **Generator Prompt**: [SETUP.md](SETUP.md) (canonical source — do not duplicate)

---

## Getting Help

- Use `/debug-learning` when stuck
- Check [docs/how-to-use.md](docs/how-to-use.md) for detailed guidance
- Review your [best practices](.claude/memory/best_practices.md) for past learnings
- Ask Claude: "Help me understand [topic]" or "What should I focus on?"

---

## License

This repository is designed for personal learning. Fork it, customize it, make it yours.

Built with Claude Code — your AI pair programmer for the learning journey.
