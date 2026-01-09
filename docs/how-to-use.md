# How to Use the Learning OS

This guide covers day-to-day usage of the AI Practitioner Learning OS.

## Quick Start

1. Open your dashboard: `paths/advanced/README.md`
2. Run `/status` to see where you are
3. Run `/plan-week` to create your week plan
4. Start building!

## The System Loop

The learning OS follows a continuous loop:

```
Execute → Log → Evaluate → Adapt → Repeat
```

### 1. Execute (Daily/Weekly)

Work on your current month's project:
- Follow the week plan
- Use templates from `templates/`
- Reference skills from `.claude/skills/`

### 2. Log (Ongoing)

Record your progress:
- Progress events → `.claude/memory/progress_log.jsonl`
- Important decisions → `.claude/memory/decisions.jsonl`
- Learned patterns → `.claude/memory/best_practices.md`

### 3. Evaluate (Weekly/Monthly)

Assess your progress:
```bash
python .claude/path-engine/evaluate.py
```

### 4. Adapt (As Needed)

Get recommendations:
```bash
python .claude/path-engine/adapt.py
```

**Remember**: All adaptations require your explicit approval.

## Weekly Cadence

### Week 1: Explore & Plan
- Understand the month's goals
- Research technologies
- Create detailed week plans
- Set up project scaffolding

### Week 2: Build Core
- Implement main functionality
- Write initial tests
- Document as you go

### Week 3: Iterate & Test
- Complete remaining features
- Comprehensive testing
- Code review with `/harden`

### Week 4: Ship & Reflect
- Finalize MVP with `/ship-mvp`
- Publish with `/publish`
- Retrospective with `/retro`
- Evaluate with `/evaluate`

## Daily Workflow

### Morning
```
/status                    # Where am I?
# Review today's tasks from week plan
```

### During Work
```
# Build, test, document
# Log significant events to progress log
/debug-learning           # If stuck
```

### End of Day
```
/status                    # Quick progress check
# Update progress log
```

## Using Commands

Commands are your interface to the learning OS.

### Planning
- `/status` - Check current progress
- `/plan-week` - Create/review week plan

### Building
- `/start-week` - Begin week execution
- `/ship-mvp` - Finalize deliverables

### Quality
- `/harden` - Code review and hardening
- `/publish` - Prepare for external sharing

### Reflection
- `/retro` - Run retrospective
- `/evaluate` - Formal evaluation
- `/adapt-path` - Get adaptation proposals

### Help
- `/debug-learning` - Get unstuck
- `/add-best-practice` - Capture learning

See [commands.md](commands.md) for the complete guide.

## Logging Progress

### Automatic Logging

Use hooks for consistent logging:
```bash
bash .claude/hooks/pre_week_start.sh
bash .claude/hooks/post_week_review.sh
```

### Manual Logging

Append to progress log:
```bash
echo '{"timestamp": "2026-01-09T14:00:00Z", "type": "task_complete", "task": "Implemented feature X"}' >> .claude/memory/progress_log.jsonl
```

### Event Types

| Type | When to Log |
|------|-------------|
| `task_complete` | Task finished |
| `blocker` | Got stuck |
| `blocker_resolved` | Unblocked |
| `milestone` | Major achievement |
| `decision` | Important choice |

## Requesting Path Changes

If you need to change your learning path:

1. Run evaluation:
   ```bash
   python .claude/path-engine/evaluate.py
   ```

2. Get proposals:
   ```bash
   python .claude/path-engine/adapt.py
   ```

3. Review proposals (printed to stdout)

4. Apply approved changes manually (or with Claude's help)

5. Log the decision:
   ```bash
   echo '{"timestamp": "...", "type": "adaptation", "applied": "..."}' >> .claude/memory/decisions.jsonl
   ```

## Capturing Best Practices

When you learn something valuable:

1. Use the command:
   ```
   /add-best-practice "Always test with real data before committing to an approach"
   ```

2. Or append manually:
   ```markdown
   ### My New Practice
   > Description of the practice...
   > When: When to apply it
   > Source: Where you learned it
   ```

## Running the Engine Locally

### Evaluate
```bash
python .claude/path-engine/evaluate.py
python .claude/path-engine/evaluate.py --month 3
python .claude/path-engine/evaluate.py --json
```

### Adapt
```bash
python .claude/path-engine/adapt.py
python .claude/path-engine/adapt.py --month 3
python .claude/path-engine/adapt.py --json
```

### Report
```bash
python .claude/path-engine/report.py --dry-run  # Preview
python .claude/path-engine/report.py            # Update tracker
```

## Common Scenarios

### Starting a New Month

1. Review month README: `paths/advanced/month-XX/README.md`
2. Run `/plan-week` for Week 1
3. Set up project from templates
4. Update `learner_profile.json` with `current_month`

### Mid-Month Check-in

1. Run `/status`
2. Run evaluation: `python .claude/path-engine/evaluate.py`
3. Adjust week plan if needed

### Feeling Stuck

1. Run `/debug-learning`
2. Describe the blocker
3. Try suggested experiments
4. Log the blocker (and resolution) to progress log

### End of Month

1. Complete remaining DoD items
2. Run `/ship-mvp` and `/harden`
3. Run `/publish` for external sharing
4. Run `/retro` for reflection
5. Run `/evaluate` for formal assessment
6. Update tracker: `python .claude/path-engine/report.py`
7. Start next month

## Tips for Success

1. **Log consistently** - Progress log is your learning journal
2. **Reflect weekly** - `/retro` helps cement learning
3. **Ask for help early** - `/debug-learning` is your friend
4. **Capture patterns** - Best practices compound over time
5. **Trust the process** - The system adapts to you

## Getting Help

- Commands guide: [commands.md](commands.md)
- Agents overview: [agents.md](agents.md)
- Evaluation rubric: [evaluation/rubric.md](evaluation/rubric.md)
- Memory system: [memory-system.md](memory-system.md)
