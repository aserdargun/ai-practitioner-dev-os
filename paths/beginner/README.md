# Beginner Learning Dashboard

**Level**: Beginner
**Tier Scope**: Tier 1 (53 technologies)
**Timeline**: 12 months (2026)

Welcome to your AI Practitioner Booster dashboard!

---

## Current Status

```
Month: [Update with current month]
Week:  [Update with current week]
```

Run `/status` for a live progress snapshot.

---

## Quick Start

### Today
```
/status
```

### This Week
```
/plan-week
I have [X] hours available this week
```

### End of Week
```
/retro
```

---

## Monthly Progress

| Month | Theme | Status |
|-------|-------|--------|
| 1 | Environment & Python Basics | ☐ Not Started |
| 2 | Data Manipulation with Pandas | ☐ Not Started |
| 3 | Statistics & Probability | ☐ Not Started |
| 4 | Data Visualization | ☐ Not Started |
| 5 | Introduction to ML | ☐ Not Started |
| 6 | Classification Algorithms | ☐ Not Started |
| 7 | Time Series Fundamentals | ☐ Not Started |
| 8 | Natural Language Processing Basics | ☐ Not Started |
| 9 | Deep Learning Introduction | ☐ Not Started |
| 10 | Building Web APIs | ☐ Not Started |
| 11 | Interactive Dashboards | ☐ Not Started |
| 12 | Capstone Project | ☐ Not Started |

---

## This Week Plan

| Day | Focus | Hours | Done |
|-----|-------|-------|------|
| Mon | | | ☐ |
| Tue | | | ☐ |
| Wed | | | ☐ |
| Thu | | | ☐ |
| Fri | | | ☐ |
| Weekend | | | ☐ |

**Total Hours**: ___ / ___ planned

---

## Commands Cheat Sheet

### Daily
| Command | What It Does |
|---------|--------------|
| `/status` | See where you are |
| `/debug-learning` | When stuck |

### Weekly
| Command | What It Does |
|---------|--------------|
| `/plan-week` | Plan your week |
| `/start-week` | Initialize week structure |
| `/retro` | End-of-week reflection |
| `/add-best-practice` | Capture a learning |

### Project
| Command | What It Does |
|---------|--------------|
| `/ship-mvp` | Finalize deliverables |
| `/harden` | Add tests and docs |
| `/publish` | Prepare for portfolio |

### Evaluation
| Command | What It Does |
|---------|--------------|
| `/evaluate` | Get evaluation scores |
| `/adapt-path` | See path recommendations |

Full reference: [docs/commands.md](../../docs/commands.md)

---

## Evaluation Snapshot

Run this to see your scores:
```
/evaluate
```

Or via command line:
```bash
python .claude/path-engine/evaluate.py
```

### Score Interpretation
| Score | Meaning |
|-------|---------|
| 80+ | Exceeding expectations |
| 60-79 | On track |
| 40-59 | Needs attention |
| <40 | At risk — consider /adapt-path |

---

## If You're Stuck

### Quick Fix
```
/debug-learning
[Describe what's blocking you]
```

### Still Stuck?
1. Take a break (seriously)
2. Re-read the current month's README
3. Try a smaller piece of the problem
4. Ask Claude for alternative approaches
5. Consider if scope is too large

### Feeling Overwhelmed?
```
/adapt-path
```
Review proposals for scope reduction or remediation.

---

## Upgrade / Downgrade Rules

### Consider Upgrading (to Intermediate) When:
- Overall score consistently >85 for 4+ weeks
- Completing Tier 1 content ahead of schedule
- Feeling unchallenged

**Action**: Run `/adapt-path` at month boundary

### Consider Downgrading When:
- Overall score consistently <40 for 4+ weeks
- Falling behind despite adjustments
- Significant life changes limiting time

**Action**: Run `/adapt-path` and discuss with Claude

### Level Changes
- **Only at month boundaries** (unless emergency)
- **Require your approval**
- **Logged to decisions.jsonl**

---

## Resources

### Current Month
See: [month-01/README.md](month-01/README.md) (update link for current month)

### Documentation
- [How to Use](../../docs/how-to-use.md) — Full guide
- [Evaluation Rubric](../../docs/evaluation/rubric.md) — How scoring works
- [Best Practices](../../.claude/memory/best_practices.md) — Your learnings

### Path Engine
```bash
# Get scores
python .claude/path-engine/evaluate.py

# See recommendations
python .claude/path-engine/adapt.py

# Update tracker
python .claude/path-engine/report.py
```

---

## Tracker

For detailed progress tracking, see: [tracker.md](tracker.md)

---

## Journal

Weekly reflections go in: [journal/](journal/)

Template: [journal/weekly-template.md](journal/weekly-template.md)

---

## Tips for Success

1. **Consistency beats intensity** — 1 hour daily > 7 hours once a week
2. **Log as you go** — Don't wait until end of week
3. **Ask for help early** — /debug-learning is your friend
4. **Ship something** — Imperfect and done > perfect and unfinished
5. **Reflect weekly** — /retro makes you better faster

---

**Let's build something great!** 🚀

Start with `/status` to see where you are.
