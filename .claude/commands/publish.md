# Command: /publish

## Purpose

Prepare your project for publication: create demo materials, write-up, and portfolio entry.

## Inputs

Optional context:
- Target audience
- Key points to highlight
- Demo scenario

The command reads from:
- Your completed project
- Current month's README (publishing requirements)
- `docs/publishing/` guides
- `.claude/memory/progress_log.jsonl`

## Outputs

- Demo script/guide
- Write-up outline
- Portfolio entry draft
- Publishing checklist

**Note**: All outputs are drafts for your review.

## When to Use

- Week 4 of monthly cycle
- After hardening is complete
- When ready to share your work

## Agent Routing

**Primary**: Builder Agent

The Builder helps structure your demo and write-up based on the project deliverables.

## Example Usage

```
/publish
```

Or with context:

```
/publish

I want to write a Medium post about this RAG project.
Focus on the evaluation approach I used.
```

## Output Format

```markdown
## Publishing Package — [Project Name]

### Demo Guide

#### Setup
```bash
# Commands to run the demo
[setup commands]
```

#### Demo Script
1. **Introduction** (30 sec)
   - What problem does this solve?
   - Key features

2. **Live Demo** (3-5 min)
   - Step 1: [action] → [expected result]
   - Step 2: [action] → [expected result]
   - Step 3: [action] → [expected result]

3. **Technical Highlights** (1-2 min)
   - [Key technical decision]
   - [Interesting challenge solved]

4. **Q&A Prep**
   - Likely question 1: [answer]
   - Likely question 2: [answer]

### Write-up Outline

#### Title Options
1. [Option 1]
2. [Option 2]

#### Structure
1. **Hook** — The problem/opportunity
2. **Context** — Why this matters
3. **Solution** — What you built
4. **Technical Deep Dive** — How it works
5. **Results** — What you achieved
6. **Learnings** — What you discovered
7. **Next Steps** — Future improvements

#### Key Points to Include
- [Point 1]
- [Point 2]
- [Point 3]

### Portfolio Entry

```markdown
## [Project Name]

**Summary**: [One-line description]

**Technologies**: [list]

**Links**: [repo] | [demo] | [write-up]

**Highlights**:
- [Achievement 1]
- [Achievement 2]
```

### Publishing Checklist
- [ ] Demo tested and working
- [ ] Write-up drafted
- [ ] Screenshots/recordings captured
- [ ] Code repo cleaned up
- [ ] README finalized
- [ ] Portfolio entry created

---
**Ready to publish?**
```

## Publishing Resources

- [docs/publishing/how-to-demo.md](../../docs/publishing/how-to-demo.md)
- [docs/publishing/how-to-write-medium-post.md](../../docs/publishing/how-to-write-medium-post.md)
- [docs/publishing/portfolio-checklist.md](../../docs/publishing/portfolio-checklist.md)
