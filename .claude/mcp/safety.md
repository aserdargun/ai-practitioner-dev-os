# MCP Safety Guidelines

Security, privacy, and integrity guidelines for MCP tool usage.

## Core Principles

### 1. Least Privilege
Tools have only the permissions necessary for their function.

- `hello`: No file access, no side effects
- `read_repo_file`: Read-only, path-restricted
- `write_memory_entry`: Append-only, file-restricted

### 2. Explicit Consent
User must approve all state-changing operations.

```
BEFORE writing to any memory file:
1. Show the proposed content to the user
2. Explain what will be written and where
3. Wait for explicit "yes" approval
4. Only then execute the write
```

### 3. Audit Trail
All operations are logged for review.

```json
{
  "timestamp": "2026-01-15T10:00:00Z",
  "tool": "write_memory_entry",
  "parameters": {"file": "progress_log.jsonl"},
  "result": "success",
  "user_approved": true
}
```

### 4. Safe Defaults
When in doubt, fail closed.

- Unknown paths → Reject
- Invalid JSON → Reject
- Missing approval → Do not execute

---

## File Access Rules

### Allowed Reads
- `.claude/memory/*.jsonl`
- `.claude/memory/*.md`
- `.claude/memory/*.json`
- `paths/*/tracker.md`
- `docs/**/*.md`

### Blocked Reads
- `.env`, `.env.*` — Environment secrets
- `**/secret*`, `**/credential*` — Sensitive files
- `.git/**` — Git internals
- `**/*.key`, `**/*.pem` — Private keys
- Files outside repository root

### Allowed Writes
- `.claude/memory/progress_log.jsonl` (append)
- `.claude/memory/decisions.jsonl` (append)
- `.claude/memory/best_practices.md` (append)

### Blocked Writes
- All other files
- Any overwrite operation
- Any delete operation

---

## Secret Handling

### Never Store
- API keys
- Passwords
- Tokens
- Private keys
- Personal identifiable information (PII)

### If Secrets Are Detected
1. Do not log the content
2. Warn the user
3. Reject the operation

```python
SENSITIVE_PATTERNS = [
    r'(?i)api[_-]?key',
    r'(?i)secret',
    r'(?i)password',
    r'(?i)token',
    r'sk-[a-zA-Z0-9]+',  # OpenAI key pattern
    r'ghp_[a-zA-Z0-9]+',  # GitHub token pattern
]
```

---

## Privacy Considerations

### What to Log
- Event types (start, end, milestone)
- Progress indicators
- Technical decisions
- Learning reflections

### What NOT to Log
- Personal details beyond learning context
- Location data
- Employer/client information
- Financial information

### Data Retention
Memory files are append-only. The learner owns all data and can:
- Review all entries
- Edit or remove entries
- Export their data
- Delete the repository

---

## Evaluation Integrity

### Preventing Gaming
- Evaluations are based on multiple signals
- No single metric determines outcomes
- Manual review is always available

### Honest Assessment
- Scores reflect actual evidence
- Failures are documented fairly
- Progress is not inflated

### Adaptation Boundaries
`adapt.py` can only propose:
- Level changes (within rules)
- Month reordering
- Remediation weeks
- Project swaps

It cannot:
- Skip required content
- Auto-approve changes
- Modify evaluation criteria
- Access external systems

---

## Implementation Checklist

### Server Security
- [ ] Input validation on all parameters
- [ ] Path traversal prevention
- [ ] Size limits enforced
- [ ] Rate limiting (if needed)
- [ ] Error messages don't leak internals

### Client Security
- [ ] Validate responses
- [ ] Handle errors gracefully
- [ ] Don't expose server details
- [ ] Timeout handling

### Operational Security
- [ ] Regular audit log review
- [ ] Keep dependencies updated
- [ ] Monitor for anomalies
- [ ] Document all changes

---

## Incident Response

### If Security Issue Found

1. **Stop** — Halt the operation
2. **Document** — Record what happened
3. **Assess** — Determine impact
4. **Fix** — Address the vulnerability
5. **Review** — Prevent recurrence

### Reporting
If you discover a security issue:
- Don't exploit it
- Document responsibly
- Report through appropriate channels

---

## See Also

- [tool-contracts.md](tool-contracts.md) — Tool specifications
- [examples.md](examples.md) — Usage patterns
- [../memory/README.md](../memory/README.md) — Memory system overview
