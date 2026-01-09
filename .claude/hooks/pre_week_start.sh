#!/bin/bash
set -e

# pre_week_start.sh - Prepare for a new week of learning
# When to use: Monday morning, or whenever you start a new week

echo "=== Pre-Week Start Hook ==="
echo ""

# Get current date info
CURRENT_DATE=$(date +%Y-%m-%d)
WEEK_NUM=$(date +%V)

# Paths
REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
TRACKER_PATH="$REPO_ROOT/paths/advanced/tracker.md"
JOURNAL_DIR="$REPO_ROOT/paths/advanced/journal"
MEMORY_DIR="$REPO_ROOT/.claude/memory"

# 1. Create week plan stub if it doesn't exist
WEEK_FILE="$JOURNAL_DIR/week-$WEEK_NUM.md"
if [ ! -f "$WEEK_FILE" ]; then
    echo "Creating week plan stub: $WEEK_FILE"
    cat > "$WEEK_FILE" << EOF
# Week $WEEK_NUM Plan

**Date**: $CURRENT_DATE
**Status**: In Progress

## Goals This Week

- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

## Daily Tasks

### Monday
- [ ] Task 1

### Tuesday
- [ ] Task 2

### Wednesday
- [ ] Task 3

### Thursday
- [ ] Task 4

### Friday
- [ ] Review & Retro

## Notes

_Add notes as the week progresses..._

## End of Week Reflection

_To be completed at week end..._
EOF
    echo "Created $WEEK_FILE"
else
    echo "Week plan already exists: $WEEK_FILE"
fi

# 2. Append start event to progress log
PROGRESS_LOG="$MEMORY_DIR/progress_log.jsonl"
echo "Logging week start to progress log..."
echo "{\"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\", \"type\": \"week_start\", \"week\": $WEEK_NUM}" >> "$PROGRESS_LOG"

# 3. Display current month goals
echo ""
echo "=== Current Month Goals ==="
echo ""

# Find current month directory (most recently modified)
CURRENT_MONTH=$(ls -td "$REPO_ROOT/paths/advanced/month-"* 2>/dev/null | head -1)
if [ -n "$CURRENT_MONTH" ] && [ -f "$CURRENT_MONTH/README.md" ]; then
    # Print first 30 lines of month README
    head -30 "$CURRENT_MONTH/README.md"
    echo ""
    echo "... (see full goals in $CURRENT_MONTH/README.md)"
else
    echo "No month README found. Run /status to check your position."
fi

echo ""
echo "=== Ready! ==="
echo ""
echo "Next steps:"
echo "1. Review your week plan: $WEEK_FILE"
echo "2. Run /status to check current progress"
echo "3. Start with /plan-week to refine your plan"
echo ""
