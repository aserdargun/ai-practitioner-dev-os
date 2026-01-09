#!/bin/bash
# pre_week_start.sh
# Run this before starting a new learning week

set -e

# Configuration
PATHS_DIR="paths/beginner"
JOURNAL_DIR="$PATHS_DIR/journal"
TRACKER_FILE="$PATHS_DIR/tracker.md"
PROGRESS_LOG=".claude/memory/progress_log.jsonl"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=========================================="
echo "  Pre-Week Start Hook"
echo "=========================================="
echo ""

# Get current date info
CURRENT_DATE=$(date +%Y-%m-%d)
CURRENT_MONTH=$(date +%m)
WEEK_NUM=${1:-$(date +%V)}

# Ask for week info if not provided
if [ -z "$1" ]; then
    read -p "Which month are you in? (1-12): " MONTH_NUM
    read -p "Which week of the month? (1-4): " WEEK_OF_MONTH
else
    MONTH_NUM=$1
    WEEK_OF_MONTH=$2
fi

# Format month with leading zero
MONTH_FORMATTED=$(printf "%02d" $MONTH_NUM)
WEEK_FILE="$JOURNAL_DIR/month-${MONTH_FORMATTED}-week-${WEEK_OF_MONTH}.md"

echo -e "${YELLOW}Creating week journal file...${NC}"

# Create journal directory if needed
mkdir -p "$JOURNAL_DIR"

# Create week file from template if it doesn't exist
if [ ! -f "$WEEK_FILE" ]; then
    cat > "$WEEK_FILE" << EOF
# Month ${MONTH_NUM} — Week ${WEEK_OF_MONTH}

**Started**: ${CURRENT_DATE}

## Goals
- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

## Daily Log

### Day 1 ($(date +%A))
**Planned**:
-

**Completed**:
-

**Notes**:


### Day 2
**Planned**:
-

**Completed**:
-

**Notes**:


### Day 3
**Planned**:
-

**Completed**:
-

**Notes**:


### Day 4
**Planned**:
-

**Completed**:
-

**Notes**:


### Day 5
**Planned**:
-

**Completed**:
-

**Notes**:


## Week Summary
(Fill in at end of week)

### What I Accomplished


### What Was Challenging


### What I Learned


### Best Practices to Capture

EOF
    echo -e "${GREEN}Created: $WEEK_FILE${NC}"
else
    echo "Week file already exists: $WEEK_FILE"
fi

# Update tracker
echo -e "${YELLOW}Updating tracker...${NC}"
if [ -f "$TRACKER_FILE" ]; then
    # Check if week entry exists
    if ! grep -q "Month ${MONTH_NUM}, Week ${WEEK_OF_MONTH}" "$TRACKER_FILE"; then
        echo "" >> "$TRACKER_FILE"
        echo "### Month ${MONTH_NUM}, Week ${WEEK_OF_MONTH}" >> "$TRACKER_FILE"
        echo "- **Started**: ${CURRENT_DATE}" >> "$TRACKER_FILE"
        echo "- **Status**: In Progress" >> "$TRACKER_FILE"
        echo -e "${GREEN}Added week entry to tracker${NC}"
    else
        echo "Week entry already exists in tracker"
    fi
fi

# Log event
echo -e "${YELLOW}Logging event...${NC}"
mkdir -p "$(dirname $PROGRESS_LOG)"
echo "{\"timestamp\": \"$(date -Iseconds)\", \"event\": \"week_started\", \"month\": ${MONTH_NUM}, \"week\": ${WEEK_OF_MONTH}}" >> "$PROGRESS_LOG"
echo -e "${GREEN}Logged to progress_log.jsonl${NC}"

# Summary
echo ""
echo "=========================================="
echo -e "${GREEN}Week ${WEEK_OF_MONTH} of Month ${MONTH_NUM} is ready!${NC}"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Edit your goals in: $WEEK_FILE"
echo "2. Run /plan-week with Claude to create detailed plan"
echo "3. Start working on your first task"
echo ""
echo "Quick commands:"
echo "  /status    - Check your progress"
echo "  /plan-week - Create detailed plan"
echo ""

# Manual Fallback Instructions
: << 'MANUAL_FALLBACK'
If you cannot run this script, do the following manually:

1. Create the week journal file:
   - Copy paths/beginner/journal/weekly-template.md
   - Rename to month-XX-week-Y.md (e.g., month-03-week-2.md)
   - Fill in the date and initial goals

2. Update the tracker:
   - Open paths/beginner/tracker.md
   - Add a new section for the week

3. Log the event:
   - Open .claude/memory/progress_log.jsonl
   - Add: {"timestamp": "YYYY-MM-DDTHH:MM:SS", "event": "week_started", "month": X, "week": Y}
MANUAL_FALLBACK
