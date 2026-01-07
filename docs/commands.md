# Commands Guide

Complete guide to all commands available in the learning system.

---

## Quick Reference

| Command | Purpose | Agent |
|---------|---------|-------|
| `/status` | Check progress | Evaluator |
| `/plan-week` | Generate weekly plan | Planner |
| `/start-week` | Begin the week | Planner |
| `/ship-mvp` | Ship working code | Builder |
| `/harden` | Add tests and docs | Builder |
| `/publish` | Prepare for demo | Builder |
| `/retro` | Weekly retrospective | Coach |
| `/evaluate` | Score progress | Evaluator |
| `/adapt-path` | Propose changes | Evaluator |
| `/add-best-practice` | Capture learning | Coach |
| `/debug-learning` | Get unstuck | Coach |
| `/report` | Update tracker | Evaluator |

---

## Detailed Command Reference

### `/status`

**Purpose**: Check your current progress and identify blockers.

**Agent**: Evaluator

**When to use**: Daily check-in, before starting work

**What it shows**:
- Current week and month
- Tasks in progress
- Completed tasks
- Any blockers or warnings

**Example**:
```
/status

📊 Status Report
────────────────────────
Month: 02 (Data Engineering)
Week: 3 of 4

Progress:
✅ Completed: 4 tasks
🔄 In Progress: Data validation pipeline
⏳ Remaining: 2 tasks

Status: On Track (78%)
```

---

### `/plan-week`

**Purpose**: Generate this week's task list based on current month objectives.

**Agent**: Planner (with Coach support)

**When to use**: Start of each week (Monday)

**What it produces**:
- Task list for the week
- Estimated effort per task
- Resources and references
- Journal entry in `paths/Advanced/journal/`

**Example**:
```
/plan-week

📅 Week 3 Plan Generated
────────────────────────
Focus: Data Validation & Quality

Tasks:
1. [ ] Implement Pydantic models (2h)
2. [ ] Write validation tests (2h)
3. [ ] Create data pipeline (3h)
4. [ ] Document the API (1h)

See: paths/Advanced/journal/week-03.md
```

---

### `/start-week`

**Purpose**: Initialize the week and run pre-week checks.

**Agent**: Planner

**When to use**: Monday morning

**What it does**:
1. Runs `pre_week_start.sh` hook
2. Validates environment
3. Checks for uncommitted work
4. Shows week overview

**Example**:
```
/start-week

🚀 Starting Week 3
────────────────────────
Running pre-week checks...

✓ Git repository clean
✓ Python 3.11 detected
✓ Memory files present
✓ No linting errors

Ready to begin!
Run /plan-week if you haven't already.
```

---

### `/ship-mvp`

**Purpose**: Ship the minimum viable version of your current task.

**Agent**: Builder (with Reviewer support)

**When to use**: When feature is ready for first working version

**What it does**:
1. Reviews current task requirements
2. Identifies applicable template
3. Helps implement core functionality
4. Creates commit

**Example**:
```
/ship-mvp

🚀 Shipping MVP
────────────────────────
Task: Data validation pipeline

Actions:
✓ Created src/pipeline/validator.py
✓ Added Pydantic models
✓ Basic tests passing (3/3)

Commit: abc1234
"Add data validation pipeline with Pydantic models"
```

---

### `/harden`

**Purpose**: Add tests, documentation, and error handling to existing code.

**Agent**: Builder (with Reviewer support)

**When to use**: Friday, before publish, or when code needs polish

**What it does**:
1. Reviews existing code
2. Identifies missing tests
3. Adds error handling
4. Updates documentation
5. Runs linting

**Example**:
```
/harden

🔧 Hardening Code
────────────────────────
Analyzing: src/pipeline/

Improvements:
✓ Added 5 edge case tests
✓ Added input validation
✓ Updated docstrings
✓ Fixed 2 linting issues

Test Coverage: 85% (+12%)
```

---

### `/publish`

**Purpose**: Prepare code for demo or portfolio inclusion.

**Agent**: Builder (with Coach support)

**When to use**: End of month, before demo

**What it does**:
1. Runs `pre_publish_check.sh`
2. Verifies all tests pass
3. Checks documentation completeness
4. Creates demo-ready package

**Example**:
```
/publish

📦 Publish Check
────────────────────────
Running quality gates...

Git Status: ✓ Clean
Linting: ✓ No errors
Tests: ✓ 24/24 passing
Docs: ✓ README complete
Security: ✓ No secrets found

✅ Ready to publish!
```

---

### `/retro`

**Purpose**: Conduct weekly retrospective.

**Agent**: Coach (with Evaluator support)

**When to use**: End of week (Friday/Weekend)

