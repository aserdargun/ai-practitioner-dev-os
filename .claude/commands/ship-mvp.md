# Command: /ship-mvp

## Purpose

Finalize and ship the minimum viable deliverable for the current month. This command triggers a final review, ensures all DoD items are met, and prepares the deliverable for demonstration.

## Inputs

- Current implementation state
- Month's Definition of Done checklist
- Context from progress log

## Outputs

- DoD checklist status
- Final review feedback
- Completed MVP (tests passing, docs updated)
- Demo preparation notes
- **All finalizations require user approval**

## When to Use

- Core functionality is implemented
- Basic tests are passing
- Ready to move from "building" to "polishing"
- End of month approaching

## Agent Routing

**Primary**: Builder Agent (finalization)
**Secondary**: Reviewer Agent (quality check)

## Example Usage

**User Input**:
```
/ship-mvp
```

**Expected Output**:
```
## Ship MVP: Month 03 RAG System

### Definition of Done Check

| Item | Status | Notes |
|------|--------|-------|
| Retrieval pipeline works | ✅ | Returns top-5 relevant chunks |
| Unit tests (min 5) | ✅ | 7 tests passing |
| Integration test | ⚠️ | Missing end-to-end test |
| Documentation | ⚠️ | README exists, API docs incomplete |
| Demo script | ❌ | Not created yet |

### Status: Almost Ready (3/5 required items complete)

### Remaining Work

1. **Integration Test** (30 min)
   - Add end-to-end test that ingests doc → retrieves → verifies

2. **API Documentation** (20 min)
   - Document `retrieve()` parameters and return values

3. **Demo Script** (15 min)
   - Create `demo.py` that shows the system working

### Proposed Actions

I'll create:
1. `tests/test_integration.py` - E2E test
2. Update `rag/README.md` - API docs
3. `demo.py` - Demo script

**Approve these additions?** (yes / modify / no)

---

After approval, run `/harden` for final quality review.
```

## MVP Philosophy

An MVP is:
- ✅ Core functionality working
- ✅ Basic tests passing
- ✅ Minimal documentation
- ✅ Demonstrable

An MVP is NOT:
- ❌ Perfect or polished
- ❌ All edge cases handled
- ❌ Production-hardened
- ❌ Optimized for performance

## Related Commands

- `/harden` - Quality review after MVP
- `/publish` - External publishing prep
- `/evaluate` - Formal progress evaluation
