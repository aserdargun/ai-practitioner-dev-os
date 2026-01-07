# How to Demo Your Work

Guide to preparing and presenting your projects for demo or portfolio.

---

## Overview

At the end of each month (or when you're ready), you'll want to demo your work. This guide covers preparation, presentation, and follow-up.

---

## Before the Demo

### 1. Run Pre-Publish Checks

```bash
bash .claude/hooks/pre_publish_check.sh
```

Or use the command:
```
/publish
```

Fix any errors before proceeding.

### 2. Verify Everything Works

```bash
# Run all tests
pytest

# Start the application (if applicable)
uvicorn src.main:app --reload

# Verify key features manually
```

### 3. Prepare Demo Data

- Have sample inputs ready
- Prepare edge cases to show error handling
- Create a demo script/checklist

### 4. Update Documentation

Ensure README includes:
- [ ] Project description
- [ ] How to run locally
- [ ] Key features
- [ ] Screenshots/GIFs (if applicable)
- [ ] Known limitations

---

## Demo Checklist

### Technical Preparation

- [ ] All tests passing
- [ ] No lint errors
- [ ] Application starts without errors
- [ ] Demo data prepared
- [ ] Network/API keys configured
- [ ] Backup plan if live demo fails

### Content Preparation

- [ ] Clear problem statement
- [ ] Solution overview (30 seconds)
- [ ] Key features list
- [ ] Technical decisions to highlight
- [ ] Challenges overcome
- [ ] Future improvements

### Logistics

- [ ] Demo environment ready
- [ ] Screen sharing tested
- [ ] Recording setup (if needed)
- [ ] Time allocated (aim for 5-10 min)

---

## Demo Structure

### 1. Introduction (1 minute)

```
"This month I built [PROJECT NAME], which solves [PROBLEM].
The main features are [FEATURE 1], [FEATURE 2], and [FEATURE 3]."
```

### 2. Live Demo (3-5 minutes)

Show the application in action:
1. Start with the happy path
2. Show 2-3 key features
3. Demonstrate error handling
4. Show tests passing (briefly)

### 3. Technical Highlights (2 minutes)

```
"Some interesting technical decisions:
- I used [TECHNOLOGY] because [REASON]
- The [COMPONENT] handles [CHALLENGE] by [SOLUTION]"
```

### 4. Learnings (1 minute)

```
"Key things I learned:
- [LEARNING 1]
- [LEARNING 2]
- If I were to do it again, I would [IMPROVEMENT]"
```

### 5. Questions (2+ minutes)

Be prepared for:
- "Why did you choose X over Y?"
- "How would this scale?"
- "What would you add next?"

---

## Demo Tips

### Do

- **Practice the flow** before the actual demo
- **Start the app before presenting** (avoid cold start delays)
- **Have a backup** (screenshots, recorded video)
- **Speak to the "why"** not just the "what"
- **Time yourself** during practice

### Don't

- **Don't apologize** for incomplete features
- **Don't read code line by line** (highlight key parts)
- **Don't debug live** (if something breaks, move on)
- **Don't rush** (better to show less clearly than more chaotically)

---

## Recording Your Demo

### Tools

- **OBS Studio**: Free, cross-platform
- **Loom**: Easy web-based recording
- **QuickTime** (Mac): Built-in screen recording
- **Asciinema**: For terminal-only demos

### Recording Tips

1. **Resolution**: 1920x1080 recommended
2. **Font size**: Increase for readability
3. **Clean desktop**: Hide notifications
4. **Narrate clearly**: Explain what you're doing
5. **Keep under 10 minutes**: Edit if needed

### Post-Recording

- Trim dead air at start/end
- Add title card (project name, your name)
- Upload to YouTube (unlisted) or your portfolio

---

## Portfolio Integration

### README Structure for Portfolio

```markdown
# Project Name

Brief description that hooks the reader.

## Problem

What problem does this solve?

## Solution

How does it solve it?

## Demo

[Link to video or GIF]

## Key Features

- Feature 1
- Feature 2
- Feature 3

## Technical Stack

- Python 3.11
- FastAPI
- PostgreSQL
- etc.

## Getting Started

```bash
git clone ...
pip install -r requirements.txt
uvicorn src.main:app
```

## Architecture

[Diagram or description]

## What I Learned

Key takeaways from this project.

## Future Work

What would you add with more time?
```

### GitHub Repository Hygiene

- [ ] Clear README
- [ ] Proper .gitignore
- [ ] No secrets committed
- [ ] Tags for releases
- [ ] Issues for known limitations

---

## Common Demo Scenarios

### API Demo

```python
# Show in this order:
1. Health endpoint (prove it runs)
2. Main functionality (POST/GET flow)
3. Validation (show error response)
4. Swagger docs (/docs endpoint)
```

### Data Pipeline Demo

```python
# Show in this order:
1. Input data (sample)
2. Run pipeline
3. Output data
4. Quality checks/validation
5. Logs/monitoring
```

### ML Model Demo

```python
# Show in this order:
1. Problem and data
2. Model prediction (live or recorded)
3. Evaluation metrics
4. Edge cases
5. How to retrain/update
```

---

## Handling Demo Failures

### If the App Crashes

"Let me show you what that feature does via [screenshots/recorded video].
This is why we have backup demos!"

### If You Forget Something

"I wanted to also mention... [recover naturally]"

### If Asked About Limitations

"Great question. Currently it doesn't handle [X], but I've documented
that as a future improvement. My approach would be [brief idea]."

---

## After the Demo

### Collect Feedback

- What resonated?
- What was confusing?
- What questions came up?

### Document Learnings

Add to your journal:
- What went well
- What to improve
- Feedback received

### Update Portfolio

- Add recording/screenshots
- Update README based on feedback
- Create shareable links

---

## See Also

- [How to Use](../how-to-use.md) — Workflow guide
- [Commands Guide](../commands.md) — `/publish` command
- [Hooks Guide](../hooks.md) — `pre_publish_check.sh`
