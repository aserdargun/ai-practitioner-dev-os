# ai-practitioner-dev-os

**AI Practitioner Booster 2026 — AI-driven, project-based learning system**

A public, forkable GitHub repository that provides a comprehensive 12-month learning path for becoming a production-ready AI practitioner. This system is AI-driven and continuously evolves based on your successes and challenges.

---

## What This Repo Is

This is your **Learning Operating System**—a structured, AI-assisted framework that guides you through mastering AI/ML engineering skills via real projects. The system:

- **Evaluates** your progress through signals and rubrics
- **Adapts** your learning path based on performance
- **Executes** weekly plans with Claude as your AI coach

All Claude capabilities live under the `.claude/` folder, including agents, commands, skills, hooks, memory, and MCP integrations.

---

## How to Use (From Zero)

1. **Fork this repository** to your GitHub account
2. **Connect Claude Code** to your forked repository
3. **Copy the Generator Prompt** from [`SETUP.md`](SETUP.md) and paste it into Claude Code
4. **Claude Code generates** the full repo structure and commits it to your fork
5. **Clone your generated repository** to your local dev environment
6. **Recommended IDE:** VS Code with Python and Jupyter extensions

> **Note:** See [`SETUP.md`](SETUP.md) for the canonical generator prompt. Do not duplicate it here to avoid drift.

---

## Quickstart (5 Minutes)

Run your first AI-driven learning cycle:

```bash
# 1. Check your current status
# In Claude Code, type:
/status

# 2. Generate this week's plan
/plan-week

# 3. Evaluate your progress
/evaluate

# 4. Generate a progress report
/report
```

This completes one loop of the **Evaluate → Adapt → Execute** cycle.

---

## How the AI-Driven Loop Works

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   EVALUATE  │────▶│    ADAPT    │────▶│   EXECUTE   │
│             │     │             │     │             │
│ Read memory │     │ Propose     │     │ Run weekly  │
│ Check signals│    │ mutations   │     │ plan        │
│ Score rubric│     │ Update path │     │ Build & ship│
└─────────────┘     └─────────────┘     └─────────────┘
       ▲                                       │
       └───────────────────────────────────────┘
                    (continuous)
```

1. **Evaluate**: `.claude/path-engine/evaluate.py` reads memory files and repo signals to score your progress
2. **Adapt**: `.claude/path-engine/adapt.py` proposes path modifications (remediation, acceleration, level changes)
3. **Execute**: You work through weekly plans with Claude's guidance, building real projects

---

## Your Learner Dashboard

**Your Level:** Advanced (Tier 1 + Tier 2 + Tier 3)

👉 **[Go to Your Dashboard](paths/Advanced/README.md)** — This is your main control center.

---

## Daily Workflow

1. **Morning standup** with Claude:
   ```
   /status
   ```
2. **Work on tasks** from your weekly plan
3. **Log progress** in your journal (`paths/Advanced/journal/`)
4. **Ask for help** when stuck:
   ```
   /debug-learning
   ```

## Weekly Workflow

| Day | Activity |
|-----|----------|
| **Monday** | `/start-week` — Initialize the week, run `pre_week_start.sh` |
| **Tue–Thu** | Build, code, learn — use `/ship-mvp` when ready |
| **Friday** | `/harden` — Add tests, docs, polish |
| **Weekend** | `/retro` + `/evaluate` — Reflect and assess |

---

## Asking Claude for Help

Use `/commands` to see all available commands:

| Command | Purpose |
|---------|---------|
| `/status` | Check current progress and blockers |
| `/plan-week` | Generate this week's tasks |
| `/start-week` | Begin the week (runs hooks) |
| `/ship-mvp` | Ship minimum viable version |
| `/harden` | Add tests, docs, error handling |
| `/publish` | Prepare for demo/portfolio |
| `/retro` | Weekly retrospective |
| `/evaluate` | Run evaluation scripts |
| `/adapt-path` | Propose path changes |
| `/add-best-practice` | Capture a learning |
| `/debug-learning` | Get unstuck |

See [docs/commands.md](docs/commands.md) for the full guide.

---

## Where Claude Capabilities Live

All AI system components are in the [`.claude/`](.claude/) folder:

```
.claude/
├── agents/          # AI agent definitions (planner, builder, reviewer, etc.)
├── commands/        # Command catalog and routing
├── skills/          # Reusable skill playbooks
├── hooks/           # Automation scripts (pre/post week, publish checks)
├── memory/          # Your learning profile, progress logs, decisions
├── mcp/             # Tool contracts and integrations
└── path-engine/     # Evaluation and adaptation scripts
```

See [.claude/README.md](.claude/README.md) for details.

---

## Key Documentation

- [How to Use](docs/how-to-use.md) — Complete usage guide
- [System Overview](docs/system-overview.md) — Architecture explanation
- [Evaluation Rubric](docs/evaluation/rubric.md) — How you're assessed
- [Skills Playbook](docs/skills-playbook.md) — Reusable skill guides
- [Memory System](docs/memory-system.md) — How learning state is tracked

---

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

---

**Ready to start?** Go to your [Learner Dashboard](paths/Advanced/README.md) and begin your journey!