**What it does**:
1. Runs `post_week_review.sh`
2. Collects metrics
3. Facilitates reflection
4. Captures action items

**Example**:
```
/retro

📝 Week 3 Retrospective
────────────────────────

What Went Well:
• Completed pipeline ahead of schedule
• Tests caught 2 bugs early

What Could Improve:
• Started documentation too late
• Forgot to log one task completion

Key Learning:
→ "Test early, document as you go"
  Added to best_practices.md

Action Items:
[ ] Set daily doc reminder
[ ] Review test coverage reports
```

---

### `/evaluate`

**Purpose**: Run full evaluation of your progress.

**Agent**: Evaluator

**When to use**: End of week, end of month

**What it does**:
1. Reads all memory files
2. Collects repo signals
3. Calculates dimension scores
4. Generates recommendations

**Example**:
```
/evaluate

📊 Evaluation Report
────────────────────────

Scores:
Completion   [████████░░] 82%
Quality      [███████░░░] 75%
Consistency  [█████████░] 88%
Growth       [███████░░░] 70%
Engagement   [████████░░] 80%

Overall: 79% (On Track)

Recommendations:
• Add more tests to improve quality
• Capture learnings as best practices
```

---

### `/adapt-path`

**Purpose**: Get recommendations for learning path changes.

**Agent**: Evaluator (with Coach support)

**When to use**: After evaluation, when struggling, or exceeding expectations

**What it does**:
1. Analyzes evaluation results
2. Applies adaptation rules
3. Proposes mutations
4. Logs decisions

**Example**:
```
/adapt-path

🔄 Path Analysis
────────────────────────

Current: Month 02, Week 3
Score: 79% (On Track)

Proposed Changes: None

Your current pace is appropriate.
Continue with the planned curriculum.
```

Or with changes:
```
/adapt-path

🔄 Path Analysis
────────────────────────

Current: Month 02, Week 3
Score: 52% (Needs Attention)

Proposed Changes:

1. [REMEDIATION_WEEK] ⚠️ Requires Approval
   Insert catch-up week before Month 03
   Focus: Quality improvement, test coverage

Review and approve? (y/n)
```

---

### `/add-best-practice`

**Purpose**: Capture a learning or pattern you've discovered.

**Agent**: Coach

**When to use**: After learning something valuable

**Syntax**: `/add-best-practice "Your learning here"`

**What it does**:
- Appends entry to `best_practices.md`
- Formats with date and context
- Updates growth score

**Example**:
```
/add-best-practice "Always validate data at API boundaries using Pydantic"

✅ Best Practice Added
────────────────────────

### 2026-01-15 - Always validate data at API boundaries using Pydantic

Added to: .claude/memory/best_practices.md
```

---

### `/debug-learning`

**Purpose**: Get help when you're stuck on something.

**Agent**: Coach (with Researcher support)

**When to use**: When blocked, confused, or need guidance

**Syntax**: `/debug-learning "Description of your blocker"`

**What it does**:
1. Analyzes the blocker type
2. Provides targeted help
3. Suggests resources
4. Offers next steps

**Example**:
```
/debug-learning "Can't figure out how to mock async functions in pytest"

🔍 Debugging: Async Test Mocking
────────────────────────

The Issue:
Async functions need special handling in pytest.

Solution:
1. Install pytest-asyncio
2. Mark tests with @pytest.mark.asyncio
3. Use AsyncMock from unittest.mock

Example:
```python
import pytest
from unittest.mock import AsyncMock

@pytest.mark.asyncio
async def test_async_function():
    mock = AsyncMock(return_value=42)
    result = await mock()
    assert result == 42
```

Resources:
• pytest-asyncio docs
• Real Python async testing guide
```

---

### `/report`

**Purpose**: Generate progress report and update tracker.

**Agent**: Evaluator

**When to use**: Any time you want a summary

**What it does**:
1. Compiles progress data
2. Generates formatted report
3. Updates `tracker.md`

**Example**:
```
/report

📈 Progress Report Generated
────────────────────────

Month 2, Week 3
Overall: 79%
Status: On Track

Tracker updated: paths/Advanced/tracker.md
```

---

## Command Tips

### Combining Commands

Commands can be run in sequence:
```
/start-week
/plan-week
```

### Getting Help

Ask Claude to explain any command:
```
"What does /harden do exactly?"
```

### Custom Usage

You can ask for variations:
```
"Run /evaluate but focus on quality scores"
```

---

## See Also

- [How to Use](how-to-use.md) — Complete workflow guide
- [Agents](agents.md) — Agent role details
- [Evaluation Rubric](evaluation/rubric.md) — Scoring details
