#!/bin/bash
# pre_week_start.sh - Run at the beginning of each week
#
# Purpose:
#   - Create week plan stub in journal
#   - Update tracker with week start
#   - Run initial status check
#
# Usage:
#   bash .claude/hooks/pre_week_start.sh
#
# Manual fallback (if you can't run .sh scripts):
#   1. Create a new file: paths/Beginner/journal/week-YYYY-MM-DD.md
#   2. Copy template from paths/Beginner/journal/weekly-template.md
#   3. Add entry to .claude/memory/progress_log.jsonl

set -e

# Configuration
LEARNER_LEVEL="Beginner"
JOURNAL_DIR="paths/${LEARNER_LEVEL}/journal"
MEMORY_DIR=".claude/memory"
PROGRESS_LOG="${MEMORY_DIR}/progress_log.jsonl"

# Get current date info
TODAY=$(date +%Y-%m-%d)
WEEK_NUM=$(date +%V)
YEAR=$(date +%Y)
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)

echo "=========================================="
echo "  Pre-Week Start Hook"
echo "  Date: ${TODAY}"
echo "  Week: ${WEEK_NUM}"
echo "=========================================="

# Create journal directory if needed
mkdir -p "${JOURNAL_DIR}"

# Create week journal file
WEEK_FILE="${JOURNAL_DIR}/week-${TODAY}.md"

if [ -f "${WEEK_FILE}" ]; then
    echo "Week journal already exists: ${WEEK_FILE}"
else
    echo "Creating week journal: ${WEEK_FILE}"
    cat > "${WEEK_FILE}" << EOF
# Week ${WEEK_NUM} - ${TODAY}

## Goals for This Week
- [ ] Goal 1
- [ ] Goal 2
- [ ] Goal 3

## Daily Log

### Monday
- Tasks:
- Notes:

### Tuesday
- Tasks:
- Notes:

### Wednesday
- Tasks:
- Notes:

### Thursday
- Tasks:
- Notes:

### Friday
- Tasks:
- Notes:

## Blockers
- None yet

## Resources Used
-

## Notes
-
EOF
    echo "Created week journal"
fi

# Ensure memory directory exists
mkdir -p "${MEMORY_DIR}"

# Add week start entry to progress log
echo "Adding week start to progress log..."
ENTRY=$(cat << EOF
{"timestamp": "${TIMESTAMP}", "event": "week_start", "week": ${WEEK_NUM}, "year": ${YEAR}, "date": "${TODAY}", "level": "${LEARNER_LEVEL}"}
EOF
)
echo "${ENTRY}" >> "${PROGRESS_LOG}"

echo ""
echo "Week ${WEEK_NUM} initialized!"
echo ""
echo "Next steps:"
echo "  1. Open ${WEEK_FILE} and set your goals"
echo "  2. Run /plan-week in Claude to create detailed plan"
echo "  3. Run /status to see current state"
echo ""
echo "=========================================="
