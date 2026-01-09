# AI Practitioner Dev OS

**AI Practitioner Booster 2026** — an AI-driven, project-based learning OS that evaluates your progress, adapts your curriculum, and keeps your best practices inside the repo.

> **Current Level**: Beginner (Tier 1 Foundation)

---

## What This Repo Is

This is a fully-generated learning system for AI practitioners. It includes:

- **12-month curriculum** tailored to Beginner level (Tier 1 technologies)
- **AI-assisted workflow** with human-in-the-loop approval
- **Evaluation system** that tracks progress and proposes adaptations
- **Project templates** ready to use for hands-on learning
- **Best practices capture** to build your own knowledge base

### The AI-Assisted Loop

```
Evaluate → Recommend → **You Approve** → Execute
```

**Important**: Claude provides suggestions and recommendations. You make all final decisions. No changes to your learning path happen without your explicit approval.

---

## Quick Navigation

| What You Need | Where to Find It |
|---------------|------------------|
| **Your Dashboard** | [paths/beginner/README.md](paths/beginner/README.md) |
| **How to Use** | [docs/how-to-use.md](docs/how-to-use.md) |
| **Commands Reference** | [docs/commands.md](docs/commands.md) |
| **Agents Guide** | [docs/agents.md](docs/agents.md) |
| **Skills Playbook** | [docs/skills-playbook.md](docs/skills-playbook.md) |
| **Evaluation Rubric** | [docs/evaluation/rubric.md](docs/evaluation/rubric.md) |
| **Memory System** | [docs/memory-system.md](docs/memory-system.md) |
| **Claude Capabilities** | [.claude/README.md](.claude/README.md) |

---

## Quickstart (5 Minutes)

### 1. Check Your Status

In Claude Code, run:
```
/status
```

This shows your current month, progress, and next steps.

### 2. Plan Your Week

```
/plan-week
```

Claude will help create a focused plan for the week.

### 3. Run Evaluation

From the command line:
```bash
python .claude/path-engine/evaluate.py
```

This generates scores based on your progress.

### 4. Get Recommendations

```bash
python .claude/path-engine/adapt.py
```

Review proposed adaptations. Accept or reject each one.

### 5. Update Your Tracker

```bash
python .claude/path-engine/report.py
```

Regenerates your progress tracker at `paths/beginner/tracker.md`.

---

## Daily Workflow

```
Morning:
1. Check /status for today's focus
2. Review your week plan

During Work:
3. Use agents for help (Planner, Builder, Researcher)
4. Ship deliverables, write code, learn

Evening:
5. Log progress to .claude/memory/progress_log.jsonl
6. Capture any learnings in best_practices.md
```

## Weekly Workflow

```
Monday:
- /plan-week to set the week's focus
- bash .claude/hooks/pre_week_start.sh

Tuesday-Thursday:
- Execute on your plan
- Use /debug-learning if stuck

Friday:
- /retro to reflect on the week
- bash .claude/hooks/post_week_review.sh
- /evaluate to check progress
- /adapt-path to review any recommended changes
```

---

## Folder Structure

```
ai-practitioner-dev-os/
├── .claude/                    # Claude capabilities
│   ├── agents/                 # AI personas (planner, builder, etc.)
│   ├── commands/               # Slash commands (/status, /plan-week, etc.)
│   ├── skills/                 # Playbooks (EDA, ML, APIs, etc.)
│   ├── hooks/                  # Shell scripts for automation
│   ├── memory/                 # Progress tracking (append-only)
│   ├── mcp/                    # Tool contracts and stubs
│   └── path-engine/            # Evaluation scripts
├── docs/                       # Documentation
│   ├── evaluation/             # Rubrics, scoring, adaptation rules
│   └── publishing/             # How to demo and share your work
├── paths/beginner/             # Your learning dashboard
│   ├── README.md               # Main dashboard
│   ├── tracker.md              # Progress tracker (derived)
│   ├── journal/                # Weekly/monthly reflection templates
│   └── month-01...month-12/    # Monthly curricula
├── stacks/                     # Technology tier definitions
├── templates/                  # Project templates
│   ├── template-fastapi-service/
│   ├── template-data-pipeline/
│   ├── template-rag-service/
│   └── template-eval-harness/
├── examples/                   # Working examples
│   └── mini-example/           # Complete Iris classifier
└── .github/                    # GitHub templates and CI
```

---

## Asking Claude for Help

### Using Commands

Commands are your main interface. Run them in Claude Code:

