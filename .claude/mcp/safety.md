# MCP Safety Guidelines

This document outlines the security, privacy, and evaluation integrity guidelines for the MCP tools in the AI Practitioner Learning OS.

---

## Principles

1. **Least Privilege**: Tools only have access to what they need
2. **Append-Only Memory**: Cannot delete or modify history
3. **No Secrets in Code**: Never store credentials in memory files
4. **Transparent Operations**: All operations are logged

---

## Secret Management

### Never Store in Memory

Do NOT put these in any memory file:

- API keys (OpenAI, AWS, etc.)
- Passwords
- Personal identifiable information (PII)
- Authentication tokens
- Private keys

### Safe Storage

Store secrets in:
- Environment variables
- `.env` files (not tracked in git)
- Secret management services (AWS Secrets Manager, etc.)

### Example: Using Environment Variables

```python
# WRONG - never do this
config = {
    "api_key": "sk-1234567890abcdef"  # NO!
}

# RIGHT - use environment variables
import os
config = {
    "api_key": os.environ.get("OPENAI_API_KEY")
}
```

---

## Privacy Guidelines

### What's Safe to Log

✅ Events and timestamps
✅ Task names and durations
✅ Scores and metrics
✅ General reflections
✅ Technical decisions

### What's NOT Safe to Log

❌ Personal information
❌ Company proprietary data
❌ Client/customer data
❌ Detailed code from work projects
❌ Anything covered by NDA

### Reflection Guidelines

When logging reflections, keep them general:

```json
// GOOD
{"reflection": "Struggled with complex SQL joins today"}

// BAD - too specific about work
{"reflection": "Struggled with the customer_orders join for Project X at Company Y"}
```

---

## Evaluation Integrity

### Don't Game the System

The evaluation system is designed to help you learn. Don't:

- Artificially inflate progress logs
- Log tasks you didn't actually complete
- Manipulate scores to avoid remediation
- Skip ahead without understanding

### Why Integrity Matters

- The system adapts based on your honest input
- Inaccurate data leads to bad recommendations
- You're only cheating yourself

### How to Stay Honest

1. Log tasks when you actually complete them
2. Be honest in reflections (struggles are valuable data!)
3. Let evaluations reflect reality
4. Accept remediation when needed - it helps

---

## File Access Controls

### Read Permissions

| Path Pattern | Access |
|--------------|--------|
| `paths/**` | ✅ Allowed |
| `docs/**` | ✅ Allowed |
| `.claude/memory/**` | ✅ Allowed |
| `templates/**` | ✅ Allowed |
| `examples/**` | ✅ Allowed |
| `.git/**` | ❌ Blocked |
| `**/.env*` | ❌ Blocked |
| `**/secret*` | ❌ Blocked |
| `**/*.key` | ❌ Blocked |
| `**/*.pem` | ❌ Blocked |

### Write Permissions

| File | Access |
|------|--------|
| `progress_log.jsonl` | ✅ Append only |
| `decisions.jsonl` | ✅ Append only |
| `learner_profile.json` | ❌ Manual edit only |
| `best_practices.md` | ❌ Via command only |
| Any other file | ❌ Not via MCP |

---

## Rate Limiting

Tools are rate-limited to prevent abuse:

| Tool | Limit | Window |
|------|-------|--------|
| `hello` | 100 | 1 minute |
| `read_repo_file` | 60 | 1 minute |
| `write_memory_entry` | 30 | 1 minute |

Exceeding limits returns a `RATE_LIMITED` error.

---

## Audit Trail

All MCP operations are logged:

```json
{
  "timestamp": "2026-01-07T10:00:00Z",
  "tool": "write_memory_entry",
  "input": {"file": "progress_log.jsonl", "entry": {...}},
  "result": "success",
  "caller": "evaluator_agent"
}
```

You can review the audit trail in `.claude/mcp/audit.log` (if enabled).

---

## Reporting Issues

If you find a security issue:

1. Do NOT open a public GitHub issue
2. Email the maintainer directly
3. Include:
   - Description of the issue
   - Steps to reproduce
   - Potential impact

See [SECURITY.md](../../../SECURITY.md) for full details.

---

## Summary Checklist

Before using MCP tools:

- [ ] No secrets in entries or files
- [ ] No PII in logs
- [ ] Honest progress reporting
- [ ] Entries have timestamps
- [ ] File paths are in allowed list
- [ ] Entry sizes are reasonable (< 10KB)
