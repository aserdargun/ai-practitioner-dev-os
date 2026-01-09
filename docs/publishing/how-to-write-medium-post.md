# How to Write a Medium Post

Guide to writing technical blog posts about your projects.

## Overview

A good technical post:
- Teaches something useful
- Tells a compelling story
- Shows your thinking process
- Provides actionable takeaways

---

## Post Structure

### 1. Hook (First Paragraph)

**Goal**: Make readers want to continue.

**Techniques**:
- Start with a problem
- Use a surprising statistic
- Ask a question
- Share a relatable frustration

**Example**:
> "I spent three hours debugging why my RAG system was giving wrong answers.
> The model was fine. The prompt was fine. The bug? My retrieval was returning
> irrelevant chunks. Here's how I fixed it and what I learned."

### 2. Context (Background)

**Goal**: Set up the reader's understanding.

**Include**:
- What you were trying to build
- Why it matters
- What approach you took

**Example**:
> "I was building a Q&A system for our internal documentation — about 500
> technical guides that employees struggled to search through. The goal:
> let anyone ask questions in plain English and get accurate answers."

### 3. The Journey (Main Content)

**Goal**: Share what you did and learned.

**Structure options**:
- Problem → Attempt → Failure → Insight → Solution
- Step 1 → Step 2 → Step 3 (tutorial style)
- Before → Challenge → After

**Include**:
- Code snippets (but not too much)
- Diagrams when helpful
- Specific numbers and results

### 4. Key Learnings (Takeaways)

**Goal**: Give readers something actionable.

**Format**:
```
## Key Takeaways

1. **Always evaluate retrieval separately from generation.**
   Don't assume retrieval is working just because you're getting answers.

2. **Chunk size matters more than you think.**
   Smaller chunks (500 tokens) significantly outperformed larger ones for our use case.

3. **Build an evaluation set early.**
   Having 50 golden Q&A pairs saved hours of debugging later.
```

### 5. Conclusion (Call to Action)

**Goal**: End with purpose.

**Options**:
- Link to your code
- Invite discussion
- Suggest next steps
- Ask a question

---

## Writing Tips

### Keep It Scannable

- Use headers liberally
- Keep paragraphs short (3-4 sentences max)
- Use bullet points and lists
- Include code blocks

### Show, Don't Just Tell

Instead of:
> "The retrieval quality was poor."

Write:
> "Of 100 test queries, only 45 returned the correct document in the top 3 results."

### Include Visuals

- Architecture diagrams
- Before/after comparisons
- Evaluation results (charts/tables)
- Screenshots of the working system

### Code Snippets

Keep them focused:

```python
# Good: focused on the insight
def evaluate_retrieval(retriever, golden_set):
    """Evaluate retrieval quality separately from generation."""
    hits = 0
    for item in golden_set:
        retrieved = retriever.get_relevant_documents(item["question"])
        if item["source"] in [d.metadata["source"] for d in retrieved[:3]]:
            hits += 1
    return hits / len(golden_set)
```

Avoid: dumping your entire codebase

---

## Title Options

### Formula 1: "How I [Did X]"
- "How I Built a RAG System That Actually Works"
- "How I Improved ML Model Accuracy by 20%"

### Formula 2: "[Number] Things I Learned"
- "5 Things I Learned Building My First RAG System"
- "3 Mistakes to Avoid in ML Evaluation"

### Formula 3: "The [Adjective] Guide to [Topic]"
- "The Practical Guide to RAG Evaluation"
- "A Beginner's Guide to ML Experiment Tracking"

---

## Outline Template

```markdown
# [Title]

## Hook
[Opening that grabs attention — 2-3 sentences]

## The Problem
[What you were trying to solve — 1 paragraph]

## My Approach
[High-level approach — 1-2 paragraphs]

## The Implementation
### [Step/Phase 1]
[Description + code snippet]

### [Step/Phase 2]
[Description + code snippet]

### [Step/Phase 3]
[Description + code snippet]

## Results
[What you achieved — include numbers]

## Key Learnings
1. **[Learning 1]** — [Explanation]
2. **[Learning 2]** — [Explanation]
3. **[Learning 3]** — [Explanation]

## Conclusion
[Wrap-up + call to action]

---

*[Bio/Links]*
```

---

## Publishing Checklist

### Before Publishing

- [ ] Read aloud for flow
- [ ] Check code snippets compile/run
- [ ] Verify all links work
- [ ] Add relevant tags
- [ ] Include featured image
- [ ] Proofread one more time

### After Publishing

- [ ] Share on LinkedIn/Twitter
- [ ] Post in relevant communities
- [ ] Respond to comments
- [ ] Add to your portfolio

---

## Medium-Specific Tips

### Formatting

- Use headers (H2, H3)
- Add code blocks with language tags
- Embed GitHub gists for longer code
- Use horizontal rules to separate sections

### SEO

- Include keywords in title and first paragraph
- Use descriptive header text
- Write a compelling subtitle

### Engagement

- Respond to comments
- Clap for others' posts
- Follow relevant publications

---

## Example Posts to Study

Look for posts that:
- Have clear structure
- Include code but aren't overwhelming
- Tell a story
- Provide actionable takeaways

---

## Related Documentation

- [how-to-demo.md](how-to-demo.md) — Demonstrating your project
- [portfolio-checklist.md](portfolio-checklist.md) — Portfolio presentation
