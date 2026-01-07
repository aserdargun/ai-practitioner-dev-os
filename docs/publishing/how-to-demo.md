# How to Demo Your Work

This guide helps you create effective demos of your projects.

## Why Demo?

Demos are important because they:
- Prove your work actually functions
- Practice explaining technical concepts
- Build your portfolio
- Get feedback from others

## Demo Checklist

Before demoing, ensure:

- [ ] Code runs without errors
- [ ] Sample data is available
- [ ] Environment is set up
- [ ] You've rehearsed the flow
- [ ] Backup plan if something fails

## Demo Structure

### 1. Introduction (1 minute)

- What problem does this solve?
- Who would use this?
- What's the key insight?

**Example**:
> "This is a customer churn prediction model. It helps subscription businesses identify customers likely to cancel, so they can intervene early. The key insight is that usage patterns in the last 30 days are highly predictive."

### 2. Show the End Result (2 minutes)

Start with the output, not the code.

- Show the final product working
- Use realistic data
- Highlight key features

**Example**:
> "Here's the prediction dashboard. You can see customer X has a 78% churn probability. The model highlights usage drop and support tickets as key factors."

### 3. Walk Through the Process (3-5 minutes)

Show how you got there:

- Data exploration highlights
- Key decisions you made
- Challenges you solved

**Example**:
> "The data had 20% missing values in the usage column. I tried three imputation strategies and found forward-fill worked best for this time-series data."

### 4. Show the Code (2-3 minutes)

Pick 1-2 interesting code sections:

- Don't show everything
- Focus on clever solutions
- Explain your reasoning

**Example**:
> "Here's the feature engineering. I created a 'usage_trend' feature that captures the 7-day rolling average compared to the 30-day baseline. This single feature improved accuracy by 5%."

### 5. Results and Metrics (1-2 minutes)

Share what you measured:

- Key metrics (accuracy, F1, etc.)
- Comparison to baseline
- Business impact

**Example**:
> "The model achieves 0.82 F1 score, up from 0.65 with the baseline. In business terms, this could identify 200 more at-risk customers per month."

### 6. Lessons Learned (1 minute)

What would you do differently?

- Honest reflection
- Future improvements
- What you learned

**Example**:
> "If I did this again, I'd spend more time on feature engineering earlier. The model architecture mattered less than the features."

### 7. Q&A

Be ready for questions about:
- Technical decisions
- Alternative approaches
- Limitations
- Next steps

## Demo Tips

### Technical Setup

```bash
# Before demo, verify everything works
python -m pytest tests/ -v
python run_demo.py  # Your demo script

# Have a backup
cp demo_output.png demo_output_backup.png
```

### During Demo

**Do**:
- Speak slowly and clearly
- Pause after key points
- Make eye contact (if live)
- Admit what you don't know

**Don't**:
- Read from slides
- Show every line of code
- Rush through errors
- Make excuses

### If Something Breaks

1. Stay calm
2. Acknowledge the issue
3. Show backup output if available
4. Explain what should have happened
5. Continue with the demo

## Demo Formats

### Live Demo

Best for: Interactive features, real-time predictions

```python
# demo.py - Live demo script
def run_demo():
    print("Loading model...")
    model = load_model("model.joblib")

    print("\nMaking predictions...")
    sample = get_sample_data()
    prediction = model.predict(sample)

    print(f"\nPrediction: {prediction}")
    print("Demo complete!")
```

### Recorded Demo

Best for: Complex workflows, async sharing

Tools:
- Screen recording (OBS, Loom)
- Jupyter notebook walkthrough
- Terminal recording (asciinema)

### Notebook Demo

Best for: Data exploration, step-by-step analysis

```python
# Demo notebook structure
# 1. Setup and imports
# 2. Load sample data
# 3. Show key analysis
# 4. Run model
# 5. Visualize results
```

## Recording Tips

If recording your demo:

1. **Preparation**
   - Clean desktop
   - Close notifications
   - Prepare script/outline
   - Test audio/video

2. **Recording**
   - Record in sections (easier to edit)
   - Speak clearly
   - Pause between sections
   - Keep it under 10 minutes

3. **Post-production**
   - Trim dead air
   - Add captions if possible
   - Include intro/outro
   - Add background music (optional)

## Example Demo Script

```markdown
# Churn Prediction Demo Script

## Setup (before recording)
- [ ] Activate environment
- [ ] Load model
- [ ] Open dashboard
- [ ] Prepare sample data

## Demo Flow

### [0:00] Introduction
"Hi, I'm going to show you a customer churn prediction model..."

### [1:00] End Result
- Open dashboard
- Show prediction for sample customer
- Highlight key risk factors

### [3:00] Data Exploration
- Show notebook
- Highlight missing value analysis
- Show key visualizations

### [6:00] Code Walkthrough
- Feature engineering function
- Model training snippet

### [8:00] Results
- Show metrics comparison
- Business impact estimate

### [9:00] Lessons Learned
- Feature engineering key insight
- What I'd do differently

### [10:00] Wrap Up
"Thanks for watching. Code is available at..."
```

## After the Demo

1. Share materials (code, slides, recording)
2. Collect feedback
3. Log learnings to best practices
4. Update portfolio

## Related Documentation

- [How to Write Medium Post](how-to-write-medium-post.md)
- [Portfolio Checklist](portfolio-checklist.md)
