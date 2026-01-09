# MCP Safety Guidelines

This document defines security, privacy, and integrity requirements for MCP tools.

## Core Principles

1. **Minimal Privilege**: Tools have only the permissions they need
2. **User Approval**: No state changes without explicit user consent
3. **Transparency**: All tool actions are logged and visible
4. **Defense in Depth**: Multiple layers of protection

## Secret Management

### Never in Code
- No API keys in source files
- No passwords in configuration
- No tokens in examples

### Environment Variables
```python
# ✅ Correct
import os
api_key = os.environ.get("OPENAI_API_KEY")

# ❌ Wrong
api_key = "sk-abc123..."
```

### .env Files
- Never commit `.env` to git
- Add to `.gitignore`
- Provide `.env.example` with placeholders

```bash
# .env.example (safe to commit)
OPENAI_API_KEY=your-api-key-here
DATABASE_URL=postgresql://user:pass@host:5432/db
```

## Input Validation

### Path Traversal Prevention

```python
import os

ALLOWED_PREFIXES = [
    "docs/",
    "paths/",
    "stacks/",
    ".claude/memory/",
]

def validate_path(path: str) -> bool:
    # Normalize path
    normalized = os.path.normpath(path)

    # Check for path traversal
    if ".." in normalized:
        return False

    # Check against allowlist
    for prefix in ALLOWED_PREFIXES:
        if normalized.startswith(prefix):
            return True

    return False
```

### Size Limits

```python
MAX_FILE_SIZE = 1024 * 1024  # 1MB
MAX_ENTRY_SIZE = 10 * 1024   # 10KB

def validate_file_size(path: str) -> bool:
    return os.path.getsize(path) <= MAX_FILE_SIZE

def validate_entry_size(entry: dict) -> bool:
    return len(json.dumps(entry)) <= MAX_ENTRY_SIZE
```

### Schema Validation

```python
import jsonschema

def validate_input(schema: dict, data: dict) -> tuple[bool, str]:
    try:
        jsonschema.validate(data, schema)
        return True, ""
    except jsonschema.ValidationError as e:
        return False, str(e.message)
```

## Scope Limitations

### Read Scope

Tools can only read:
- Documentation: `docs/**`
- Learning path: `paths/**`
- Stack definitions: `stacks/**`
- Memory files: `.claude/memory/**`
- Root docs: `README.md`, `CLAUDE.md`

Tools cannot read:
- Source code in templates (to prevent leaking solutions)
- Git directory: `.git/**`
- Environment files: `.env*`
- Secrets: `**/secrets/**`

### Write Scope

Tools can only write:
- `progress_log.jsonl` (append-only)
- `decisions.jsonl` (append-only)

Tools cannot write:
- Any other file
- Cannot delete files
- Cannot modify existing content

## Evaluation Integrity

### Preventing Score Manipulation

1. **Separate evaluation from adaptation**
   - `evaluate.py` computes scores
   - `adapt.py` proposes changes
   - User approves before any modification

2. **Immutable history**
   - Progress log is append-only
   - Decisions are timestamped
   - No retroactive changes

3. **Transparent scoring**
   - Rubric is documented
   - Signals are visible
   - User can audit any evaluation

### Anti-Gaming Measures

```python
# Prevent bulk additions
def validate_entry_frequency(progress_log: list, new_entry: dict) -> bool:
    recent = [e for e in progress_log if is_within_hours(e, 1)]
    if len(recent) > 20:
        raise RateLimitError("Too many entries in the last hour")
    return True
```

## Audit Logging

All tool calls should be logged:

```python
def log_tool_call(tool_name: str, input_data: dict, result: dict, user: str):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "tool": tool_name,
        "input": sanitize_input(input_data),  # Remove any sensitive data
        "success": "error" not in result,
        "user": user
    }
    # Append to audit log
```

## Error Handling

### Safe Error Messages

```python
# ✅ Safe - doesn't reveal system internals
def handle_error(e: Exception) -> dict:
    return {"error": "Operation failed. Please check your input."}

# ❌ Unsafe - reveals file path and stack trace
def handle_error(e: Exception) -> dict:
    return {"error": str(e), "traceback": traceback.format_exc()}
```

### Fail Secure

When in doubt, deny:

```python
def check_permission(path: str, operation: str) -> bool:
    try:
        return validate_path(path) and validate_operation(operation)
    except Exception:
        # On any error, deny access
        return False
```

## Checklist for New Tools

Before adding a new MCP tool:

- [ ] Define input/output schemas
- [ ] Implement input validation
- [ ] Add to allowlist if needed
- [ ] Set appropriate size limits
- [ ] Handle all error cases safely
- [ ] Add audit logging
- [ ] Document in tool-contracts.md
- [ ] Add usage examples
- [ ] Test with malicious inputs
- [ ] Review with security mindset
