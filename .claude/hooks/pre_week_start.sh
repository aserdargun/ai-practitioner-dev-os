#!/bin/bash
# Pre-Week Start Hook
# Runs at the beginning of each week to prepare the environment

set -e

echo "=========================================="
echo "  Pre-Week Start Hook"
echo "=========================================="
echo ""

# Get current date and week info
CURRENT_DATE=$(date +%Y-%m-%d)
WEEK_NUM=$(date +%V)
echo "Date: $CURRENT_DATE"
echo "Week: $WEEK_NUM"
echo ""

# Check git status
echo "Checking git status..."
if [ -d ".git" ]; then
    git status --short
    echo ""
else
    echo "Warning: Not a git repository"
fi

# Verify memory files exist
echo "Verifying memory files..."
MEMORY_DIR=".claude/memory"
if [ -f "$MEMORY_DIR/learner_profile.json" ]; then
    echo "  ✓ learner_profile.json exists"
else
    echo "  ✗ learner_profile.json missing"
fi

if [ -f "$MEMORY_DIR/progress_log.jsonl" ]; then
    ENTRIES=$(wc -l < "$MEMORY_DIR/progress_log.jsonl")
    echo "  ✓ progress_log.jsonl exists ($ENTRIES entries)"
else
    echo "  ✗ progress_log.jsonl missing"
fi

if [ -f "$MEMORY_DIR/best_practices.md" ]; then
    echo "  ✓ best_practices.md exists"
else
    echo "  ✗ best_practices.md missing"
fi
echo ""

# Check Python environment
echo "Checking Python environment..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "  ✓ $PYTHON_VERSION"
else
    echo "  ✗ Python3 not found"
fi
echo ""

# Run linting check on templates (if ruff is available)
echo "Running quick lint check..."
if command -v ruff &> /dev/null; then
    if [ -d "templates" ]; then
        ruff check templates/ --quiet && echo "  ✓ No linting errors" || echo "  ! Some linting issues found"
    fi
else
    echo "  - ruff not installed, skipping lint check"
fi
echo ""

# Check for uncommitted changes
echo "Checking for uncommitted work..."
if [ -d ".git" ]; then
    UNCOMMITTED=$(git status --porcelain | wc -l)
    if [ "$UNCOMMITTED" -gt 0 ]; then
        echo "  ! $UNCOMMITTED uncommitted changes found"
        echo "  Consider committing before starting new week"
    else
        echo "  ✓ Working directory clean"
    fi
fi
echo ""

echo "=========================================="
echo "  Pre-Week Start Complete"
echo "=========================================="
echo ""
echo "Ready to start Week $WEEK_NUM!"
echo "Run /plan-week to generate your weekly tasks."
