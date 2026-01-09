# Command: /harden

## Purpose

Focus on code quality, comprehensive testing, documentation, and edge case handling to prepare the project for production-readiness.

## Inputs

Optional context:
- Areas of concern
- Known edge cases to handle
- Performance requirements

The command reads from:
- Your codebase
- Test coverage reports
- `.claude/skills/` playbooks
- `.claude/memory/best_practices.md`

## Outputs

- Quality assessment of current code
- Test coverage gaps
- Documentation checklist
- Edge cases to handle
- Refactoring suggestions

## When to Use

- Week 3 of monthly cycle
- After MVP is complete
- Before publishing/demo

## Agent Routing

**Primary**: Builder Agent
**Secondary**: Reviewer Agent

Builder proposes improvements, Reviewer validates quality.

## Example Usage

```
/harden
```

Or with focus areas:

```
/harden

Focus on error handling and the data validation layer.
I'm worried about malformed input.
```

## Output Format

```markdown
## Hardening Report — [Project Name]

### Current Quality Assessment

| Aspect | Status | Notes |
|--------|--------|-------|
| Test Coverage | 65% | Missing edge cases |
| Documentation | Partial | API docs incomplete |
| Error Handling | Basic | Needs improvement |
| Type Hints | Good | 90% coverage |

### Test Gaps

#### Missing Tests
1. `test_invalid_input.py` — edge case handling
2. `test_error_recovery.py` — failure modes

#### Suggested Test Cases
```python
def test_handles_empty_input():
    """Should gracefully handle empty input."""
    result = process("")
    assert result.status == "empty"
```

### Documentation Needs
- [ ] API endpoint documentation
- [ ] Error code reference
- [ ] Configuration options
- [ ] Deployment notes

### Edge Cases to Handle
1. Empty input
2. Malformed data
3. Network timeouts
4. Rate limiting

### Refactoring Suggestions
- Extract [function] into separate module
- Add retry logic to [component]
- Improve error messages in [area]

### Quality Checklist
- [ ] All tests passing
- [ ] ruff lint clean
- [ ] No TODO/FIXME in code
- [ ] README complete
- [ ] Error handling comprehensive

---
**Approve hardening plan?** (yes/no/modify)
```

## Quality Standards

For Intermediate level:
- Test coverage: aim for 70%+
- All public functions documented
- Error handling for expected failures
- Type hints on public interfaces
- Clean ruff output
