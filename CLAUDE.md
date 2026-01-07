# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Repository Purpose

This is the **AI Practitioner Booster 2026** — an AI-driven, project-based learning system. The repository helps learners master AI/ML engineering through a structured 12-month curriculum with continuous evaluation and adaptation.

## Key Architecture

### Claude Capabilities (`.claude/`)

All AI system components live in `.claude/`:

- **agents/**: Agent role definitions (planner, builder, reviewer, evaluator, coach, researcher)
- **commands/**: Command catalog (`catalog.md` is source of truth)
- **skills/**: Reusable skill playbooks for common tasks
- **hooks/**: Shell scripts for automation (pre_week_start, post_week_review, pre_publish_check)
- **memory/**: Learning state storage (learner_profile.json, progress_log.jsonl, decisions.jsonl, best_practices.md)
- **mcp/**: Model Context Protocol tool contracts and examples
- **path-engine/**: Python scripts for evaluation, adaptation, and reporting

### Learner Path

The current learner is at **Advanced** level, completing Tier 1 + Tier 2 + Tier 3.

- Dashboard: `paths/Advanced/README.md`
- Monthly modules: `paths/Advanced/month-01/` through `month-12/`
- Journal: `paths/Advanced/journal/`
- Progress tracker: `paths/Advanced/tracker.md`

### Templates

Starter templates in `templates/`:
- `template-fastapi-service/` — FastAPI microservice scaffold
- `template-data-pipeline/` — Data pipeline with validation
- `template-rag-service/` — RAG system with evaluation
- `template-eval-harness/` — Evaluation framework

## Command Routing

When the user invokes a command, route to the appropriate agent:

| Command | Primary Agent | Supporting Agents |
|---------|--------------|-------------------|
| `/status` | Evaluator | — |
| `/plan-week` | Planner | Coach |
| `/start-week` | Planner | — |
| `/ship-mvp` | Builder | Reviewer |
| `/harden` | Builder | Reviewer |
| `/publish` | Builder | Coach |
| `/retro` | Coach | Evaluator |
| `/evaluate` | Evaluator | — |
| `/adapt-path` | Evaluator | Coach |
| `/add-best-practice` | Coach | — |
| `/debug-learning` | Coach | Researcher |

## Memory Update Rules

When updating memory files:

1. **Append-only discipline**: Never delete entries from `progress_log.jsonl` or `decisions.jsonl`
2. **JSON Lines format**: Each entry is a single JSON object on its own line
3. **Timestamps**: Always include ISO 8601 timestamps
4. **Best practices**: Append to `best_practices.md`, never overwrite existing entries

## Evaluation Flow

1. Run `python .claude/path-engine/evaluate.py` to score progress
2. Run `python .claude/path-engine/adapt.py` to get adaptation recommendations
3. Run `python .claude/path-engine/report.py` to update `paths/Advanced/tracker.md`

## Allowed Adaptations

The system can only propose these mutations (see `docs/evaluation/adaptation-rules.md`):

- **Level change**: Upgrade/downgrade learner level (only at month boundaries)
- **Month reorder**: Swap upcoming month modules (preserving tier scope)
- **Remediation week**: Insert 1-week remediation block
- **Project swap**: Replace project with equivalent scope alternative

## Code Style

- Python: Use ruff for linting, follow PEP 8
- Markdown: Use consistent heading hierarchy, include links
- JSON: Pretty-print with 2-space indent
- Shell: POSIX-compatible when possible

## Testing

Run tests from template directories:

```bash
cd templates/template-fastapi-service && pytest
cd templates/template-data-pipeline && pytest
cd templates/template-rag-service && pytest
cd templates/template-eval-harness && pytest
```

## CI/CD

GitHub Actions workflow in `.github/workflows/ci.yml`:
- Runs on PR and push to main
- Lints with ruff
- Runs pytest on all templates
