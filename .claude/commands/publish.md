# Command: /publish

## Purpose
Prepare a completed project for public sharing, including demo materials, write-up for blog/portfolio, and presentation assets.

## Inputs
- **Project**: Which project to publish
- **Audience**: Who will see this (recruiters, peers, general)
- **Format**: Blog post, portfolio entry, demo video script

## Outputs
- **Demo Guide**: Step-by-step demo instructions with screenshots
- **Write-up Draft**: Blog post or portfolio description
- **Assets**: Screenshots, diagrams, GIFs
- **Publish Checklist**: Verification before going public

## When to Use
- When project is complete and hardened
- Building your portfolio
- Preparing for job applications
- Sharing learnings with the community

## Agent Routing
**Builder** — creates demo materials and assets

## Example Usage

### Basic Publish
```
/publish the forecasting project
For my portfolio, targeting recruiters
```

### Blog Post
```
/publish Month 3 project as a Medium post
Explain the technical decisions and learnings
```

### Demo Focus
```
/publish
Create a demo script I can record as a 3-minute video
Highlight the key features
```

## Sample Output

```
📝 PUBLISH PACKAGE — Sales Forecasting Dashboard

Demo Guide:
1. Start the app: streamlit run app.py
2. Upload sample data (data/sample_sales.csv)
3. Select forecast horizon (7 days)
4. Show prediction chart
5. Export results

Screenshots Needed:
☐ Dashboard home screen
☐ Data upload flow
☐ Forecast visualization
☐ Export dialog

Write-up Draft:

# Building a Sales Forecasting Dashboard with Python

## The Problem
Small businesses need simple forecasting tools...

## The Solution
I built a Streamlit dashboard that...

## Technical Highlights
- ARIMA model for time series
- Interactive Plotly charts
- CSV export functionality

## What I Learned
- Time series data requires careful preprocessing
- ARIMA parameter tuning matters
- User feedback improved the UI significantly

## Try It Yourself
[Link to repo]
[Link to demo]

---

Publish Checklist:
☐ Code is public on GitHub
☐ README is polished
☐ Demo can run standalone
☐ Screenshots captured
☐ Write-up reviewed for typos
☐ Personal branding consistent

Recommended Platforms:
- GitHub (code + README)
- Medium or Dev.to (write-up)
- LinkedIn (announcement)
- Personal portfolio site
```

## Publishing Tips

### For Recruiters
- Lead with business impact
- Show technical depth without jargon
- Include metrics if possible
- Make it easy to run/demo

### For Peers
- Focus on technical decisions
- Share learnings and gotchas
- Include code snippets
- Invite feedback

### For Learning
- Document your journey
- Be honest about challenges
- Share resources that helped
- Connect to bigger goals

## Related Commands
- `/harden` — Ensure quality before publishing
- `/retro` — Extract learnings to include
- `/add-best-practice` — Capture insights
