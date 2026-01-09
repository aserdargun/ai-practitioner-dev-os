#!/bin/bash
# post_week_review.sh
# Run this after completing a learning week

set -e

# Configuration
PATHS_DIR="paths/beginner"
JOURNAL_DIR="$PATHS_DIR/journal"
TRACKER_FILE="$PATHS_DIR/tracker.md"
PROGRESS_LOG=".claude/memory/progress_log.jsonl"
BEST_PRACTICES=".claude/memory/best_practices.md"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo "=========================================="
echo "  Post-Week Review Hook"
echo "=========================================="
echo ""

# Get week info
read -p "Which month? (1-12): " MONTH_NUM
read -p "Which week? (1-4): " WEEK_NUM

MONTH_FORMATTED=$(printf "%02d" $MONTH_NUM)
WEEK_FILE="$JOURNAL_DIR/month-${MONTH_FORMATTED}-week-${WEEK_NUM}.md"

# Check if week file exists
if [ ! -f "$WEEK_FILE" ]; then
    echo "Week file not found: $WEEK_FILE"
    echo "Please create the week file first with pre_week_start.sh"
    exit 1
fi

echo -e "${BLUE}Running Week ${WEEK_NUM} Retrospective...${NC}"
echo ""

# Prompt for reflections
echo "Let's reflect on your week."
echo ""

echo -e "${YELLOW}What did you accomplish this week?${NC}"
read -p "> " ACCOMPLISHED
echo ""

echo -e "${YELLOW}What was challenging?${NC}"
read -p "> " CHALLENGING
echo ""

echo -e "${YELLOW}What did you learn?${NC}"
read -p "> " LEARNED
echo ""

echo -e "${YELLOW}Any best practices to capture? (Enter to skip)${NC}"
read -p "> " BEST_PRACTICE
echo ""

echo -e "${YELLOW}How would you rate this week? (1-5)${NC}"
read -p "> " RATING
echo ""

# Update week file with reflections
echo -e "${YELLOW}Updating week journal...${NC}"

# Check if Week Summary section exists and update it
if grep -q "## Week Summary" "$WEEK_FILE"; then
    # Append to the file (simplified - in real use, would insert at right location)
    cat >> "$WEEK_FILE" << EOF

---
*Retrospective completed on $(date +%Y-%m-%d)*

### Accomplishments
${ACCOMPLISHED}

### Challenges
${CHALLENGING}

### Learnings
${LEARNED}

### Week Rating: ${RATING}/5
EOF
    echo -e "${GREEN}Updated week journal${NC}"
fi

# Update tracker
echo -e "${YELLOW}Updating tracker...${NC}"
# Mark week as completed
sed -i.bak "s/Month ${MONTH_NUM}, Week ${WEEK_NUM}.*Status: In Progress/Month ${MONTH_NUM}, Week ${WEEK_NUM} - Status: Completed/" "$TRACKER_FILE" 2>/dev/null || true
echo -e "${GREEN}Updated tracker${NC}"

# Log completion event
echo -e "${YELLOW}Logging completion...${NC}"
mkdir -p "$(dirname $PROGRESS_LOG)"
cat >> "$PROGRESS_LOG" << EOF
{"timestamp": "$(date -Iseconds)", "event": "week_completed", "month": ${MONTH_NUM}, "week": ${WEEK_NUM}, "rating": ${RATING}}
{"timestamp": "$(date -Iseconds)", "event": "retro_completed", "month": ${MONTH_NUM}, "week": ${WEEK_NUM}, "learned": "${LEARNED}"}
EOF
echo -e "${GREEN}Logged to progress_log.jsonl${NC}"

# Add best practice if provided
if [ -n "$BEST_PRACTICE" ]; then
    echo -e "${YELLOW}Adding best practice...${NC}"
    mkdir -p "$(dirname $BEST_PRACTICES)"
    echo "" >> "$BEST_PRACTICES"
    echo "### $(date +%Y-%m-%d) — Month ${MONTH_NUM}, Week ${WEEK_NUM}" >> "$BEST_PRACTICES"
    echo "${BEST_PRACTICE}" >> "$BEST_PRACTICES"
    echo -e "${GREEN}Added to best_practices.md${NC}"
fi

# Summary
echo ""
echo "=========================================="
echo -e "${GREEN}Week ${WEEK_NUM} of Month ${MONTH_NUM} completed!${NC}"
echo "=========================================="
echo ""
echo "Summary:"
echo "  - Rating: ${RATING}/5"
echo "  - Journal updated: $WEEK_FILE"
echo "  - Progress logged"
if [ -n "$BEST_PRACTICE" ]; then
    echo "  - Best practice captured"
fi
echo ""
echo "Next steps:"
echo "1. Run /evaluate to see your scores"
echo "2. Run /plan-week for next week"
echo "3. Take a break - you earned it!"
echo ""

# Manual Fallback Instructions
: << 'MANUAL_FALLBACK'
If you cannot run this script, do the following manually:

1. Update your week journal file:
   - Open paths/beginner/journal/month-XX-week-Y.md
   - Fill in the Week Summary section

2. Update the tracker:
   - Open paths/beginner/tracker.md
   - Mark the week as Completed

3. Log the events:
   - Open .claude/memory/progress_log.jsonl
   - Add: {"timestamp": "...", "event": "week_completed", "month": X, "week": Y, "rating": Z}

4. Add best practice (if any):
   - Open .claude/memory/best_practices.md
   - Add the learning with date and context
MANUAL_FALLBACK
