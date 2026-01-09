# System Overview

How the AI Practitioner Booster learning system works.

## What This System Is

The AI Practitioner Booster is a self-directed learning OS that helps you:
- Learn AI/ML skills through hands-on projects
- Track your progress systematically
- Get adaptive recommendations
- Build a portfolio of work

It's designed for **one year of learning** (2026), with monthly projects that build skills progressively.

---

## Core Principles

### 1. Human in the Loop
Claude provides recommendations. You make decisions. No changes happen without your explicit approval.

### 2. Project-Based Learning
Each month focuses on building something real — not just reading or watching tutorials.

### 3. Adaptive Pacing
The system monitors your progress and suggests adjustments. You can speed up, slow down, or change focus.

### 4. Memory and Continuity
Your progress, decisions, and learnings are stored locally. Each session builds on the previous ones.

---

## Architecture

```
┌────────────────────────────────────────────────────────────┐
│                      YOU (LEARNER)                         │
├────────────────────────────────────────────────────────────┤
│                                                            │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐│
│   │   Claude     │───▶│    Memory    │───▶│   Tracker    ││
│   │   Agents     │    │   System     │    │   & Reports  ││
│   └──────────────┘    └──────────────┘    └──────────────┘│
│          │                   │                   │        │
│          ▼                   ▼                   ▼        │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐│
│   │   Commands   │    │ Path Engine  │    │   Docs &     ││
│   │   & Skills   │    │ (Evaluation) │    │   Curriculum ││
│   └──────────────┘    └──────────────┘    └──────────────┘│
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## Key Components

### Claude Agents (`.claude/agents/`)
Six specialized AI personas:
- **Planner**: Creates plans and schedules
- **Builder**: Writes code and implements features
- **Reviewer**: Provides feedback and code review
- **Evaluator**: Assesses progress and generates scores
- **Coach**: Offers guidance and helps with blockers
- **Researcher**: Gathers information and explores topics

Each agent operates in advisory mode — suggestions only.

### Commands (`.claude/commands/`)
Slash commands for common workflows:
- `/status` — See where you are
- `/plan-week` — Plan what's next
- `/evaluate` — Get scores
- `/adapt-path` — See recommendations

### Skills (`.claude/skills/`)
Detailed playbooks for specific tasks:
- EDA to Insight
- Baseline Model and Card
- RAG with Evals
- API Shipping Checklist

### Memory System (`.claude/memory/`)
Local storage for your learning journey:
- `learner_profile.json` — Your goals and constraints
- `progress_log.jsonl` — Timestamped events
- `decisions.jsonl` — Important decisions
- `best_practices.md` — Captured learnings

### Path Engine (`.claude/path-engine/`)
Python scripts for the evaluation loop:
- `evaluate.py` — Compute scores
- `adapt.py` — Propose changes
- `report.py` — Update tracker

---

## The Learning Loop

### Evaluate
```
python .claude/path-engine/evaluate.py
```
Computes scores from your memory and activity:
- **Completion**: Tasks done vs. planned
- **Quality**: Tests, docs, reviews
- **Velocity**: Progress rate and trends
- **Learning**: Reflections and best practices

### Recommend
```
python .claude/path-engine/adapt.py
```
Based on scores, proposes adaptations:
- Remediation weeks (if struggling)
- Scope adjustments (if behind)
- Acceleration (if excelling)

### Approve (You)
You review each proposal and decide:
- Approve and apply
- Reject and continue
- Modify and apply

### Execute
Only approved changes are applied. The system updates:
- Your tracker
- Your decisions log
- Your path going forward

---

## Monthly Structure

Each month has:
- **Theme**: Focus area (e.g., "Data Pipelines")
- **Learning Goals**: What you'll learn
- **Main Project**: What you'll build
- **Definition of Done**: How you know you're finished
- **Stretch Goals**: Optional extras

Monthly README location: `paths/beginner/month-XX/README.md`

---

## Tier System

Learning is organized into three tiers:

| Tier | Focus | Item Count |
|------|-------|------------|
| Tier 1 | Beginner Foundation | 53 technologies |
| Tier 2 | Intermediate Shipping | 95 technologies |
| Tier 3 | Advanced Scale | 27 technologies |

**Beginner** learners focus on Tier 1 only in 2026.

See `stacks/tiers.md` for details.

---

## File Locations

| What | Where |
|------|-------|
| Claude capabilities | `.claude/` |
| Documentation | `docs/` |
| Your learning path | `paths/beginner/` |
| Stack definitions | `stacks/` |
| Project templates | `templates/` |
| Example projects | `examples/` |

---

## Integration Points

### With Claude Code
- Commands work as slash commands
- Agents respond to natural language
- Memory persists between sessions

### With Your IDE
- Work on projects in VS Code
- Use Git for version control
- Run tests with pytest

### With External Tools
- GitHub for code hosting
- Optional: Cloud platforms for deployment

---

## What Makes This Different

### Not a Course
This is a system, not a video series. You learn by doing projects with AI assistance.

### Not Autonomous
Claude assists but doesn't decide. You're always in control.

### Not One-Size-Fits-All
The adaptive system adjusts to your pace, schedule, and challenges.

### Not Ephemeral
Everything is logged and persisted. Your learning journey is documented.

---

## Getting Started

1. Read this overview (done!)
2. Check your path: `paths/beginner/README.md`
3. Run `/status` to see current state
4. Start with your first month's project

---

## Further Reading

- [How to Use](how-to-use.md) — Practical guide
- [Commands](commands.md) — Command reference
- [Agents](agents.md) — Agent details
- [Evaluation](evaluation/rubric.md) — How scoring works
- [.claude/README.md](../.claude/README.md) — Technical details
