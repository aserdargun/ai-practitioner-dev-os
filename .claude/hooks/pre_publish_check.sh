#!/bin/bash
# Pre-Publish Check Hook
# Runs before publishing/demoing to ensure quality standards

set -e

echo "=========================================="
echo "  Pre-Publish Quality Check"
echo "=========================================="
echo ""

ERRORS=0
WARNINGS=0

# Function to report status
check_pass() {
    echo "  ✓ $1"
}

check_fail() {
    echo "  ✗ $1"
    ERRORS=$((ERRORS + 1))
}

check_warn() {
    echo "  ! $1"
    WARNINGS=$((WARNINGS + 1))
}

# 1. Git Status Check
echo "1. Git Status"
echo "-------------"
if [ -d ".git" ]; then
    UNCOMMITTED=$(git status --porcelain | wc -l)
    if [ "$UNCOMMITTED" -eq 0 ]; then
        check_pass "All changes committed"
    else
        check_warn "Uncommitted changes: $UNCOMMITTED files"
    fi

    # Check if on main/master
    BRANCH=$(git branch --show-current)
    if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
        check_pass "On main branch"
    else
        check_warn "On branch: $BRANCH (consider merging to main)"
    fi
else
    check_fail "Not a git repository"
fi
echo ""

# 2. Linting Check
echo "2. Code Quality (Linting)"
echo "-------------------------"
if command -v ruff &> /dev/null; then
    if [ -d "templates" ]; then
        if ruff check templates/ --quiet 2>/dev/null; then
            check_pass "No linting errors in templates/"
        else
            check_fail "Linting errors found"
        fi
    fi

    if [ -d "src" ]; then
        if ruff check src/ --quiet 2>/dev/null; then
            check_pass "No linting errors in src/"
        else
            check_fail "Linting errors found in src/"
        fi
    fi
else
    check_warn "ruff not installed, skipping lint check"
fi
echo ""

# 3. Test Check
echo "3. Tests"
echo "--------"
if command -v pytest &> /dev/null; then
    TESTS_FOUND=0
    TESTS_PASSED=1

    for dir in templates/*/; do
        if [ -d "$dir/tests" ] || [ -f "$dir/test_*.py" ]; then
            TESTS_FOUND=1
            if ! pytest "$dir" --quiet --tb=no 2>/dev/null; then
                TESTS_PASSED=0
                check_fail "Tests failing in $dir"
            fi
        fi
    done

    if [ "$TESTS_FOUND" -eq 0 ]; then
        check_warn "No tests found"
    elif [ "$TESTS_PASSED" -eq 1 ]; then
        check_pass "All tests passing"
    fi
else
    check_warn "pytest not installed, skipping test check"
fi
echo ""

# 4. Documentation Check
echo "4. Documentation"
echo "----------------"

# Check README
if [ -f "README.md" ]; then
    README_LINES=$(wc -l < "README.md")
    if [ "$README_LINES" -gt 20 ]; then
        check_pass "README.md exists ($README_LINES lines)"
    else
        check_warn "README.md is short ($README_LINES lines)"
    fi
else
    check_fail "README.md missing"
fi

# Check for docstrings in Python files
if [ -d "src" ] || [ -d "templates" ]; then
    PYTHON_FILES=$(find . -name "*.py" -not -path "./.git/*" | head -5)
    MISSING_DOCS=0
    for pyfile in $PYTHON_FILES; do
        if ! grep -q '"""' "$pyfile" 2>/dev/null; then
            MISSING_DOCS=$((MISSING_DOCS + 1))
        fi
    done
    if [ "$MISSING_DOCS" -eq 0 ]; then
        check_pass "Python files have docstrings"
    else
        check_warn "Some Python files may lack docstrings"
    fi
fi
echo ""

# 5. Security Check
echo "5. Security"
echo "-----------"

# Check for secrets
SECRETS_FOUND=0
if grep -r "password\s*=" --include="*.py" . 2>/dev/null | grep -v "test" | grep -v "#" > /dev/null; then
    check_warn "Possible hardcoded passwords found"
    SECRETS_FOUND=1
fi

if grep -r "api_key\s*=" --include="*.py" . 2>/dev/null | grep -v "test" | grep -v "#" | grep -v "os.getenv" > /dev/null; then
    check_warn "Possible hardcoded API keys found"
    SECRETS_FOUND=1
fi

if [ -f ".env" ]; then
    if grep -q ".env" .gitignore 2>/dev/null; then
        check_pass ".env is in .gitignore"
    else
        check_fail ".env exists but not in .gitignore"
    fi
fi

if [ "$SECRETS_FOUND" -eq 0 ]; then
    check_pass "No obvious secrets in code"
fi
echo ""

# 6. Dependencies Check
echo "6. Dependencies"
echo "---------------"
if [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
    check_pass "Dependencies file exists"

    # Check if requirements are pinned
    if [ -f "requirements.txt" ]; then
        UNPINNED=$(grep -c "^[^#]" requirements.txt | grep -cv "==" || echo "0")
        if [ "$UNPINNED" -gt 0 ]; then
            check_warn "Some dependencies may not be pinned"
        fi
    fi
else
    check_warn "No requirements.txt or pyproject.toml found"
fi
echo ""

# Summary
echo "=========================================="
echo "  Summary"
echo "=========================================="
echo ""
echo "  Errors:   $ERRORS"
echo "  Warnings: $WARNINGS"
echo ""

if [ "$ERRORS" -eq 0 ]; then
    if [ "$WARNINGS" -eq 0 ]; then
        echo "  Status: READY TO PUBLISH"
        echo ""
        echo "  All checks passed! Your code is ready for demo/portfolio."
    else
        echo "  Status: READY WITH WARNINGS"
        echo ""
        echo "  Consider addressing warnings before publishing."
    fi
    exit 0
else
    echo "  Status: NOT READY"
    echo ""
    echo "  Please fix errors before publishing."
    exit 1
fi
