# How to Demo

Guide to creating effective project demonstrations.

## Overview

A good demo:
- Shows the value of your work
- Tells a story
- Handles questions gracefully
- Leaves a lasting impression

---

## Demo Structure

### 1. Introduction (30 seconds)

**What to cover**:
- What problem does this solve?
- Who cares about this problem?
- What's your solution?

**Example**:
> "Ever tried to find specific information in hundreds of documents?
> I built a RAG system that lets you ask questions in natural language
> and get accurate, sourced answers."

### 2. Live Demo (3-5 minutes)

**Structure**:
1. Setup (show starting state)
2. Action (demonstrate key feature)
3. Result (show the outcome)
4. Repeat for 2-3 key features

**Example flow**:
```
1. "Here's our document corpus — 200 technical docs"
2. "I'll ask: 'What are the authentication requirements?'"
3. "The system retrieves relevant chunks and generates an answer"
4. "Notice it cites sources — you can click to verify"
```

### 3. Technical Highlights (1-2 minutes)

**What to show**:
- One interesting technical decision
- One challenge you solved
- The architecture at a high level

**Example**:
> "Under the hood, I'm using a hybrid search approach —
> combining semantic similarity with keyword matching.
> This improved retrieval accuracy from 65% to 85%."

### 4. Q&A Preparation

**Common questions to prepare for**:
- "How does it handle [edge case]?"
- "What's the latency/performance?"
- "How would you scale this?"
- "What would you do differently?"

---

## Demo Environment Setup

### Pre-Demo Checklist

```bash
# Verify everything works
- [ ] Demo data is loaded
- [ ] Services are running
- [ ] No pending errors
- [ ] Screen resolution is readable
- [ ] Backup plan if live demo fails
```

### Demo Script

Create a repeatable demo script:

```bash
# demo_script.sh

echo "=== Demo: RAG Question Answering ==="

# Show corpus
echo "\n1. Document corpus:"
ls -la documents/ | head -5

# Ask a question
echo "\n2. Asking: 'What are the authentication requirements?'"
python query.py "What are the authentication requirements?"

# Show another query
echo "\n3. Multi-hop question:"
python query.py "How do auth requirements differ between API and web?"
```

### Fallback Plan

If live demo fails:
1. Have screenshots ready
2. Have a recorded video backup
3. Walk through code as alternative
4. Be honest: "Let me show you the code instead"

---

## Presentation Tips

### Pacing

- Don't rush
- Pause after important points
- Let the audience absorb what they see

### Narration

- Explain what you're doing before you do it
- Point out what to look at
- Verbalize the result

### Handling Errors

If something goes wrong:
- Stay calm
- Acknowledge it briefly
- Move to backup plan
- Don't apologize excessively

---

## Recording Your Demo

### Tools

- **Screen recording**: OBS, Loom, QuickTime
- **Terminal**: asciinema for terminal recordings
- **Editing**: iMovie, DaVinci Resolve (free)

### Tips

- Record in high resolution
- Zoom in on important parts
- Add captions for clarity
- Keep under 5 minutes

---

## Demo Checklist

### Before Demo

- [ ] Test complete flow end-to-end
- [ ] Clear any sensitive data
- [ ] Prepare demo data/examples
- [ ] Have backup plan ready
- [ ] Test audio/video if remote

### During Demo

- [ ] State what you're showing upfront
- [ ] Point out important details
- [ ] Handle errors gracefully
- [ ] Stay within time limit

### After Demo

- [ ] Share recording/slides if applicable
- [ ] Note questions for FAQ
- [ ] Capture feedback for improvements

---

## Example Demo Outline

### RAG Service Demo

```
1. INTRO (30 sec)
   "Finding information in docs is painful.
    I built a Q&A system for technical documentation."

2. DEMO PART 1 - Basic Query (1 min)
   - Show document corpus
   - Ask simple question
   - Show answer with sources

3. DEMO PART 2 - Complex Query (1 min)
   - Multi-hop question
   - Show reasoning/retrieval
   - Highlight accuracy

4. DEMO PART 3 - Edge Case (1 min)
   - Question with no answer
   - Show graceful handling
   - "I don't know" response

5. TECHNICAL HIGHLIGHT (1 min)
   - Show architecture diagram
   - Explain hybrid search
   - Show eval results

6. WRAP UP (30 sec)
   - Summarize what you built
   - Mention next steps
   - Invite questions
```

---

## Related Documentation

- [how-to-write-medium-post.md](how-to-write-medium-post.md) — Writing about your project
- [portfolio-checklist.md](portfolio-checklist.md) — Portfolio presentation
- [../commands.md](../commands.md) — /publish command
