#!/bin/bash
# Post-Week Review Hook
# Runs after weekly retrospective to collect metrics and update state

set -e

echo "=========================================="
echo "  Post-Week Review Hook"
echo "=========================================="
echo ""

# Get current date and week info
CURRENT_DATE=$(date +%Y-%m-%d)
WEEK_NUM=$(date +%V)
echo "Date: $CURRENT_DATE"
echo "Week: $WEEK_NUM (ending)"
echo ""

# Count commits this week
echo "Collecting week metrics..."
if [ -d ".git" ]; then
    WEEK_START=$(date -d "last monday" +%Y-%m-%d 2>/dev/null || date -v-monday +%Y-%m-%d 2>/dev/null || echo "")
    if [ -n "$WEEK_START" ]; then
        COMMITS=$(git log --oneline --since="$WEEK_START" 2>/dev/null | wc -l)
        echo "  Commits this week: $COMMITS"
    else
        COMMITS=$(git log --oneline -n 20 | wc -l)
        echo "  Recent commits: $COMMITS"
    fi

    # Files changed
    FILES_CHANGED=$(git diff --stat HEAD~5 2>/dev/null | tail -1 || echo "Unable to determine")
    echo "  Recent changes: $FILES_CHANGED"
else
    echo "  Not a git repository, skipping commit metrics"
fi
echo ""

# Check test status
echo "Running tests..."
if [ -d "templates" ]; then
    FAILED=0
    for template_dir in templates/*/; do
        if [ -f "$template_dir/pyproject.toml" ]; then
            template_name=$(basename "$template_dir")
            if command -v pytest &> /dev/null; then
                if pytest "$template_dir" --quiet --tb=no 2>/dev/null; then
                    echo "  ✓ $template_name tests passing"
                else
                    echo "  ✗ $template_name tests failing"
                    FAILED=1
                fi
            fi
        fi
    done
    if [ "$FAILED" -eq 0 ]; then
        echo "  All template tests passing!"
    fi
else
    echo "  No templates directory found"
fi
echo ""

# Count progress log entries this week
echo "Progress log summary..."
MEMORY_DIR=".claude/memory"
if [ -f "$MEMORY_DIR/progress_log.jsonl" ]; then
    TOTAL_ENTRIES=$(wc -l < "$MEMORY_DIR/progress_log.jsonl")
    echo "  Total progress entries: $TOTAL_ENTRIES"

    # Count recent entries (approximation - entries with today's date)
    TODAY=$(date +%Y-%m-%d)
    if grep -c "$TODAY" "$MEMORY_DIR/progress_log.jsonl" > /dev/null 2>&1; then
        TODAY_ENTRIES=$(grep -c "$TODAY" "$MEMORY_DIR/progress_log.jsonl")
        echo "  Entries today: $TODAY_ENTRIES"
    fi
fi
echo ""

# Best practices check
echo "Best practices captured..."
if [ -f "$MEMORY_DIR/best_practices.md" ]; then
    BP_COUNT=$(grep -c "^###" "$MEMORY_DIR/best_practices.md" 2>/dev/null || echo "0")
    echo "  Total best practices: $BP_COUNT"
fi
echo ""

# Generate summary for journal
echo "=========================================="
echo "  Week Summary"
echo "=========================================="
echo ""
echo "Add these metrics to your retrospective:"
echo ""
echo "- Commits: ${COMMITS:-N/A}"
echo "- Tests: $([ "$FAILED" -eq 0 ] && echo "Passing" || echo "Some failures")"
echo "- Progress entries: ${TOTAL_ENTRIES:-N/A}"
echo "- Best practices: ${BP_COUNT:-N/A}"
echo ""

echo "=========================================="
echo "  Post-Week Review Complete"
echo "=========================================="
echo ""
echo "Run /evaluate to see your weekly scores."
echo "Run /adapt-path if you need curriculum adjustments."
