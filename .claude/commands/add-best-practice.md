# Command: /add-best-practice

## Purpose

Add a learned best practice to the memory system. This captures valuable patterns and lessons for future reference.

## Inputs

- Best practice description (what you learned)
- Context (optional): when to apply, source

## Outputs

- Proposed addition to `.claude/memory/best_practices.md`
- **Requires user approval before writing**

## When to Use

- After solving a tricky problem
- After a retrospective surfaces a pattern
- When you discover a reusable approach
- When you want to remember something for next time

## Agent Routing

**Primary**: Coach Agent

The Coach helps format and categorize the best practice.

## Example Usage

**User Input**:
```
/add-best-practice "Always test chunking with real documents before committing to a strategy"
```

**Expected Output**:
```
## Add Best Practice

### Proposed Entry

**Category**: RAG / Data Processing

**Practice**:
> Always test chunking with real documents before committing to a
> strategy. Use 3 representative documents and measure retrieval
> quality, not just chunk count.

**When to Apply**:
- Starting any RAG or document processing project
- Evaluating chunking libraries or approaches
- Before finalizing ingestion pipeline

**Source**: Month 03 - RAG System project

---

### Preview in best_practices.md

```markdown
## RAG / Data Processing

### Chunking Strategy Testing
> Always test chunking with real documents before committing to a
> strategy. Use 3 representative documents and measure retrieval
> quality, not just chunk count.
>
> *When*: Starting RAG projects, evaluating chunking approaches
> *Source*: Month 03 (2026-01)
```

---

**Add this to best_practices.md?** (yes/modify/no)
```

## Best Practice Categories

Common categories in the system:

| Category | Examples |
|----------|----------|
| Testing | TDD patterns, test data management |
| Architecture | Design decisions, module organization |
| RAG / LLM | Chunking, embeddings, prompting |
| DevOps | CI/CD, deployment, monitoring |
| Debugging | Investigation approaches, logging |
| Planning | Estimation, scope management |
| Learning | Study techniques, resource curation |

## Batch Add (from Retro)

After `/retro`, you might add multiple:

```
/add-best-practice "Document as you go, not at the end"
/add-best-practice "Time-box research to 2h before asking for help"
```

## Related Commands

- `/retro` - Often surfaces best practices
- `/debug-learning` - Solving problems may yield practices
- `/harden` - Review feedback may suggest practices
