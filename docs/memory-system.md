# Memory System

How the learning state is stored and managed.

## Overview

Memory files in `.claude/memory/` are the **source of truth** for your learning journey:

| File | Purpose | Format |
|------|---------|--------|
| `learner_profile.json` | Your configuration | JSON |
| `progress_log.jsonl` | Event stream | JSON Lines |
| `decisions.jsonl` | Important choices | JSON Lines |
| `best_practices.md` | Accumulated learnings | Markdown |

For technical details, see [.claude/memory/README.md](../.claude/memory/README.md).

---

## Core Principles

### 1. Append-Only

Memory files are append-only. Old entries are never deleted or modified automatically.

```
2026-01-01: Event A → stays
2026-01-15: Event B → appended
2026-02-01: Event C → appended
```

This provides:
- Complete history
- Audit trail
- Reproducibility

### 2. Human Approval Required

Claude must show proposed updates and receive explicit approval before writing.

```
Claude: "I'd like to log this milestone. Here's the entry:
         {timestamp: ..., event: milestone, description: ...}

         Approve this update? (yes/no)"

You:     "yes"

Claude:  [writes to progress_log.jsonl]
```

### 3. Source of Truth

Memory files are authoritative. Other files are derived:

| Authoritative | Derived |
|---------------|---------|
| `progress_log.jsonl` | `tracker.md` |
| `decisions.jsonl` | adaptation history |
| `learner_profile.json` | dashboard status |

`report.py` regenerates `tracker.md` from memory files.

---

## File Details

### learner_profile.json

Your learning configuration:

```json
{
  "level": "intermediate",
  "created_at": "2026-01-01T00:00:00Z",
  "goals": [
    "Master ML fundamentals",
    "Build portfolio projects"
  ],
  "constraints": {
    "hours_per_week": 10,
    "preferred_times": ["evenings", "weekends"]
  },
  "preferences": {
    "learning_style": "project-based",
    "communication": "direct"
  },
  "tier_scope": {
    "tier_1": true,
    "tier_2": true,
    "tier_3": false
  }
}
```

**How to update**: Edit directly or ask Claude to propose updates.

### progress_log.jsonl

Event stream of your journey:

```json
{"timestamp": "2026-01-15T09:00:00Z", "event": "week_start", "week": "3"}
{"timestamp": "2026-01-15T18:30:00Z", "event": "milestone", "description": "Completed EDA"}
{"timestamp": "2026-01-16T10:00:00Z", "event": "learning", "description": "Learned attention mechanisms"}
{"timestamp": "2026-01-19T17:00:00Z", "event": "week_end", "week": "3"}
```

**Event types**:
- `week_start` / `week_end` — Week boundaries
- `milestone` — Significant completions
- `learning` — Learning events
- `evaluation` — Assessment results
- `decision` — Choices made
- `reflection` — Retrospectives

### decisions.jsonl

Important choices recorded:

```json
{
  "timestamp": "2026-02-01T10:00:00Z",
  "type": "project_choice",
  "choice": "RAG over fine-tuning",
  "rationale": "Better fit for current skills and timeline"
}
{
  "timestamp": "2026-03-15T14:00:00Z",
  "type": "path_adaptation",
  "adaptation": "month_reorder",
  "details": {"from": [5, 6], "to": [6, 5]},
  "approved_by": "learner"
}
```

**Decision types**:
- `project_choice` — Choosing between options
- `technology_choice` — Tech decisions
- `path_adaptation` — Path changes
- `level_change` — Level upgrades/downgrades

### best_practices.md

Living document of learnings:

```markdown
### RAG Evaluation Order
**Category**: RAG | **Added**: 2026-03-15

Always evaluate retrieval quality before debugging generation.

**When to apply**: Building or debugging RAG systems.
```

**How to add**: Use `/add-best-practice` or edit directly.

---

## How Claude Uses Memory

### Reading

```
Claude reads memory to understand:
- Your level and goals (profile)
- Recent progress (progress_log)
- Past decisions (decisions)
- Accumulated knowledge (best_practices)
```

### Proposing Updates

```
1. Claude analyzes context
2. Claude formulates proposed entry
3. Claude shows you the proposal
4. You approve, reject, or modify
5. Only approved entries are written
```

### Example Workflow

```
You:     "/status"

Claude:  [reads learner_profile.json]
         [reads progress_log.jsonl]
         [reads tracker.md]

         "Based on your progress, here's your status:
          - Month 3, Week 2
          - Recent: Completed EDA milestone
          - Focus: Build retrieval component

          I'd like to log this status check. Entry:
          {timestamp: ..., event: status_check}

          Approve? (yes/no)"

You:     "yes"

Claude:  [appends to progress_log.jsonl]
```

---

## Your Control

### Reviewing Memory

You can read all memory files:
```bash
cat .claude/memory/learner_profile.json
cat .claude/memory/progress_log.jsonl
cat .claude/memory/decisions.jsonl
cat .claude/memory/best_practices.md
```

### Editing Memory

You have full control to edit:
```bash
# Edit profile
code .claude/memory/learner_profile.json

# Edit best practices
code .claude/memory/best_practices.md
```

### Removing Entries

If needed, you can remove truly erroneous entries:
```bash
# Edit the JSONL file to remove a line
code .claude/memory/progress_log.jsonl
```

(This should be rare — the system is designed to be append-only)

---

## Memory and Evaluation

The path engine reads memory for evaluation:

```
evaluate.py reads:
├── progress_log.jsonl  → Count milestones, events
├── decisions.jsonl     → Track significant choices
└── learner_profile.json → Know your constraints

Outputs:
├── Scores
├── Evidence
└── Assessment
```

---

## Memory and Adaptation

adapt.py uses memory to propose changes:

```
adapt.py reads:
├── Recent evaluations from progress_log
├── Historical decisions from decisions.jsonl
├── Current level from profile

Outputs (proposals only):
├── Level change proposals
├── Remediation suggestions
├── Project swap options
```

**No changes are auto-applied** — you approve each proposal.

---

## Regenerating Derived Files

If `tracker.md` gets out of sync:

```bash
python .claude/path-engine/report.py
```

This regenerates tracker from memory files.

---

## Related Documentation

- [.claude/memory/README.md](../.claude/memory/README.md) — Technical details
- [evaluation/scoring.md](evaluation/scoring.md) — How memory affects scores
- [system-overview.md](system-overview.md) — Full system architecture
