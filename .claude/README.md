# Claude Capabilities

This folder contains all AI system components for the AI Practitioner Booster 2026.

## Directory Structure

```
.claude/
├── agents/          # Agent role definitions
├── commands/        # Command catalog and routing
├── skills/          # Reusable skill playbooks
├── hooks/           # Automation scripts
├── memory/          # Learning state storage
├── mcp/             # Model Context Protocol integrations
└── path-engine/     # Evaluation and adaptation scripts
```

---

## agents/

Agent definitions that Claude Code adopts when executing commands:

| Agent | File | Purpose |
|-------|------|---------|
| Planner | `planner.md` | Creates weekly plans, schedules tasks |
| Builder | `builder.md` | Writes code, ships features |
| Reviewer | `reviewer.md` | Reviews code, suggests improvements |
| Evaluator | `evaluator.md` | Scores progress, identifies gaps |
| Coach | `coach.md` | Provides guidance, retrospectives |
| Researcher | `researcher.md` | Finds resources, debugs blockers |

---

## commands/

The command system that routes user requests to agents.

- **`catalog.md`** — Source of truth for all commands
- Commands are invoked via `/command-name` in Claude Code
- Each command specifies which agent handles it and what artifacts are produced

See [catalog.md](commands/catalog.md) for the full list.

---

## skills/

Reusable playbooks for common tasks:

| Skill | File | Use Case |
|-------|------|----------|
| EDA to Insight | `eda.md` | Exploratory data analysis workflow |
| Shipping APIs | `shipping-api.md` | Build and deploy FastAPI services |
| RAG + Evals | `rag-eval.md` | RAG systems with evaluation |

---

## hooks/

Shell scripts for automation:

| Hook | File | Trigger |
|------|------|---------|
| Pre-week Start | `pre_week_start.sh` | Before starting a new week |
| Post-week Review | `post_week_review.sh` | After weekly retrospective |
| Pre-publish Check | `pre_publish_check.sh` | Before publishing to portfolio |

### Running Hooks

```bash
bash .claude/hooks/pre_week_start.sh
bash .claude/hooks/post_week_review.sh
bash .claude/hooks/pre_publish_check.sh
```

---

## memory/

Append-only learning state storage:

| File | Format | Purpose |
|------|--------|---------|
| `learner_profile.json` | JSON | Static learner configuration |
| `progress_log.jsonl` | JSON Lines | Event log of progress updates |
| `decisions.jsonl` | JSON Lines | Record of adaptation decisions |
| `best_practices.md` | Markdown | Accumulated best practices |

### Memory Rules

1. **Append-only**: Never delete entries from `.jsonl` files
2. **Timestamps**: Always use ISO 8601 format
3. **Best practices**: Only append, never remove

---

## mcp/

Model Context Protocol tool contracts:

| File | Purpose |
|------|---------|
| `tool_contracts.md` | Tool specifications |
| `example_server.py` | Example MCP server |
| `example_client.py` | Example MCP client |

---

## path-engine/

Python scripts for the Evaluate → Adapt → Execute loop:

| Script | Purpose |
|--------|---------|
| `evaluate.py` | Read memory, compute scores |
| `adapt.py` | Propose path mutations |
| `report.py` | Update tracker.md |

### Running the Engine

```bash
python .claude/path-engine/evaluate.py
python .claude/path-engine/adapt.py
python .claude/path-engine/report.py
```

---

## Integration with Claude Code

When Claude Code is connected to this repo:

1. Claude reads `CLAUDE.md` at the root for guidance
2. Commands in `commands/catalog.md` are available via `/command-name`
3. Agents adopt their roles based on definitions in `agents/`
4. Memory files in `memory/` track all learning state

The system operates as a continuous learning loop that evaluates progress, adapts the curriculum, and guides execution.
