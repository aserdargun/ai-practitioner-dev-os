# MCP Safety Guidelines

Security, privacy, and safety rules for MCP tools in the learning OS.

## Core Principles

### 1. Least Privilege
Tools should only access what they need to function. No broad permissions.

### 2. Human Oversight
Critical operations require user approval. The system proposes, the user decides.

### 3. Transparency
All tool operations should be visible and auditable.

### 4. Defense in Depth
Multiple layers of protection: input validation, path restrictions, output sanitization.

---

## File Access Rules

### Allowed Read Paths
```
docs/**              # Documentation
paths/**             # Learning paths
stacks/**            # Stack definitions
.claude/memory/*     # Memory files
.claude/commands/*   # Command definitions
.claude/skills/*     # Skill playbooks
README.md            # Root readme
CLAUDE.md            # Claude instructions
```

### Denied Read Paths
```
.env                 # Environment variables
.env.*               # Environment variants
**/secrets/**        # Secret directories
**/*.key             # Key files
**/*.pem             # Certificate files
**/*.p12             # Certificate stores
**/credentials*      # Credential files
**/config/prod*      # Production configs
.git/**              # Git internals
node_modules/**      # Dependencies (too large)
```

### Write Paths
Only append to:
```
.claude/memory/progress_log.jsonl
.claude/memory/decisions.jsonl
.claude/memory/best_practices.md
```

---

## Input Validation

### Path Validation
```python
def validate_path(path: str) -> bool:
    # No path traversal
    if ".." in path:
        return False

    # No absolute paths
    if path.startswith("/"):
        return False

    # Only allowed characters
    if not re.match(r'^[a-zA-Z0-9_\-./]+$', path):
        return False

    # Check against allow/deny lists
    return is_allowed(path) and not is_denied(path)
```

### Entry Validation
```python
def validate_entry(entry: dict) -> bool:
    # Must have timestamp
    if "timestamp" not in entry:
        return False

    # Timestamp must be valid ISO format
    try:
        datetime.fromisoformat(entry["timestamp"])
    except:
        return False

    # Size limit
    if len(json.dumps(entry)) > 5000:
        return False

    return True
```

---

## Secrets Protection

### Never Log
- API keys
- Passwords
- Tokens
- Personal identifiable information (PII)
- Financial data

### Environment Variable Handling
```python
# Never read environment variables through tools
# If configuration is needed, use safe config files

# BAD - Don't do this
os.environ.get("API_KEY")

# GOOD - Use config that's explicitly allowed
config = read_safe_config("config/public.json")
```

### Detection Patterns
The system should reject content containing:
```
password\s*[=:]\s*['"]
api_key\s*[=:]\s*['"]
secret\s*[=:]\s*['"]
token\s*[=:]\s*['"]
bearer\s+[a-zA-Z0-9\-._~+/]+=*
```

---

## Evaluation Integrity

### Preventing Gaming
- Evaluation scores should come from actual evidence
- Progress log entries should be validated against real activity
- Time-based checks prevent batch-fabricating entries

### Audit Trail
```json
{
  "timestamp": "2026-03-15T10:00:00Z",
  "event": "task_completed",
  "evidence": {
    "commit_sha": "abc123",
    "files_changed": ["src/pipeline.py"],
    "tests_passed": true
  }
}
```

### Rate Limiting
- Max 100 progress entries per day
- Max 10 decision entries per day
- Alerts on unusual patterns

---

## Privacy Guidelines

### Data Minimization
Only collect what's necessary for learning tracking:
- Progress events (not detailed code)
- Decisions (not personal notes)
- Best practices (learner chooses what to share)

### Local Storage
All memory stays in the local repository:
- Not sent to external services
- Learner controls their data
- Can delete anything at any time

### Sharing Decisions
Before any data could be shared:
- Explicit user consent required
- Clear explanation of what will be shared
- Easy opt-out

---

## Error Handling

### Safe Error Messages
```python
# BAD - Reveals system information
raise Exception(f"Cannot read {full_system_path}")

# GOOD - Safe error message
raise Exception("File not accessible")
```

### Graceful Degradation
If a tool fails:
1. Return structured error
2. Don't expose internal state
3. Allow workflow to continue
4. Log for debugging (sanitized)

---

## Security Checklist

Before adding new tools:
- [ ] Does it follow least privilege?
- [ ] Is input validated?
- [ ] Are paths restricted?
- [ ] Are secrets protected?
- [ ] Is output sanitized?
- [ ] Is there an audit trail?
- [ ] Does it require user approval for writes?

---

## Incident Response

If a security issue is discovered:
1. Disable affected tool immediately
2. Review audit logs
3. Notify user of potential impact
4. Fix and test before re-enabling
5. Document in decisions.jsonl

---

## Updates to Safety Rules

Changes to safety rules require:
1. Clear documentation of the change
2. Rationale for why it's needed
3. Review of potential risks
4. Testing before deployment
5. User notification of changes
