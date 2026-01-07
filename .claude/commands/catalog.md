# Command Catalog

This is the source of truth for all commands available in the AI Practitioner learning system.

---

## Command Reference

### Status & Planning

#### `/status`
Check current progress and blockers.

- **Agent**: Evaluator
- **Input**: Memory files, tracker
- **Output**: Status summary with progress metrics
- **Example**:
  ```
  /status

  Response:
  📊 Week 3 of Month 02 (Data Engineering)
  ✅ Completed: 4/6 tasks
  🔄 In Progress: Data validation pipeline
  ⏳ Remaining: 2 tasks
  📈 On track for weekly goals
  ```

#### `/plan-week`
Generate this week's task list.

- **Agent**: Planner (with Coach support)
- **Input**: Current month module, progress log
- **Output**: Weekly plan in journal
- **Example**:
  ```
  /plan-week

  Response:
  📅 Week 3 Plan Created
  See: paths/Advanced/journal/week-03.md
  ```

#### `/start-week`
Initialize the week and run pre-week hooks.

- **Agent**: Planner
- **Input**: Weekly plan
- **Output**: Hook execution, status update
- **Runs**: `.claude/hooks/pre_week_start.sh`

---

### Building & Shipping

#### `/ship-mvp`
Ship minimum viable version of current task.

- **Agent**: Builder (with Reviewer support)
- **Input**: Current task, applicable templates
- **Output**: Working code, commit
- **Example**:
  ```
  /ship-mvp

  Response:
  🚀 MVP Shipped!
  - Created: src/pipeline/validator.py
  - Tests: 3 passing
  - Commit: abc1234 "Add data validation pipeline"
  ```

#### `/harden`
Add tests, documentation, and error handling.

- **Agent**: Builder (with Reviewer support)
- **Input**: Existing code
- **Output**: Improved code, tests, docs
- **Runs**: ruff, pytest

#### `/publish`
Prepare code for demo or portfolio.

- **Agent**: Builder (with Coach support)
- **Input**: Completed feature
- **Output**: Polished, documented code
- **Runs**: `.claude/hooks/pre_publish_check.sh`

---

### Reflection & Growth

#### `/retro`
Run weekly retrospective.

- **Agent**: Coach (with Evaluator support)
- **Input**: Week's journal, progress log
- **Output**: Retrospective summary
- **Runs**: `.claude/hooks/post_week_review.sh`
- **Example**:
  ```
  /retro

  Response:
  📝 Week 3 Retrospective

  What Went Well:
  - Completed data pipeline ahead of schedule
  - Learned Pydantic validation patterns

  What to Improve:
  - More consistent commit messages
  - Earlier testing in development cycle

  Key Learning:
  → Added to best_practices.md
  ```

#### `/add-best-practice`
Capture a learning or pattern.

- **Agent**: Coach
- **Input**: Learning description
- **Output**: Entry in best_practices.md
- **Example**:
  ```
  /add-best-practice "Always validate data at system boundaries using Pydantic"

  Response:
  ✅ Best practice added to .claude/memory/best_practices.md
  ```

#### `/debug-learning`
Get help when stuck.

- **Agent**: Coach (with Researcher support)
- **Input**: Description of blocker
- **Output**: Guidance, resources, next steps
- **Example**:
  ```
  /debug-learning "Can't figure out how to test async functions"

  Response:
  🔍 Let's debug this together...

  The Issue:
  Testing async functions requires pytest-asyncio

  Solution:
  1. pip install pytest-asyncio
  2. Add @pytest.mark.asyncio decorator
  3. Use async def test_...

  Resources:
  - pytest-asyncio docs: [link]
  ```

---

### Evaluation & Adaptation

#### `/evaluate`
Run full evaluation of progress.

- **Agent**: Evaluator
- **Input**: All memory files, repo signals
- **Output**: Evaluation report with scores
- **Runs**: `python .claude/path-engine/evaluate.py`
- **Example**:
  ```
  /evaluate

  Response:
  📊 Evaluation Report

  Scores:
  - Completion: 85%
  - Quality: 78%
  - Consistency: 90%
  - Growth: 82%
  - Engagement: 88%

  Overall: 84% (On Track)

  Recommendations:
  - Focus on test coverage for quality improvement
  ```

#### `/adapt-path`
Propose changes to learning path.

- **Agent**: Evaluator (with Coach support)
- **Input**: Evaluation results
- **Output**: Adaptation proposals
- **Runs**: `python .claude/path-engine/adapt.py`

#### `/report`
Generate progress report and update tracker.

- **Agent**: Evaluator
- **Input**: Evaluation data
- **Output**: Updated tracker.md
- **Runs**: `python .claude/path-engine/report.py`

---

## Command Routing Table

| Command | Primary Agent | Supporting Agent | Hooks |
|---------|--------------|------------------|-------|
| `/status` | Evaluator | — | — |
| `/plan-week` | Planner | Coach | — |
| `/start-week` | Planner | — | `pre_week_start.sh` |
| `/ship-mvp` | Builder | Reviewer | — |
| `/harden` | Builder | Reviewer | — |
| `/publish` | Builder | Coach | `pre_publish_check.sh` |
| `/retro` | Coach | Evaluator | `post_week_review.sh` |
| `/evaluate` | Evaluator | — | — |
| `/adapt-path` | Evaluator | Coach | — |
| `/add-best-practice` | Coach | — | — |
| `/debug-learning` | Coach | Researcher | — |
| `/report` | Evaluator | — | — |

---

## Adding New Commands

To add a new command:

1. Define in this catalog with all fields
2. Specify which agent handles it
3. Document input/output
4. Add examples
5. Update routing table

Commands must be actionable and produce artifacts.
