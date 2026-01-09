# How to Write a Medium Post

Guide to writing about your projects for your portfolio.

## Why Write?

Writing about your work:
- Forces you to understand deeply
- Demonstrates communication skills
- Helps others learn
- Builds your professional brand

---

## Post Structure

### 1. Title (5 words)
Clear, specific, searchable.

**Good**:
- "Building a Sales Forecasting Dashboard with Python"
- "How I Built a RAG System for Documentation"
- "Creating a Data Pipeline with pandas"

**Avoid**:
- "My Project" (too vague)
- "The Ultimate Guide to Everything" (too broad)
- Clickbait

### 2. Hook (2-3 sentences)
Why should someone read this?

```
Small businesses lose money by ordering too much or too little inventory.
I built a forecasting dashboard that predicts next week's sales with 85% accuracy.
Here's how I did it.
```

### 3. The Problem (1 paragraph)
What challenge did you solve?

```
Predicting sales is hard. Historical patterns, seasonality, and random
events all play a role. Most small businesses either guess or use
expensive enterprise tools. I wanted to build something simple.
```

### 4. The Solution (2-3 paragraphs)
What did you build?

```
I built a Streamlit dashboard that:
- Takes a CSV of historical sales
- Applies an ARIMA model for forecasting
- Visualizes predictions with confidence intervals
- Exports results for planning

The user uploads their data, selects a forecast horizon, and gets
predictions in seconds. No ML expertise required.
```

### 5. How It Works (3-5 paragraphs)
Technical explanation with code.

```python
# Example code snippet
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(data, order=(1,1,1))
forecast = model.fit().forecast(steps=7)
```

Explain the code, don't just show it.

### 6. What I Learned (2-3 bullets)
Share your insights.

```
Building this taught me:
- Time series requires different preprocessing than tabular data
- Simple models often beat complex ones for small datasets
- User feedback dramatically improved the UI
```

### 7. Try It Yourself (1 paragraph)
Links and invitation.

```
The code is on GitHub: [link]
Try the live demo: [link]

Have questions? Reach out on LinkedIn: [link]
```

---

## Writing Tips

### Be Specific
- "Improved accuracy by 15%" not "made it better"
- "Used ARIMA because..." not "used a model"
- Show actual numbers and results

### Show, Don't Tell
- Include screenshots
- Show code snippets
- Include diagrams

### Keep It Scannable
- Use headers
- Use bullet points
- Keep paragraphs short
- Add images every few paragraphs

### Be Honest
- Share what was hard
- Mention limitations
- Don't oversell

---

## Code in Posts

### Do
```python
# Brief, focused snippets
def predict(data, horizon=7):
    model = ARIMA(data, order=(1,1,1))
    return model.fit().forecast(steps=horizon)
```

### Don't
```python
# Entire files
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
# ... 100 more lines
```

Link to the full code on GitHub instead.

---

## Images

### What to Include
- Architecture diagrams
- Screenshots of UI
- Charts/graphs of results
- Before/after comparisons

### How to Make Them
- Screenshots: Cleanshot, built-in tools
- Diagrams: Excalidraw, draw.io
- Charts: Export from matplotlib, Plotly

### Tips
- Add alt text (accessibility)
- Keep them readable
- Annotate when helpful

---

## Template

```markdown
# [Title: What You Built]

[Hook: Why this matters - 2 sentences]

## The Problem

[What challenge did you face? Who has this problem?]

## The Solution

[What did you build? Overview without deep technical detail]

[Screenshot or diagram]

## How It Works

### [Component 1]
[Explanation]
[Code snippet if relevant]

### [Component 2]
[Explanation]
[Code snippet if relevant]

## Results

[What did you achieve? Metrics if available]

[Chart or screenshot]

## What I Learned

- [Learning 1]
- [Learning 2]
- [Learning 3]

## Try It Yourself

[Link to GitHub]
[Link to demo if available]

---

*Thanks for reading! Connect with me on [LinkedIn].*
```

---

## Publishing Checklist

Before publishing:

- [ ] Title is clear and specific
- [ ] Hook grabs attention
- [ ] Technical content is accurate
- [ ] Code snippets are tested
- [ ] Images are clear and relevant
- [ ] Links work
- [ ] Proofread for typos
- [ ] Asked someone else to review

---

## Where to Publish

### Medium
- Built-in audience
- Clean reading experience
- SEO friendly

### Dev.to
- Developer-focused
- No paywall
- Great community

### Personal Blog
- Full control
- Own your content
- Can cross-post

### LinkedIn Articles
- Professional network
- Good for career building
- Less technical depth

---

## After Publishing

1. **Share** on social media
2. **Respond** to comments
3. **Track** views/engagement
4. **Update** if you improve the project
5. **Add** to your portfolio

---

## Related

- [How to Demo](how-to-demo.md) — Video/live demonstrations
- [Portfolio Checklist](portfolio-checklist.md) — Full portfolio guide
- [/publish command](../../.claude/commands/publish.md) — Prepare write-up
