# Command: /harden

## Purpose

Review and improve code quality, security, and performance. This command triggers a thorough review with actionable feedback.

## Inputs

- Files to review (optional, defaults to current project)
- Specific concerns (optional)
- Context from best practices

## Outputs

- Structured feedback with severity levels
- Suggested fixes for each issue
- Security audit results
- Performance observations
- **All fixes require user approval**

## When to Use

- After `/ship-mvp` before publishing
- When you have quality concerns
- Before submitting for code review
- After implementing complex logic

## Agent Routing

**Primary**: Reviewer Agent

The Reviewer performs a multi-dimensional review covering code quality, security, performance, and best practices.

## Example Usage

**User Input**:
```
/harden
```

**Expected Output**:
```
## Code Hardening Review: RAG System

### Summary
Reviewed 8 files, found 12 issues (1 critical, 3 important, 8 suggestions)

---

### 🔴 Critical (1)

**rag/store.py:45** - SQL Injection Risk
```python
# Current (vulnerable)
query = f"SELECT * FROM docs WHERE id = {doc_id}"

# Fixed
query = "SELECT * FROM docs WHERE id = ?"
cursor.execute(query, (doc_id,))
```
**Approve fix?** (yes/no)

---

### 🟠 Important (3)

**rag/retrieve.py:23** - No error handling for empty results
```python
# Current
return results[0]

# Fixed
if not results:
    raise ValueError("No results found")
return results[0]
```

**rag/config.py:12** - Hardcoded timeout
- Risk: May cause issues in slow networks
- Fix: Make configurable via environment variable

**tests/test_store.py** - Missing negative test cases
- Risk: Edge cases not covered
- Fix: Add tests for empty input, invalid IDs

---

### 🟡 Suggestions (8)

1. Add type hints to `retrieve()` function
2. Consider using `logging` instead of `print()`
3. Extract magic number `1536` to constant
4. Add docstring to `ChunkProcessor` class
5. Consider async for `connect()` method
6. Add retry logic for network calls
7. Use `pathlib` instead of string path manipulation
8. Consider adding `__repr__` to dataclasses

---

### 🟢 Praise

- Good separation of concerns in module structure
- Excellent test coverage for happy path
- Clear naming conventions

---

**Actions**:
- Fix critical issue? (strongly recommended)
- Fix important issues? (recommended)
- Apply suggestions? (optional)
```

## Security Checklist

The Reviewer checks for:
- [ ] No secrets in code
- [ ] Input validation
- [ ] SQL/Command injection
- [ ] Path traversal
- [ ] Error message leakage
- [ ] Dependency vulnerabilities

## Related Commands

- `/ship-mvp` - Get to MVP first
- `/publish` - After hardening, prepare to publish
- `/add-best-practice` - Capture patterns learned
