#!/bin/bash
# post_week_review.sh
# Run at the end of each week to prompt retrospective and update logs

set -e

# Configuration
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
MEMORY_DIR="$REPO_ROOT/.claude/memory"
PATHS_DIR="$REPO_ROOT/paths/intermediate"
JOURNAL_DIR="$PATHS_DIR/journal"
PROGRESS_LOG="$MEMORY_DIR/progress_log.jsonl"
BEST_PRACTICES="$MEMORY_DIR/best_practices.md"

# Get current date info
CURRENT_DATE=$(date +%Y-%m-%d)
CURRENT_WEEK=$(date +%V)
CURRENT_YEAR=$(date +%Y)
WEEK_FILE="$JOURNAL_DIR/week-${CURRENT_YEAR}-${CURRENT_WEEK}.md"

echo "=== Post-Week Review Hook ==="
echo "Date: $CURRENT_DATE"
echo "Week: $CURRENT_WEEK"
echo ""

# Step 1: Check if week journal exists
if [ ! -f "$WEEK_FILE" ]; then
    echo "Warning: Week journal not found at $WEEK_FILE"
    echo "Creating placeholder..."
    mkdir -p "$JOURNAL_DIR"
    echo "# Week ${CURRENT_WEEK} — ${CURRENT_DATE}" > "$WEEK_FILE"
    echo "" >> "$WEEK_FILE"
    echo "*Created during post-week review*" >> "$WEEK_FILE"
fi

# Step 2: Prompt for reflection
echo "=== Week Reflection Prompts ==="
echo ""
echo "Please consider the following questions:"
echo ""
echo "1. WHAT WENT WELL this week?"
echo "   - What accomplishments are you proud of?"
echo "   - What worked better than expected?"
echo ""
echo "2. WHAT COULD BE IMPROVED?"
echo "   - What took longer than expected?"
echo "   - What obstacles did you face?"
echo ""
echo "3. KEY LEARNINGS"
echo "   - What new skills or knowledge did you gain?"
echo "   - What would you do differently next time?"
echo ""
echo "4. BEST PRACTICES to capture?"
echo "   - Any insights worth preserving in best_practices.md?"
echo ""

# Step 3: Log week end to progress log
echo "Logging week end event..."
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "{\"timestamp\": \"$TIMESTAMP\", \"event\": \"week_end\", \"week\": \"$CURRENT_WEEK\", \"year\": \"$CURRENT_YEAR\"}" >> "$PROGRESS_LOG"
echo "✓ Progress log updated"

# Step 4: Show summary
echo ""
echo "=== Week Summary ==="
echo ""
echo "Journal file: $WEEK_FILE"
echo "Progress log: $PROGRESS_LOG"
echo "Best practices: $BEST_PRACTICES"
echo ""

# Step 5: Git status check
echo "=== Git Status ==="
if git status --short 2>/dev/null; then
    echo ""
    echo "Remember to commit your week's work!"
else
    echo "Not in a git repository"
fi

echo ""
echo "=== Week Review Complete ==="
echo ""
echo "Next steps:"
echo "1. Update your week journal with reflections: $WEEK_FILE"
echo "2. Run /retro for guided retrospective"
echo "3. Run /evaluate for performance assessment"
echo "4. Run /add-best-practice if you have insights to capture"
echo "5. Commit your changes"
