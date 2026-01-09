# Hooks

Shell scripts that automate workflow events in your learning journey.

## Available Hooks

| Hook | Purpose | When |
|------|---------|------|
| [pre_week_start.sh](pre_week_start.sh) | Initialize new week | Start of each week |
| [post_week_review.sh](post_week_review.sh) | Prompt retrospective | End of each week |
| [pre_publish_check.sh](pre_publish_check.sh) | Quality gates | Before publishing |

## How to Use

### Running Hooks

```bash
# From repository root
bash .claude/hooks/pre_week_start.sh
bash .claude/hooks/post_week_review.sh
bash .claude/hooks/pre_publish_check.sh
```

### Integration with Commands

Hooks are automatically suggested by commands:
- `/start-week` → suggests `pre_week_start.sh`
- `/retro` → suggests `post_week_review.sh`
- `/publish` → suggests `pre_publish_check.sh`

## Cross-Platform Compatibility

These hooks are shell scripts designed for:
- **Linux**: Works natively
- **macOS**: Works natively
- **Windows**: Use WSL or Git Bash

### Manual Fallback

If you cannot run `.sh` scripts, see `docs/hooks.md` for step-by-step manual commands that accomplish the same tasks.

## Hook Output

Hooks write to:
- `.claude/memory/progress_log.jsonl` — Timestamped events
- `paths/intermediate/tracker.md` — Progress updates
- `paths/intermediate/journal/` — Journal entries

## Customization

Feel free to modify hooks for your workflow:
1. Edit the `.sh` file
2. Test changes locally
3. Commit your customizations

## Related Documentation

- [docs/hooks.md](../../docs/hooks.md) — User guide with manual fallbacks
- [commands/catalog.md](../commands/catalog.md) — Commands that invoke hooks
