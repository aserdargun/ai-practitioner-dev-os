#!/bin/bash
# pre_publish_check.sh
# Run this before publishing a project publicly

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo "=========================================="
echo "  Pre-Publish Check Hook"
echo "=========================================="
echo ""

# Track failures
FAILURES=0

# Function to report status
check_status() {
    if [ $1 -eq 0 ]; then
        echo -e "  ${GREEN}✓${NC} $2"
    else
        echo -e "  ${RED}✗${NC} $2"
        FAILURES=$((FAILURES + 1))
    fi
}

# Get project path
PROJECT_PATH=${1:-.}
echo "Checking project: $PROJECT_PATH"
echo ""

# 1. Check for tests
echo -e "${YELLOW}Running Tests...${NC}"
if [ -f "$PROJECT_PATH/pyproject.toml" ] || [ -d "$PROJECT_PATH/tests" ]; then
    if command -v pytest &> /dev/null; then
        pytest "$PROJECT_PATH" -v --tb=short 2>/dev/null
        check_status $? "Tests pass"
    else
        echo "  pytest not installed, skipping tests"
        check_status 1 "Tests (pytest not found)"
    fi
else
    echo "  No tests directory found"
    check_status 1 "Tests exist"
fi
echo ""

# 2. Run linter
echo -e "${YELLOW}Running Linter...${NC}"
if command -v ruff &> /dev/null; then
    ruff check "$PROJECT_PATH" 2>/dev/null
    check_status $? "Linter passes"
else
    echo "  ruff not installed, skipping linter"
    check_status 1 "Linter (ruff not found)"
fi
echo ""

# 3. Check for secrets
echo -e "${YELLOW}Checking for Secrets...${NC}"
SECRETS_PATTERNS=(
    "password.*=.*['\"]"
    "api_key.*=.*['\"]"
    "secret.*=.*['\"]"
    "token.*=.*['\"]"
    "AWS_ACCESS_KEY"
    "AWS_SECRET"
    "OPENAI_API_KEY"
)

SECRETS_FOUND=0
for pattern in "${SECRETS_PATTERNS[@]}"; do
    if grep -rni "$pattern" "$PROJECT_PATH" --include="*.py" --include="*.json" --include="*.yaml" --include="*.yml" 2>/dev/null | grep -v ".env.example" | grep -v "test" | head -5; then
        SECRETS_FOUND=1
    fi
done

if [ $SECRETS_FOUND -eq 0 ]; then
    check_status 0 "No hardcoded secrets found"
else
    check_status 1 "Possible secrets detected (review above)"
fi
echo ""

# 4. Check .gitignore
echo -e "${YELLOW}Checking .gitignore...${NC}"
REQUIRED_IGNORES=(".env" "__pycache__" "*.pyc" ".DS_Store")
MISSING_IGNORES=0

if [ -f "$PROJECT_PATH/.gitignore" ]; then
    for ignore in "${REQUIRED_IGNORES[@]}"; do
        if ! grep -q "$ignore" "$PROJECT_PATH/.gitignore"; then
            echo "  Missing: $ignore"
            MISSING_IGNORES=1
        fi
    done
    check_status $MISSING_IGNORES ".gitignore complete"
else
    check_status 1 ".gitignore exists"
fi
echo ""

# 5. Check README exists and has content
echo -e "${YELLOW}Checking README...${NC}"
if [ -f "$PROJECT_PATH/README.md" ]; then
    LINES=$(wc -l < "$PROJECT_PATH/README.md")
    if [ "$LINES" -gt 10 ]; then
        check_status 0 "README.md exists and has content ($LINES lines)"
    else
        check_status 1 "README.md is too short ($LINES lines)"
    fi
else
    check_status 1 "README.md exists"
fi
echo ""

# 6. Check for broken links in markdown (basic check)
echo -e "${YELLOW}Checking Documentation Links...${NC}"
BROKEN_LINKS=0
for md_file in $(find "$PROJECT_PATH" -name "*.md" -type f 2>/dev/null | head -20); do
    # Check for relative links that don't exist
    while IFS= read -r link; do
        if [ -n "$link" ]; then
            # Extract path from markdown link
            path=$(echo "$link" | sed 's/.*](\(.*\))/\1/' | sed 's/#.*//' | sed 's/?.*//')
            if [[ "$path" != http* ]] && [[ "$path" != "" ]]; then
                full_path="$(dirname "$md_file")/$path"
                if [ ! -e "$full_path" ] && [ ! -e "$PROJECT_PATH/$path" ]; then
                    echo "  Broken link in $md_file: $path"
                    BROKEN_LINKS=1
                fi
            fi
        fi
    done < <(grep -o '\[.*\]([^)]*' "$md_file" 2>/dev/null || true)
done
check_status $BROKEN_LINKS "Documentation links valid"
echo ""

# 7. Check Python dependencies are pinned
echo -e "${YELLOW}Checking Dependencies...${NC}"
if [ -f "$PROJECT_PATH/requirements.txt" ]; then
    UNPINNED=$(grep -c "^[^#].*[^=]==" "$PROJECT_PATH/requirements.txt" 2>/dev/null || echo "0")
    if [ "$UNPINNED" -eq 0 ]; then
        check_status 0 "Dependencies pinned in requirements.txt"
    else
        check_status 1 "Some dependencies not pinned"
    fi
elif [ -f "$PROJECT_PATH/pyproject.toml" ]; then
    check_status 0 "Using pyproject.toml for dependencies"
else
    check_status 1 "No requirements.txt or pyproject.toml"
fi
echo ""

# Summary
echo "=========================================="
if [ $FAILURES -eq 0 ]; then
    echo -e "${GREEN}All checks passed! Ready to publish.${NC}"
else
    echo -e "${RED}$FAILURES check(s) failed. Please review before publishing.${NC}"
fi
echo "=========================================="
echo ""

# Exit with failure count
exit $FAILURES

# Manual Fallback Instructions
: << 'MANUAL_FALLBACK'
If you cannot run this script, do the following manually:

1. Run tests:
   pytest tests/ -v

2. Run linter:
   ruff check .

3. Search for secrets:
   grep -rni "password\|api_key\|secret\|token" --include="*.py"

4. Check .gitignore includes:
   - .env
   - __pycache__
   - *.pyc

5. Verify README.md:
   - Has project description
   - Has setup instructions
   - Has usage examples

6. Test all documentation links manually
MANUAL_FALLBACK
