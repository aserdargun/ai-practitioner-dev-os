#!/bin/bash
set -e

# post_week_review.sh - Close out a week and prepare for retrospective
# When to use: Friday afternoon, or whenever you finish a week

echo "=== Post-Week Review Hook ==="
echo ""

# Get current date info
CURRENT_DATE=$(date +%Y-%m-%d)
WEEK_NUM=$(date +%V)

# Paths
REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
MEMORY_DIR="$REPO_ROOT/.claude/memory"
JOURNAL_DIR="$REPO_ROOT/paths/advanced/journal"

# 1. Prompt for quick reflection
echo "Quick reflection (press Enter to skip):"
echo ""
read -p "What went well this week? " WENT_WELL
read -p "What could be improved? " IMPROVE
read -p "Key learning? " KEY_LEARNING

# 2. Append to progress log
PROGRESS_LOG="$MEMORY_DIR/progress_log.jsonl"
echo ""
echo "Logging week end to progress log..."

# Escape quotes for JSON
WENT_WELL_ESCAPED=$(echo "$WENT_WELL" | sed 's/"/\\"/g')
IMPROVE_ESCAPED=$(echo "$IMPROVE" | sed 's/"/\\"/g')
KEY_LEARNING_ESCAPED=$(echo "$KEY_LEARNING" | sed 's/"/\\"/g')

cat >> "$PROGRESS_LOG" << EOF
{"timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)", "type": "week_end", "week": $WEEK_NUM, "went_well": "$WENT_WELL_ESCAPED", "improve": "$IMPROVE_ESCAPED", "key_learning": "$KEY_LEARNING_ESCAPED"}
EOF

echo "Added entry to $PROGRESS_LOG"

# 3. Update week journal if it exists
WEEK_FILE="$JOURNAL_DIR/week-$WEEK_NUM.md"
if [ -f "$WEEK_FILE" ]; then
    echo ""
    echo "Updating week journal..."

    # Check if reflection section already filled
    if grep -q "To be completed at week end" "$WEEK_FILE"; then
        # Replace placeholder with actual reflection
        if [ -n "$WENT_WELL" ] || [ -n "$IMPROVE" ] || [ -n "$KEY_LEARNING" ]; then
            sed -i.bak "s/_To be completed at week end\.\.\._/### What went well\n$WENT_WELL\n\n### What to improve\n$IMPROVE\n\n### Key learning\n$KEY_LEARNING/" "$WEEK_FILE"
            rm -f "$WEEK_FILE.bak"
            echo "Updated reflection in $WEEK_FILE"
        fi
    else
        echo "Reflection already recorded in $WEEK_FILE"
    fi
fi

# 4. Show summary
echo ""
echo "=== Week $WEEK_NUM Summary ==="
echo ""

# Count commits this week
COMMITS_THIS_WEEK=$(git log --since="7 days ago" --oneline 2>/dev/null | wc -l || echo "0")
echo "Commits this week: $COMMITS_THIS_WEEK"

# Count progress log entries this week
ENTRIES_THIS_WEEK=$(grep -c "\"week\": $WEEK_NUM" "$PROGRESS_LOG" 2>/dev/null || echo "0")
echo "Progress log entries: $ENTRIES_THIS_WEEK"

echo ""
echo "=== Next Steps ==="
echo ""
echo "1. Run /retro for a detailed retrospective"
echo "2. Run /evaluate if end of month"
echo "3. Run pre_week_start.sh when you're ready for next week"
echo ""
