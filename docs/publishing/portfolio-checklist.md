# Portfolio Checklist

Use this checklist to ensure your projects are portfolio-ready.

## What Makes a Good Portfolio Project?

A strong portfolio project demonstrates:

1. **Problem Solving**: Clear problem → solution narrative
2. **Technical Skills**: Appropriate use of tools and techniques
3. **Communication**: Well-documented and explainable
4. **Completeness**: Works end-to-end, not just a notebook
5. **Quality**: Tests, error handling, clean code

## Project Checklist

### Documentation

- [ ] **README.md** exists and includes:
  - [ ] Project title and description
  - [ ] Problem statement
  - [ ] Solution approach
  - [ ] How to run the code
  - [ ] Results summary
  - [ ] Technologies used
  - [ ] Author information

- [ ] **Code comments** explain non-obvious logic
- [ ] **Docstrings** on public functions
- [ ] **Architecture diagram** (if applicable)

### Code Quality

- [ ] **Runs without errors** from fresh clone
- [ ] **Dependencies documented** (requirements.txt or pyproject.toml)
- [ ] **Environment reproducible** (clear setup instructions)
- [ ] **Follows style guide** (passes linting)
- [ ] **No hardcoded paths** or secrets
- [ ] **Modular structure** (not one giant script)

### Testing

- [ ] **Tests exist** and pass
- [ ] **Core functionality covered**
- [ ] **Edge cases handled**
- [ ] **CI runs tests** (optional but impressive)

### Results

- [ ] **Metrics documented** with context
- [ ] **Baseline comparison** included
- [ ] **Visualizations** that tell the story
- [ ] **Honest about limitations**

### Presentation

- [ ] **Demo available** (live, video, or screenshots)
- [ ] **Write-up exists** (README or blog post)
- [ ] **LinkedIn-ready summary** (2-3 sentences)

## README Template

```markdown
# Project Name

Brief description of what this project does.

## Problem

What problem does this solve? Why does it matter?

## Solution

How does your solution work? Key approach/insight.

## Results

| Metric | Value |
|--------|-------|
| Accuracy | 0.85 |
| F1 Score | 0.82 |

## Demo

[Link to demo or screenshots]

## Quick Start

\`\`\`bash
# Clone the repo
git clone https://github.com/username/project.git
cd project

# Install dependencies
pip install -r requirements.txt

# Run the demo
python demo.py
\`\`\`

## Project Structure

\`\`\`
project/
├── data/           # Sample data
├── src/            # Source code
├── tests/          # Test files
├── notebooks/      # Exploration notebooks
├── README.md       # This file
└── requirements.txt
\`\`\`

## Technologies

- Python 3.11
- scikit-learn
- pandas
- FastAPI

## What I Learned

Key insights from building this project.

## Future Improvements

What you'd add with more time.

## Author

Your Name - [LinkedIn](link) - [GitHub](link)
```

## Portfolio Page Structure

If you have a portfolio website:

### Project Card (Summary View)

```
┌─────────────────────────────────┐
│ [Screenshot/GIF]                │
├─────────────────────────────────┤
│ Project Name                    │
│ Brief 1-sentence description    │
│                                 │
│ [Python] [ML] [FastAPI]         │
│                                 │
│ [Demo] [Code] [Write-up]        │
└─────────────────────────────────┘
```

### Project Detail Page

```
# Project Name

[Hero image or demo GIF]

## Overview
2-3 paragraphs explaining the project

## Technical Highlights
- Key technical decisions
- Interesting challenges solved
- Technologies used

## Results
Metrics and impact

## Links
- [Live Demo]
- [GitHub Repo]
- [Blog Post]
- [Video Walkthrough]
```

## LinkedIn Post Template

When sharing your project:

```
🚀 Just shipped: [Project Name]

[One sentence about what it does]

The challenge: [Problem in 1-2 sentences]

My approach: [Solution in 2-3 sentences]

Key results:
• [Metric 1]
• [Metric 2]
• [Insight]

What I learned: [1-2 sentences]

Check it out: [Link]

#MachineLearning #DataScience #Python
```

## Quality Levels

### Minimum Viable Portfolio (MVP)

- [ ] README with problem/solution
- [ ] Code runs from clone
- [ ] Basic results documented

### Good Portfolio

Everything in MVP plus:
- [ ] Tests exist
- [ ] Demo available
- [ ] Write-up or blog post
- [ ] Clean code structure

### Excellent Portfolio

Everything in Good plus:
- [ ] CI/CD pipeline
- [ ] Deployed demo
- [ ] Comprehensive documentation
- [ ] Video walkthrough
- [ ] Multiple iterations documented

## Common Mistakes

### Avoid

- Jupyter notebooks as the only artifact
- "My ML Project" as the title
- No instructions to run the code
- Screenshots instead of working code
- Claiming results you can't reproduce

### Instead

- Extract code into proper modules
- Descriptive, specific titles
- Step-by-step setup instructions
- Working code with test data
- Reproducible experiments with seeds

## Monthly Portfolio Review

Each month, review your portfolio:

1. **Update** projects with new learnings
2. **Archive** outdated projects
3. **Highlight** your best 3-5 projects
4. **Refresh** READMEs and screenshots
5. **Check** all links still work

## Related Documentation

- [How to Demo](how-to-demo.md)
- [How to Write Medium Post](how-to-write-medium-post.md)
