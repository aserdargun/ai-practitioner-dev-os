# Portfolio Checklist

Presenting your projects professionally.

## Overview

A strong portfolio project includes:
- Clear description of what you built
- Evidence of your skills
- Working demo or screenshots
- Clean, documented code
- Reflection on learnings

---

## Portfolio Entry Format

### Template

```markdown
## [Project Name]

**Summary**: [One-line description of what it does]

**Technologies**: [Key technologies used]

**Links**: [GitHub] | [Demo] | [Write-up]

### The Problem
[What problem does this solve? Who cares?]

### My Solution
[High-level description of your approach]

### Key Features
- [Feature 1]
- [Feature 2]
- [Feature 3]

### Technical Highlights
- [Interesting technical decision or challenge]
- [Performance metrics or results]

### What I Learned
- [Learning 1]
- [Learning 2]

### Screenshots/Demo
[Include visuals]
```

### Example Entry

```markdown
## RAG Document Q&A

**Summary**: Natural language Q&A over technical documentation

**Technologies**: Python, FastAPI, LangChain, Chroma, OpenAI

**Links**: [GitHub](link) | [Demo](link) | [Blog Post](link)

### The Problem
Engineers waste hours searching through documentation. They need
instant, accurate answers to technical questions.

### My Solution
A RAG system that indexes documents, retrieves relevant chunks,
and generates accurate answers with source citations.

### Key Features
- Natural language queries
- Source citation for verification
- Hybrid search (semantic + keyword)
- 85% retrieval accuracy

### Technical Highlights
- Implemented custom hybrid search that improved accuracy by 20%
- Built evaluation harness with 50 golden questions
- Deployed as containerized API with health checks

### What I Learned
- Evaluate retrieval separately from generation
- Chunk size significantly impacts accuracy
- Build evaluation sets early in the project

### Screenshots
[Architecture diagram]
[Query interface]
[Evaluation results]
```

---

## Project Checklist

### Code Quality

- [ ] README with clear setup instructions
- [ ] Requirements/dependencies specified
- [ ] Code is clean and readable
- [ ] Functions have docstrings
- [ ] No secrets in code
- [ ] Tests present and passing

### Documentation

- [ ] What the project does
- [ ] How to set it up
- [ ] How to use it
- [ ] Technical decisions explained
- [ ] Known limitations noted

### Demo Materials

- [ ] Screenshots of key features
- [ ] Demo video (optional but valuable)
- [ ] Live demo link (if applicable)
- [ ] Sample inputs/outputs

### Presentation

- [ ] Clear project name
- [ ] One-line summary
- [ ] Technology list
- [ ] Problem/solution framing
- [ ] Results/metrics

---

## GitHub Repository Checklist

### README Structure

```markdown
# Project Name

[One-line description]

## Features
- Feature 1
- Feature 2

## Quick Start
```bash
pip install -r requirements.txt
python main.py
```

## Usage
[How to use the project]

## Architecture
[High-level architecture]

## Results
[Key metrics/outcomes]

## License
[License info]
```

### Repository Organization

```
project/
├── README.md           # Project overview
├── requirements.txt    # Dependencies
├── pyproject.toml      # Modern Python config
├── src/                # Source code
├── tests/              # Test suite
├── docs/               # Documentation
├── examples/           # Usage examples
└── .github/            # CI/CD workflows
```

### Nice-to-Haves

- [ ] GitHub Actions badge
- [ ] License badge
- [ ] Test coverage badge
- [ ] Well-organized issues/PRs

---

## Presentation Platforms

### GitHub Profile README

Add project highlights to your GitHub profile:

```markdown
### Featured Projects

- [RAG Q&A](link) — Natural language Q&A over documents
- [ML Pipeline](link) — End-to-end ML training pipeline
```

### LinkedIn

- Add projects to your profile
- Share posts about completing projects
- Include demo links and screenshots

### Personal Website

- Dedicated projects page
- Consistent presentation format
- Easy navigation

---

## Common Mistakes to Avoid

### Code Issues

- Hardcoded paths or credentials
- No documentation
- No tests
- Messy commit history
- Broken dependencies

### Presentation Issues

- Vague descriptions ("ML project")
- No problem statement
- No results/metrics
- Missing visuals
- Broken links

### Completeness Issues

- README says "TODO"
- Half-finished features
- No setup instructions
- Doesn't actually run

---

## Portfolio Review Questions

Ask yourself:

1. **Would a hiring manager understand what this does in 30 seconds?**
2. **Can someone clone and run this without asking questions?**
3. **Does this demonstrate skills relevant to my target role?**
4. **Are there concrete results/metrics?**
5. **Would I be comfortable discussing this in an interview?**

---

## Updating Your Portfolio

### When to Add Projects

- After completing a significant project
- After learning a new technology
- After solving an interesting problem

### When to Remove Projects

- Old/outdated technology
- No longer representative of your skills
- Embarrassingly simple
- Can't explain it anymore

### Maintaining Projects

- Periodically check links work
- Update dependencies
- Archive rather than delete

---

## Related Documentation

- [how-to-demo.md](how-to-demo.md) — Creating demonstrations
- [how-to-write-medium-post.md](how-to-write-medium-post.md) — Writing about projects
