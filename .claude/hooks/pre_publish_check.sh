#!/bin/bash
set -e

# pre_publish_check.sh - Quality gate before publishing work externally
# When to use: Before publishing, demoing, or submitting work

echo "=== Pre-Publish Check ==="
echo ""

REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
cd "$REPO_ROOT"

FAILED=0
WARNINGS=0

# 1. Run tests
echo "1. Running tests..."
if command -v pytest &> /dev/null; then
    if pytest --tb=short -q 2>/dev/null; then
        echo "   ✅ Tests passed"
    else
        echo "   ❌ Tests failed"
        FAILED=$((FAILED + 1))
    fi
else
    echo "   ⚠️  pytest not installed, skipping tests"
    WARNINGS=$((WARNINGS + 1))
fi
echo ""

# 2. Run linter
echo "2. Running linter..."
if command -v ruff &> /dev/null; then
    LINT_OUTPUT=$(ruff check . 2>&1 || true)
    LINT_ERRORS=$(echo "$LINT_OUTPUT" | grep -c "error" || echo "0")
    LINT_WARNINGS=$(echo "$LINT_OUTPUT" | grep -c "warning" || echo "0")

    if [ "$LINT_ERRORS" -eq 0 ]; then
        if [ "$LINT_WARNINGS" -gt 0 ]; then
            echo "   ⚠️  $LINT_WARNINGS warnings (run 'ruff check --fix' to auto-fix)"
            WARNINGS=$((WARNINGS + 1))
        else
            echo "   ✅ Linting passed"
        fi
    else
        echo "   ❌ $LINT_ERRORS errors found"
        echo "$LINT_OUTPUT" | head -20
        FAILED=$((FAILED + 1))
    fi
else
    echo "   ⚠️  ruff not installed, skipping linting"
    WARNINGS=$((WARNINGS + 1))
fi
echo ""

# 3. Check for secrets (basic patterns)
echo "3. Checking for secrets..."
SECRET_PATTERNS="password=|api_key=|secret=|token=|AWS_|OPENAI_API_KEY"
SECRETS_FOUND=$(grep -r -E "$SECRET_PATTERNS" --include="*.py" --include="*.json" --include="*.yaml" --include="*.yml" . 2>/dev/null | grep -v ".env.example" | grep -v "test" | head -5 || true)

if [ -z "$SECRETS_FOUND" ]; then
    echo "   ✅ No obvious secrets found"
else
    echo "   ❌ Possible secrets detected:"
    echo "$SECRETS_FOUND"
    FAILED=$((FAILED + 1))
fi
echo ""

# 4. Check documentation links
echo "4. Checking documentation..."
if command -v python3 &> /dev/null; then
    BROKEN_LINKS=0
    for md_file in $(find docs -name "*.md" 2>/dev/null); do
        # Check for relative links that might be broken
        LINKS=$(grep -oE '\[.*\]\([^)]+\)' "$md_file" 2>/dev/null | grep -v "http" || true)
        for link in $LINKS; do
            # Extract path from markdown link
            path=$(echo "$link" | sed 's/.*(\([^)]*\)).*/\1/' | cut -d'#' -f1)
            if [ -n "$path" ] && [ ! -f "$REPO_ROOT/docs/$path" ] && [ ! -f "$REPO_ROOT/$path" ]; then
                echo "   ⚠️  Broken link in $md_file: $path"
                BROKEN_LINKS=$((BROKEN_LINKS + 1))
            fi
        done
    done

    if [ "$BROKEN_LINKS" -eq 0 ]; then
        echo "   ✅ Documentation links look OK"
    else
        echo "   ⚠️  $BROKEN_LINKS potentially broken links"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo "   ⚠️  Skipping link check"
fi
echo ""

# 5. Check for uncommitted changes
echo "5. Checking git status..."
UNCOMMITTED=$(git status --porcelain 2>/dev/null | wc -l || echo "0")
if [ "$UNCOMMITTED" -eq 0 ]; then
    echo "   ✅ Working directory clean"
else
    echo "   ⚠️  $UNCOMMITTED uncommitted changes"
    WARNINGS=$((WARNINGS + 1))
fi
echo ""

# 6. Summary
echo "=== Summary ==="
echo ""
if [ "$FAILED" -eq 0 ] && [ "$WARNINGS" -eq 0 ]; then
    echo "✅ All checks passed! Ready to publish."
    exit 0
elif [ "$FAILED" -eq 0 ]; then
    echo "⚠️  $WARNINGS warnings, but no blocking issues."
    echo "   Consider fixing warnings before publishing."
    exit 0
else
    echo "❌ $FAILED checks failed, $WARNINGS warnings."
    echo "   Fix the failures before publishing."
    exit 1
fi
