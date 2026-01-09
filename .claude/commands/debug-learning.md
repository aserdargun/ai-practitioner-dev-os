# Command: /debug-learning

## Purpose

Get help when stuck on a concept, task, or blocker. This command connects you with the Coach agent for targeted assistance.

## Inputs

- Description of the blocker (optional, will be asked)
- What you've tried (optional)

## Outputs

- Diagnostic questions
- Targeted advice
- Alternative approaches
- Resources to try
- Small experiments to unblock

## When to Use

- When stuck on a concept
- When implementation isn't working
- When feeling frustrated or overwhelmed
- When unsure how to proceed
- When the same problem keeps recurring

## Agent Routing

**Primary**: Coach Agent
**Secondary**: Researcher Agent (if research is needed)

## Example Usage

**User Input**:
```
/debug-learning
```

**Expected Output**:
```
## Debug Learning Session

I'm here to help you get unstuck. Let's figure this out together.

### First, some questions:

1. **What are you trying to accomplish?**
   (Be specific: "implement X" or "understand Y")

2. **What have you tried so far?**
   (Code, reading, experiments)

3. **Where exactly does it break or confuse you?**
   (Error message, conceptual gap, decision paralysis)

---

*Waiting for your responses...*
```

**After user responds**:

```
## Analysis

Based on what you've shared:

**Blocker Type**: Conceptual gap (embedding dimensions)

### The Core Issue

You're confused about why embeddings are 1536-dimensional and how
that relates to semantic similarity.

### Quick Explanation

Think of embeddings as coordinates in a high-dimensional space:
- Each dimension captures some aspect of meaning
- Similar concepts end up near each other
- 1536 dimensions = 1536 aspects of meaning
- Cosine similarity measures the angle between vectors

**Analogy**: Like GPS coordinates (2D) but for meaning (1536D)

### Try This Experiment

```python
from openai import OpenAI
client = OpenAI()

# Get embeddings for similar words
e1 = client.embeddings.create(input="happy", model="text-embedding-3-small")
e2 = client.embeddings.create(input="joyful", model="text-embedding-3-small")
e3 = client.embeddings.create(input="refrigerator", model="text-embedding-3-small")

# Compare similarities
# happy-joyful should be high
# happy-refrigerator should be low
```

### Resources

1. [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
2. `.claude/skills/rag-with-evals.md` - Embeddings section
3. [3Blue1Brown: Vectors](https://www.youtube.com/watch?v=fNk_zzaMoSs)

---

**Did this help?** Or would you like to go deeper on any part?
```

## Common Blocker Types

| Type | Approach |
|------|----------|
| Conceptual gap | Explain differently, use analogies |
| Implementation stuck | Rubber duck, simplify scope |
| Decision paralysis | List trade-offs, pick one and iterate |
| Error confusion | Read error carefully, isolate cause |
| Overwhelmed | Break down, focus on smallest next step |
| Motivation low | Acknowledge, find small win |

## Escalation

If Coach can't help:
- Research Agent for deep technical research
- Planner Agent to revise scope/approach
- Community resources (Stack Overflow, Discord, etc.)

## Related Commands

- `/status` - See if the blocker is tracked
- `/plan-week` - Revise plan if needed
- `/retro` - Capture the learning after unblocking
