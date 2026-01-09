# Command: /harden

## Purpose
Improve code quality by adding tests, documentation, error handling, and addressing technical debt after MVP functionality is complete.

## Inputs
- **Target**: Code, module, or project to harden
- **Focus areas**: Tests, docs, errors, performance (optional)
- **Coverage goal**: Desired test coverage (optional)

## Outputs
- **Tests**: Unit and integration tests
- **Documentation**: Docstrings, README updates, usage examples
- **Error Handling**: Input validation, graceful failures, logging
- **Code Quality**: Linting fixes, type hints, refactoring

## When to Use
- After MVP is working but before publishing
- When code quality is lower than desired
- Before handing code off or making it public
- When tests are missing or incomplete

## Agent Routing
**Builder** — implements improvements
**Reviewer** — identifies issues and validates fixes

## Example Usage

### Basic Hardening
```
/harden the data_processor module
```

### Focused Hardening
```
/harden
Focus on tests only
Target: 80% coverage for the pipeline module
```

### Full Hardening
```
/harden the entire project
Add tests, improve error handling, add docstrings
Make it production-ready
```

## Sample Output

```
🔧 HARDENING REPORT — Data Pipeline

Before:
- Test coverage: 23%
- Documented functions: 4/12
- Error handling: Basic
- Lint warnings: 17

Actions Taken:

Tests Added:
✓ test_validate_input.py (8 tests)
✓ test_transform_data.py (6 tests)
✓ test_edge_cases.py (5 tests)
Coverage: 23% → 78%

Documentation:
✓ Added docstrings to all public functions
✓ Updated README with examples
✓ Added inline comments for complex logic

Error Handling:
✓ Input validation with clear messages
✓ Try/except for file operations
✓ Logging for debugging

Code Quality:
✓ Fixed all lint warnings
✓ Added type hints
✓ Extracted magic numbers to constants

After:
- Test coverage: 78%
- Documented functions: 12/12
- Error handling: Comprehensive
- Lint warnings: 0

Remaining Tech Debt:
- Consider adding integration tests
- Performance optimization for large files
- Add retry logic for network calls

Run tests: pytest tests/ -v
Run linter: ruff check .
```

## Hardening Checklist

### Tests
- [ ] Unit tests for core functions
- [ ] Edge case tests
- [ ] Error condition tests
- [ ] Integration tests (if applicable)

### Documentation
- [ ] All public functions have docstrings
- [ ] README is up to date
- [ ] Usage examples included
- [ ] Known limitations documented

### Error Handling
- [ ] Input validation
- [ ] Graceful failure modes
- [ ] Clear error messages
- [ ] Logging for debugging

### Code Quality
- [ ] Linter passes
- [ ] No hardcoded values
- [ ] Consistent style
- [ ] Type hints (optional but recommended)

## Related Commands
- `/ship-mvp` — Get functionality working first
- `/publish` — Prepare for portfolio after hardening
- `/evaluate` — Check quality scores
