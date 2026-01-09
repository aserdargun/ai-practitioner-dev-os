#!/bin/bash
# pre_publish_check.sh
# Run before publishing to verify quality gates

set -e

# Configuration
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
ERRORS=0
WARNINGS=0

echo "=== Pre-Publish Check ==="
echo "Repository: $REPO_ROOT"
echo ""

# Function to record error
error() {
    echo "❌ ERROR: $1"
    ERRORS=$((ERRORS + 1))
}

# Function to record warning
warning() {
    echo "⚠️  WARNING: $1"
    WARNINGS=$((WARNINGS + 1))
}

# Function to record success
success() {
    echo "✓ $1"
}

# Step 1: Check for Python
echo "=== Environment Checks ==="
if command -v python3 &> /dev/null; then
    success "Python3 found: $(python3 --version)"
else
    error "Python3 not found"
fi

# Step 2: Check for ruff
if command -v ruff &> /dev/null; then
    success "ruff found: $(ruff --version)"
else
    warning "ruff not found - skipping lint checks"
fi

# Step 3: Check for pytest
if command -v pytest &> /dev/null; then
    success "pytest found: $(pytest --version 2>&1 | head -1)"
else
    warning "pytest not found - skipping test checks"
fi

echo ""

# Step 4: Run ruff if available
echo "=== Lint Checks ==="
if command -v ruff &> /dev/null; then
    echo "Running ruff check..."
    if ruff check "$REPO_ROOT" --ignore E501 2>/dev/null; then
        success "ruff check passed"
    else
        error "ruff check failed"
    fi

    echo "Running ruff format check..."
    if ruff format --check "$REPO_ROOT" 2>/dev/null; then
        success "ruff format check passed"
    else
        warning "ruff format check failed (files need formatting)"
    fi
else
    warning "Skipping lint checks (ruff not installed)"
fi

echo ""

# Step 5: Run tests if available
echo "=== Test Checks ==="
if command -v pytest &> /dev/null; then
    echo "Running pytest..."
    if pytest "$REPO_ROOT" -q --tb=no 2>/dev/null; then
        success "All tests passed"
    else
        error "Some tests failed"
    fi
else
    warning "Skipping test checks (pytest not installed)"
fi

echo ""

# Step 6: Check documentation
echo "=== Documentation Checks ==="

# Check README exists
if [ -f "$REPO_ROOT/README.md" ]; then
    success "README.md exists"
else
    error "README.md not found"
fi

# Check for broken internal links (basic check)
echo "Checking for broken links in docs..."
BROKEN_LINKS=0
for md_file in $(find "$REPO_ROOT/docs" -name "*.md" 2>/dev/null); do
    # Extract relative links
    links=$(grep -oE '\[.*\]\([^)]+\)' "$md_file" 2>/dev/null | grep -oE '\([^)]+\)' | tr -d '()' | grep -v '^http' || true)
    for link in $links; do
        # Remove anchors
        link_path=$(echo "$link" | cut -d'#' -f1)
        if [ -n "$link_path" ]; then
            # Resolve relative to file location
            dir=$(dirname "$md_file")
            full_path="$dir/$link_path"
            if [ ! -e "$full_path" ]; then
                warning "Broken link in $md_file: $link"
                BROKEN_LINKS=$((BROKEN_LINKS + 1))
            fi
        fi
    done
done

if [ $BROKEN_LINKS -eq 0 ]; then
    success "No broken links found in docs/"
fi

echo ""

# Step 7: Check git status
echo "=== Git Checks ==="
if git status --short 2>/dev/null; then
    UNCOMMITTED=$(git status --short | wc -l)
    if [ "$UNCOMMITTED" -gt 0 ]; then
        warning "$UNCOMMITTED uncommitted changes"
    else
        success "Working directory clean"
    fi
else
    warning "Not in a git repository"
fi

echo ""

# Step 8: Summary
echo "=== Summary ==="
echo "Errors: $ERRORS"
echo "Warnings: $WARNINGS"
echo ""

if [ $ERRORS -gt 0 ]; then
    echo "❌ Pre-publish check FAILED"
    echo "Please fix the errors above before publishing."
    exit 1
else
    if [ $WARNINGS -gt 0 ]; then
        echo "⚠️  Pre-publish check PASSED with warnings"
        echo "Consider addressing warnings before publishing."
    else
        echo "✓ Pre-publish check PASSED"
    fi
    echo ""
    echo "Ready to publish! Next steps:"
    echo "1. Run /publish for demo and write-up guidance"
    echo "2. Commit final changes"
    echo "3. Push to remote"
    exit 0
fi
