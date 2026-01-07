#!/bin/bash
# pre_publish_check.sh - Run before publishing work
#
# Purpose:
#   - Run tests
#   - Run linter
#   - Check documentation
#   - Validate memory files
#
# Usage:
#   bash .claude/hooks/pre_publish_check.sh
#
# Manual fallback (if you can't run .sh scripts):
#   1. Run: pytest tests/
#   2. Run: ruff check .
#   3. Manually check that README links work
#   4. Validate JSON files are well-formed

set -e

echo "=========================================="
echo "  Pre-Publish Check Hook"
echo "  Date: $(date +%Y-%m-%d)"
echo "=========================================="

ERRORS=0

# Check 1: Run tests
echo ""
echo "[1/4] Running tests..."
if command -v pytest &> /dev/null; then
    if pytest tests/ -q 2>/dev/null; then
        echo "✓ Tests passed"
    else
        echo "✗ Tests failed"
        ERRORS=$((ERRORS + 1))
    fi
else
    echo "⚠ pytest not found, skipping tests"
fi

# Check 2: Run linter
echo ""
echo "[2/4] Running linter..."
if command -v ruff &> /dev/null; then
    if ruff check . --quiet 2>/dev/null; then
        echo "✓ Linting passed"
    else
        echo "✗ Linting issues found"
        ERRORS=$((ERRORS + 1))
    fi
else
    echo "⚠ ruff not found, skipping linting"
fi

# Check 3: Validate JSON files in memory
echo ""
echo "[3/4] Validating memory files..."
MEMORY_DIR=".claude/memory"

validate_json() {
    local file=$1
    if [ -f "$file" ]; then
        if python -c "import json; [json.loads(line) for line in open('$file')]" 2>/dev/null; then
            echo "  ✓ $file is valid"
        else
            echo "  ✗ $file has invalid JSON"
            return 1
        fi
    fi
}

validate_single_json() {
    local file=$1
    if [ -f "$file" ]; then
        if python -c "import json; json.load(open('$file'))" 2>/dev/null; then
            echo "  ✓ $file is valid"
        else
            echo "  ✗ $file has invalid JSON"
            return 1
        fi
    fi
}

if [ -f "${MEMORY_DIR}/progress_log.jsonl" ]; then
    validate_json "${MEMORY_DIR}/progress_log.jsonl" || ERRORS=$((ERRORS + 1))
fi
if [ -f "${MEMORY_DIR}/decisions.jsonl" ]; then
    validate_json "${MEMORY_DIR}/decisions.jsonl" || ERRORS=$((ERRORS + 1))
fi
if [ -f "${MEMORY_DIR}/learner_profile.json" ]; then
    validate_single_json "${MEMORY_DIR}/learner_profile.json" || ERRORS=$((ERRORS + 1))
fi

# Check 4: Check for common issues
echo ""
echo "[4/4] Checking for common issues..."

# Check for hardcoded secrets
if grep -r "sk-" --include="*.py" --include="*.md" . 2>/dev/null | grep -v ".git" | head -5; then
    echo "  ✗ Possible API keys found"
    ERRORS=$((ERRORS + 1))
else
    echo "  ✓ No obvious secrets found"
fi

# Check for TODO/FIXME
TODO_COUNT=$(grep -r "TODO\|FIXME" --include="*.py" --include="*.md" . 2>/dev/null | grep -v ".git" | wc -l || echo "0")
if [ "$TODO_COUNT" -gt 0 ]; then
    echo "  ⚠ Found $TODO_COUNT TODO/FIXME comments"
else
    echo "  ✓ No TODO/FIXME comments"
fi

# Summary
echo ""
echo "=========================================="
if [ $ERRORS -eq 0 ]; then
    echo "  ✓ All checks passed!"
    echo "  Ready to publish."
else
    echo "  ✗ $ERRORS check(s) failed"
    echo "  Please fix issues before publishing."
fi
echo "=========================================="

exit $ERRORS
