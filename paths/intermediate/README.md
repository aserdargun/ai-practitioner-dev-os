# Intermediate Dashboard

**AI Practitioner Booster 2026 — Your Learning Command Center**

---

## Current Status

**Learner Level**: Intermediate

**Tier Scope**: Tier 1 + Tier 2 (148 technologies)

**Current Month**: 1 of 12

---

## Quick Actions

```bash
# Daily check-in
/status

# Plan your week
/plan-week

# Run evaluation
python .claude/path-engine/evaluate.py

# Update tracker
python .claude/path-engine/report.py
```

---

## This Week Plan

| Day | Focus | Status |
|-----|-------|--------|
| Monday | Review month goals, plan week | [ ] |
| Tuesday | Core learning, project setup | [ ] |
| Wednesday | Build MVP features | [ ] |
| Thursday | Continue building, initial tests | [ ] |
| Friday | Review progress, journal | [ ] |

**Week Goals**:
- [ ] Goal 1: _[fill in]_
- [ ] Goal 2: _[fill in]_
- [ ] Goal 3: _[fill in]_

---

## Commands Cheat-Sheet

| Phase | Command | Purpose |
|-------|---------|---------|
| **Daily** | `/status` | Where am I? What's next? |
| **Planning** | `/plan-week` | Create weekly plan |
| **Planning** | `/start-week` | Initialize week setup |
| **Building** | `/ship-mvp` | MVP completion checklist |
| **Building** | `/harden` | Quality focus |
| **Publishing** | `/publish` | Demo and write-up prep |
| **Reflection** | `/retro` | Weekly retrospective |
| **Evaluation** | `/evaluate` | Get scored assessment |
| **Adaptation** | `/adapt-path` | Request path change |
| **Learning** | `/add-best-practice` | Capture insight |
| **Help** | `/debug-learning` | Get unstuck |

Full reference: [docs/commands.md](../../docs/commands.md)

---

## Evaluation Snapshot

### How to Run

```bash
# Get scores
python .claude/path-engine/evaluate.py

# Get adaptation proposals
python .claude/path-engine/adapt.py

# Update tracker
python .claude/path-engine/report.py
```

### How to Interpret

| Overall Score | Assessment | Action |
|---------------|------------|--------|
| 90-100 | Exceptional | Consider upgrade to Advanced |
| 80-89 | Strong | On track, continue |
| 70-79 | Satisfactory | Minor adjustments |
| 60-69 | Needs Improvement | Focus on weak areas |
| Below 60 | At Risk | Consider remediation |

### Current Tracker

See [tracker.md](tracker.md) for your latest progress report.

---

## 12-Month Curriculum

| Month | Focus | Project |
|-------|-------|---------|
| [01](month-01/README.md) | Python & Data Foundations | EDA Project |
| [02](month-02/README.md) | ML Fundamentals | Classification Pipeline |
| [03](month-03/README.md) | Production APIs | FastAPI Service |
| [04](month-04/README.md) | Deep Learning | Neural Network Project |
| [05](month-05/README.md) | NLP Foundations | Text Classification |
| [06](month-06/README.md) | LLM Applications | Chatbot with RAG |
| [07](month-07/README.md) | RAG Systems | Document Q&A |
| [08](month-08/README.md) | MLOps Foundations | ML Pipeline |
| [09](month-09/README.md) | Cloud Deployment | Cloud ML Service |
| [10](month-10/README.md) | Observability | Monitored System |
| [11](month-11/README.md) | Advanced LLM | Agent System |
| [12](month-12/README.md) | Capstone | Full Portfolio Project |

---

## If You Are Stuck

### Try These Commands

```
/debug-learning

I'm stuck on [specific topic]. I've tried [what you tried].
```

### Check Resources

1. Review [best practices](../../.claude/memory/best_practices.md)
2. Check the relevant [skill playbook](../../docs/skills-playbook.md)
3. Look at [month documentation](month-01/README.md)

### Common Issues

| Issue | Solution |
|-------|----------|
| Concept unclear | Ask Researcher agent for resources |
| Code not working | Ask Builder agent for debugging help |
| Overwhelmed | Ask Coach agent for prioritization |
| Low scores | Run `/evaluate` and `/adapt-path` |

---

## Upgrade/Downgrade Rules

### Upgrade to Advanced

**Triggers**:
- Consistent 90+ scores for 3+ evaluations
- Comfortable with all Tier 2 technologies
- Ready for Kubernetes, distributed systems

**Process**:
```
/adapt-path

I've been scoring consistently high and I'm ready for Advanced level.
```

### Downgrade to Beginner

**Triggers**:
- Consistent below 60 scores
- Struggling with Tier 2 concepts
- Need more foundation focus

**Process**:
```
/adapt-path

I'm struggling with the intermediate content. Should I focus on foundations?
```

### Important Notes

- Level changes happen at month boundaries
- All changes require your approval
- No automatic level changes

---

## Key Links

| Resource | Link |
|----------|------|
| How to Use | [docs/how-to-use.md](../../docs/how-to-use.md) |
| Tiers Reference | [stacks/tiers.md](../../stacks/tiers.md) |
| Commands Guide | [docs/commands.md](../../docs/commands.md) |
| Evaluation Rubric | [docs/evaluation/rubric.md](../../docs/evaluation/rubric.md) |
| Report Generator | [.claude/path-engine/report.py](../../.claude/path-engine/report.py) |
| Best Practices | [.claude/memory/best_practices.md](../../.claude/memory/best_practices.md) |

---

## Weekly Workflow

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  MONDAY: /start-week → /plan-week → /status        │
│                                                     │
│  DAILY: /status → work → log progress              │
│                                                     │
│  MID-WEEK: /ship-mvp (when ready)                  │
│                                                     │
│  WEEK 3: /harden                                   │
│                                                     │
│  WEEK 4: /publish → /retro → /evaluate             │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## Journal

Track your learning journey:
- [Journal README](journal/README.md)
- [Weekly Template](journal/weekly-template.md)
- [Monthly Template](journal/monthly-template.md)

---

*Last updated: Auto-generated by setup*
