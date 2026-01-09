# Month 02: Data Analysis & Visualization

## Why It Matters

Understanding data before modeling is critical. This month builds your exploratory data analysis (EDA) and visualization skills—the foundation for all machine learning work.

**Job Relevance**: Data scientists and ML engineers spend 60-80% of their time on data understanding and preparation. Strong EDA skills separate good practitioners from great ones.

---

## Prerequisites

- Month 01 completed (Python, pandas, NumPy)
- Jupyter environment set up
- Basic statistics knowledge

---

## Learning Goals

### Tier 1 Focus
- Statistics (descriptive and inferential)
- Probability fundamentals
- Matplotlib for static plots
- Seaborn for statistical visualization
- Plotly for interactive charts
- Jupyter notebooks
- A/B testing concepts

### Tier 2 Introduction
- Streamlit for data apps
- Dash for dashboards
- Statistical testing with scipy

### Tier 3 Preview
- Large-scale data visualization patterns

---

## Main Project: EDA Dashboard

Build an exploratory data analysis system that:
1. Loads and profiles datasets automatically
2. Generates statistical summaries
3. Creates interactive visualizations
4. Identifies data quality issues
5. Presents findings in a Streamlit app

### Deliverables

1. **`eda/`** - EDA library with reusable functions
2. **`app.py`** - Streamlit dashboard
3. **`notebooks/`** - Analysis notebooks
4. **`reports/`** - Generated EDA reports
5. **`tests/`** - Unit tests

### Definition of Done

- [ ] Auto-profiling for any tabular dataset
- [ ] At least 10 visualization types
- [ ] Statistical summary generation
- [ ] Data quality report
- [ ] Working Streamlit dashboard
- [ ] Documentation with examples

---

## Week-by-Week Plan

### Week 1: Statistics Foundations

**Focus**: Understand your data statistically.

- Descriptive statistics (mean, median, std, quartiles)
- Distributions and probability
- Correlation analysis
- Statistical significance basics

**Milestone**: Functions that compute complete statistical profiles.

### Week 2: Visualization Mastery

**Focus**: Tell stories with data.

- Matplotlib fundamentals
- Seaborn for statistical plots
- Choosing the right chart type
- Color theory and accessibility
- Multi-panel figures

**Milestone**: Library of 10+ reusable visualization functions.

### Week 3: Interactive & Dashboards

**Focus**: Make data explorable.

- Plotly for interactivity
- Streamlit basics
- Dashboard design principles
- User experience for data apps

**Milestone**: Interactive dashboard with multiple views.

### Week 4: Quality & Polish

**Focus**: Automate and document.

- Data quality metrics
- Automated reporting
- A/B testing analysis
- Testing and documentation

**Milestone**: Complete EDA system with tests and docs.

---

## Stretch Goals

- Add statistical hypothesis testing
- Implement anomaly detection visualization
- Create PDF report generation
- Add correlation clustering
- Build automated insight generation

---

## Claude Prompts

### Planning
```
/plan-week
```

### EDA Guidance
```
As the Researcher, what are the best practices for EDA on tabular data?
```

### Skill Application
```
Use the EDA to Insight skill for analyzing [dataset name].
```

### Visualization Review
```
/harden

Review my visualization code for clarity and best practices.
```

### Dashboard Feedback
```
As the Reviewer, evaluate my Streamlit dashboard for UX and performance.
```

---

## How to Publish

### Demo Script
```python
# demo.py
import streamlit as st
from eda import profile_dataset, generate_visualizations

st.title("EDA Dashboard Demo")
data = load_sample_data()
profile = profile_dataset(data)
st.write(profile)
generate_visualizations(data)
```

### Write-Up Topics
- Importance of EDA before modeling
- Visualization best practices
- Building data apps with Streamlit
- Statistical insights from real data

---

## Resources

- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Plotly Python](https://plotly.com/python/)
- Skill: `.claude/skills/eda-to-insight.md`

---

## Month Evaluation

At month end, run:
```bash
python .claude/path-engine/evaluate.py --month 2
```
