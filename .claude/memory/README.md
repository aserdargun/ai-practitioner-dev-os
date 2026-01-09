# Memory System

This folder contains the local memory store for the AI Practitioner Learning OS.

## Overview

The memory system tracks your learning journey through append-only files. Claude reads these files to provide context-aware recommendations.

## Files

| File | Purpose | Format |
|------|---------|--------|
| `learner_profile.json` | Goals, constraints, schedule | JSON object |
| `progress_log.jsonl` | Timestamped events | JSON Lines |
| `decisions.jsonl` | Important decisions | JSON Lines |
| `best_practices.md` | Learned patterns | Markdown |

## Human Oversight Requirement

**Critical**: Claude must show proposed memory updates to you and receive explicit approval before writing to any memory file.

Memory is for record-keeping. It does NOT autonomously modify Claude's behavior. All actions still require your approval.

## File Details

### learner_profile.json

Stores your goals, constraints, and preferences.

```json
{
  "name": "Your Name",
  "level": "advanced",
  "started": "2026-01-01",
  "goals": [
    "Build production ML systems",
    "Master Kubernetes deployments"
  ],
  "constraints": {
    "hours_per_week": 15,
    "preferred_days": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "timezone": "UTC"
  },
  "preferences": {
    "learning_style": "hands-on",
    "feedback_frequency": "weekly"
  }
}
```

### progress_log.jsonl

Append-only log of learning events. Each line is a JSON object.

```jsonl
{"timestamp": "2026-01-09T10:00:00Z", "type": "week_start", "week": 2}
{"timestamp": "2026-01-09T14:00:00Z", "type": "task_complete", "task": "Setup vector store"}
{"timestamp": "2026-01-09T17:00:00Z", "type": "blocker", "description": "Embedding dimension mismatch"}
{"timestamp": "2026-01-10T11:00:00Z", "type": "blocker_resolved", "description": "Fixed embedding dimensions"}
```

**Event Types**:
- `week_start`, `week_end` - Week boundaries
- `task_complete` - Task finished
- `blocker`, `blocker_resolved` - Blockers
- `milestone` - Major achievement
- `evaluation` - Formal evaluation
- `adaptation` - Path change applied

### decisions.jsonl

Records important decisions for future reference.

```jsonl
{"timestamp": "2026-01-05T09:00:00Z", "decision": "Use Qdrant for vector store", "rationale": "Good Python SDK, free self-hosted option", "alternatives": ["Pinecone", "FAISS"]}
{"timestamp": "2026-01-08T14:00:00Z", "decision": "500 token chunks with 50 overlap", "rationale": "Tested with real docs, best retrieval quality"}
```

### best_practices.md

Living document of learned patterns. Append new practices as you learn them.

```markdown
## RAG / Data Processing

### Chunking Strategy Testing
> Always test chunking with real documents before committing...

## API Development

### Health Endpoints
> Always implement /health and /ready endpoints...
```

## Memory Workflow

### How Claude Uses Memory

1. **Reads** memory files to understand context
2. **Proposes** updates based on your actions
3. **Waits** for your approval
4. **Writes** only after you confirm

### Example: Adding a Best Practice

**Claude proposes**:
```
I'd like to add this to best_practices.md:

### Connection Pooling
> Always use connection pooling for database connections in production...

**Approve?** (yes/no/modify)
```

**You approve**, then Claude appends to the file.

## Editing Memory

You have full control over memory files:

- **View**: Read any file directly
- **Edit**: Modify any entry (but prefer appending)
- **Delete**: Remove entries if needed (not recommended)

### Manual Editing

```bash
# View progress log
cat .claude/memory/progress_log.jsonl

# Add entry manually
echo '{"timestamp": "2026-01-09T12:00:00Z", "type": "note", "content": "Manual note"}' >> .claude/memory/progress_log.jsonl
```

## Memory vs Tracker

| Aspect | Memory Files | Tracker |
|--------|--------------|---------|
| Location | `.claude/memory/` | `paths/advanced/tracker.md` |
| Purpose | Source of truth | Derived view |
| Updates | Append-only | May be regenerated |
| Edited by | Claude (with approval) | `report.py` |

**Important**: Memory files are append-only sources of truth. The tracker at `paths/advanced/tracker.md` is a derived artifact that `report.py` may regenerate at any time (with user confirmation).

## Backup Recommendation

Memory files are valuable. Consider:
1. Committing them to git regularly
2. Backing up before major changes
3. Including in your repo's backup strategy
