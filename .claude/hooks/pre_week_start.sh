#!/bin/bash
# pre_week_start.sh
# Run at the start of each week to initialize the week's work

set -e

# Configuration
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
MEMORY_DIR="$REPO_ROOT/.claude/memory"
PATHS_DIR="$REPO_ROOT/paths/intermediate"
JOURNAL_DIR="$PATHS_DIR/journal"
TRACKER_FILE="$PATHS_DIR/tracker.md"
PROGRESS_LOG="$MEMORY_DIR/progress_log.jsonl"

# Get current date info
CURRENT_DATE=$(date +%Y-%m-%d)
CURRENT_WEEK=$(date +%V)
CURRENT_YEAR=$(date +%Y)
WEEK_FILE="$JOURNAL_DIR/week-${CURRENT_YEAR}-${CURRENT_WEEK}.md"

echo "=== Pre-Week Start Hook ==="
echo "Date: $CURRENT_DATE"
echo "Week: $CURRENT_WEEK"
echo ""

# Step 1: Create week journal entry if not exists
if [ ! -f "$WEEK_FILE" ]; then
    echo "Creating week journal entry: $WEEK_FILE"
    cat > "$WEEK_FILE" << EOF
# Week ${CURRENT_WEEK} — ${CURRENT_DATE}

## Week Goals
- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

## Daily Log

### Monday
-

### Tuesday
-

### Wednesday
-

### Thursday
-

### Friday
-

## Blockers
- None yet

## Learnings
-

## End of Week Reflection
*To be filled at week end*
EOF
    echo "✓ Week journal created"
else
    echo "✓ Week journal already exists"
fi

# Step 2: Log week start to progress log
echo "Logging week start event..."
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "{\"timestamp\": \"$TIMESTAMP\", \"event\": \"week_start\", \"week\": \"$CURRENT_WEEK\", \"year\": \"$CURRENT_YEAR\"}" >> "$PROGRESS_LOG"
echo "✓ Progress log updated"

# Step 3: Check tracker status
echo ""
echo "=== Current Status ==="
if [ -f "$TRACKER_FILE" ]; then
    echo "Tracker file exists: $TRACKER_FILE"
    # Show first 20 lines of tracker
    head -20 "$TRACKER_FILE"
else
    echo "Warning: Tracker file not found. Run evaluate.py and report.py to generate."
fi

echo ""
echo "=== Week Start Complete ==="
echo ""
echo "Next steps:"
echo "1. Review your week goals in: $WEEK_FILE"
echo "2. Run /plan-week to get detailed task breakdown"
echo "3. Run /status for current progress snapshot"
