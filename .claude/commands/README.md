# Commands

This folder contains the command definitions for the AI Practitioner Learning OS.

## Source of Truth

The canonical reference for all commands is [catalog.md](catalog.md).

## Overview

Commands are the primary interface for learners to interact with the system. Each command:

- Has a specific purpose
- Is routed to an agent
- Takes defined inputs
- Produces expected outputs

## Quick Reference

| Command | Agent | Purpose |
|---------|-------|---------|
| `/status` | Planner | Check progress and blockers |
| `/plan-week` | Planner | Generate weekly plan |
| `/start-week` | Planner | Initialize new week |
| `/ship-mvp` | Builder | Ship minimal viable product |
| `/harden` | Builder | Add tests and docs |
| `/publish` | Builder | Prepare for demo |
| `/retro` | Coach | Run retrospective |
| `/evaluate` | Evaluator | Score progress |
| `/adapt-path` | Evaluator | Propose path changes |
| `/add-best-practice` | Coach | Capture best practice |
| `/debug-learning` | Coach | Diagnose struggles |
| `/report` | Evaluator | Generate report |

## Documentation

For detailed usage guide, see [docs/commands.md](../../docs/commands.md).
