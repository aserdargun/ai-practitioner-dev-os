#!/bin/bash
# post_week_review.sh - Run at the end of each week
#
# Purpose:
#   - Prompt for retrospective reflection
#   - Update progress log with week summary
#   - Trigger evaluation
#
# Usage:
#   bash .claude/hooks/post_week_review.sh
#
# Manual fallback (if you can't run .sh scripts):
#   1. Open your week journal and fill in the retrospective section
#   2. Add entry to .claude/memory/progress_log.jsonl
#   3. Run: python .claude/path-engine/evaluate.py

set -e

# Configuration
LEARNER_LEVEL="Beginner"
MEMORY_DIR=".claude/memory"
PROGRESS_LOG="${MEMORY_DIR}/progress_log.jsonl"

# Get current date info
TODAY=$(date +%Y-%m-%d)
WEEK_NUM=$(date +%V)
YEAR=$(date +%Y)
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)

echo "=========================================="
echo "  Post-Week Review Hook"
echo "  Date: ${TODAY}"
echo "  Week: ${WEEK_NUM}"
echo "=========================================="

# Prompt for reflection
echo ""
echo "Time for your weekly reflection!"
echo ""

read -p "What went well this week? " went_well
read -p "What could be improved? " to_improve
read -p "What did you learn? " learned
read -p "How are you feeling? (1-5): " mood

# Validate mood
if ! [[ "$mood" =~ ^[1-5]$ ]]; then
    mood=3
fi

# Escape quotes for JSON
went_well=$(echo "$went_well" | sed 's/"/\\"/g')
to_improve=$(echo "$to_improve" | sed 's/"/\\"/g')
learned=$(echo "$learned" | sed 's/"/\\"/g')

# Add week end entry to progress log
echo ""
echo "Saving reflection to progress log..."
ENTRY=$(cat << EOF
{"timestamp": "${TIMESTAMP}", "event": "week_end", "week": ${WEEK_NUM}, "year": ${YEAR}, "date": "${TODAY}", "level": "${LEARNER_LEVEL}", "reflection": {"went_well": "${went_well}", "to_improve": "${to_improve}", "learned": "${learned}", "mood": ${mood}}}
EOF
)
echo "${ENTRY}" >> "${PROGRESS_LOG}"

echo "Reflection saved!"

# Run evaluation
echo ""
echo "Running evaluation..."
if [ -f ".claude/path-engine/evaluate.py" ]; then
    python .claude/path-engine/evaluate.py
else
    echo "Evaluation script not found. Run /evaluate in Claude."
fi

echo ""
echo "Week ${WEEK_NUM} complete!"
echo ""
echo "Next steps:"
echo "  1. Review your evaluation results"
echo "  2. Run /adapt-path if changes are needed"
echo "  3. Run /report to update your tracker"
echo "  4. Take a break - you've earned it!"
echo ""
echo "=========================================="
