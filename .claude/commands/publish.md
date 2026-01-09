# Command: /publish

## Purpose

Prepare a deliverable for external publishing (demo, blog post, portfolio). This command ensures your work is presentation-ready.

## Inputs

- Deliverable to publish
- Target audience (optional)
- Publishing platform (optional)

## Outputs

- Publishing checklist status
- Demo script/video outline
- Blog post template (if applicable)
- Portfolio entry draft
- **All publishing actions require user approval**

## When to Use

- After `/harden` passes
- Ready to share work externally
- End of month for portfolio update
- Before presenting to others

## Agent Routing

**Primary**: Reviewer Agent (quality gates)
**Secondary**: Coach Agent (presentation tips)

## Example Usage

**User Input**:
```
/publish
```

**Expected Output**:
```
## Publish Preparation: Month 03 RAG System

### Pre-publish Checklist

| Item | Status |
|------|--------|
| All tests passing | ✅ |
| No secrets in code | ✅ |
| README complete | ✅ |
| Demo works | ✅ |
| Code linted | ⚠️ (3 warnings) |
| Links valid | ✅ |

### Lint Warnings
Run `ruff check --fix` to auto-fix:
- Line too long (3 occurrences)

---

### Demo Script

**Duration**: 3-5 minutes

1. **Intro** (30s)
   - "This is a RAG system that retrieves relevant context for questions"

2. **Show the problem** (30s)
   - Query without RAG → poor answer
   - "Traditional search doesn't understand semantic meaning"

3. **Demo the solution** (2m)
   - Run `python demo.py`
   - Show document ingestion
   - Show retrieval results
   - Show improved answer quality

4. **Technical highlights** (1m)
   - Chunking strategy
   - Vector store choice
   - Evaluation metrics

5. **Wrap up** (30s)
   - What you learned
   - Next steps

---

### Blog Post Template

**Title**: Building a RAG System from Scratch: Lessons Learned

**Outline**:
1. Why RAG? (The problem it solves)
2. Architecture overview
3. Key decisions (chunking, vector store, embeddings)
4. Challenges and solutions
5. Results and metrics
6. What I'd do differently

See: `docs/publishing/how-to-write-medium-post.md`

---

### Portfolio Entry

```markdown
## RAG System (Month 03)

**Technologies**: Python, Qdrant, OpenAI Embeddings, FastAPI

**Summary**: Built a retrieval-augmented generation system that
improves answer quality by 40% on domain-specific questions.

**Links**:
- [GitHub Repo](link)
- [Demo Video](link)
- [Blog Post](link)
```

---

**Ready to publish?**
- [ ] Fix lint warnings
- [ ] Record demo video
- [ ] Write blog post
- [ ] Update portfolio
```

## Publishing Checklist (Full)

See `.claude/hooks/pre_publish_check.sh` for automated checks:
- Tests passing
- Linting clean
- No secrets
- Docs complete
- Links valid
- Demo working

## Related Commands

- `/harden` - Quality review first
- `/retro` - Reflect on what worked
- `/evaluate` - Formal progress assessment