| Command | Purpose |
|---------|---------|
| `/status` | Check current progress |
| `/plan-week` | Create weekly plan |
| `/start-week` | Begin a new week |
| `/ship-mvp` | Get help shipping deliverables |
| `/harden` | Improve code quality |
| `/publish` | Prepare for portfolio |
| `/retro` | Weekly retrospective |
| `/evaluate` | Run evaluation |
| `/adapt-path` | Review path changes |
| `/debug-learning` | Get unstuck |

### Using Agents

Ask agents directly in conversation:

```
Ask the Planner to help me scope this week's work.
```

```
Ask the Builder to help me implement a REST API endpoint.
```

```
Ask the Reviewer to check my code for issues.
```

```
Ask the Researcher to explain how TF-IDF works.
```

See [docs/agents.md](docs/agents.md) for full agent descriptions.

---

## The Evaluation System

### How It Works

1. **evaluate.py** reads your memory files and calculates scores
2. **adapt.py** proposes changes based on scores (you approve/reject)
3. **report.py** updates your tracker

### Scoring Dimensions

| Dimension | Weight | What It Measures |
|-----------|--------|------------------|
| Completion | 30% | Tasks and deliverables finished |
| Quality | 25% | Code quality, tests passing |
| Velocity | 25% | Pace vs. expected timeline |
| Learning | 20% | Reflections, best practices captured |

### Allowed Adaptations

The system can only propose (you approve):
- Change learner level
- Reorder upcoming months
- Insert remediation weeks
- Swap projects for equivalents

See [docs/evaluation/adaptation-rules.md](docs/evaluation/adaptation-rules.md) for details.

---

## Memory System

### Files (Append-Only Source of Truth)

| File | Purpose |
|------|---------|
| `learner_profile.json` | Your goals, constraints, schedule |
| `progress_log.jsonl` | Timestamped progress events |
| `decisions.jsonl` | Important decisions made |
| `best_practices.md` | Living doc of learnings |

### Important

- Memory files are **append-only** — don't delete entries
- `tracker.md` is **derived** — can be regenerated anytime
- Claude must get your approval before writing to memory

---

## Running the Path Engine

The path engine uses Python stdlib only (no dependencies).

```bash
# Run evaluation
python .claude/path-engine/evaluate.py

# Get adaptation recommendations
python .claude/path-engine/adapt.py

# Update tracker
python .claude/path-engine/report.py
```

### Options

```bash
# Evaluate specific month
python .claude/path-engine/evaluate.py --month 3

# Output JSON
python .claude/path-engine/evaluate.py --format json
```

---

## Hooks

Shell scripts for common workflows:

```bash
# Start a new week
bash .claude/hooks/pre_week_start.sh

# End of week review
bash .claude/hooks/post_week_review.sh

# Pre-publish checks
bash .claude/hooks/pre_publish_check.sh
```

### Windows Users

Use WSL or Git Bash. See [docs/hooks.md](docs/hooks.md) for manual alternatives.

---

## Templates

Ready-to-use project templates:

| Template | Use Case |
|----------|----------|
| `template-fastapi-service` | REST APIs for ML models |
| `template-data-pipeline` | Data processing pipelines |
| `template-rag-service` | RAG systems with evaluation |
| `template-eval-harness` | Model evaluation frameworks |

Each includes:
- Working code
- Tests
- `pyproject.toml` with dependencies
- Documentation

---

## CI/CD

GitHub Actions runs automatically:
- **ruff** for code style
- **pytest** for tests
- **Path engine** validation
- **Documentation** link checking

See `.github/workflows/ci.yml` for details.

---

## If You Get Stuck

1. Run `/debug-learning` in Claude Code
2. Check [paths/beginner/README.md](paths/beginner/README.md) "If you are stuck" section
3. Review your progress in `tracker.md`
4. Ask the Coach agent for guidance

---

## Upgrading Your Level

When you're ready to move beyond Beginner:

1. Run `/evaluate` to check your scores
2. If scores are high, `/adapt-path` may suggest an upgrade
3. You approve or reject the recommendation
4. If approved, regenerate the repo with the new level

Level progression:
- **Beginner** → Tier 1 (53 technologies)
- **Intermediate** → Tier 1 + Tier 2 (148 technologies)
- **Advanced** → All tiers (175 technologies)

---

## Resources

- **Generator Prompt**: [SETUP.md](SETUP.md)
- **Tech Stack Reference**: [STACK.md](STACK.md)
- **System Overview**: [docs/system-overview.md](docs/system-overview.md)

---

## Contributing

This is your personal learning repository. Feel free to:
- Customize the curriculum
- Add your own templates
- Improve documentation
- Share learnings in `best_practices.md`

---

**Start here**: [paths/beginner/README.md](paths/beginner/README.md)

Happy learning! 🚀
