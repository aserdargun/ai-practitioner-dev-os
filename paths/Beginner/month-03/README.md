# Month 3: Statistics & Probability

**Focus**: Build statistical foundations essential for machine learning

---

## Why It Matters

Statistics is the language of data science. Understanding probability and statistical inference helps you:
- Interpret model results correctly
- Design valid experiments
- Avoid common analytical mistakes
- Communicate findings with confidence

Employers expect data scientists to understand statistical significance, distributions, and hypothesis testing.

---

## Prerequisites

- Month 1 & 2 completed
- Comfortable with pandas and NumPy
- Basic math comfort (algebra level)

---

## Learning Goals

By the end of this month, you will:

1. **Descriptive Statistics**
   - [ ] Measures of central tendency (mean, median, mode)
   - [ ] Measures of spread (variance, std dev, IQR)
   - [ ] Percentiles and quartiles
   - [ ] Correlation and covariance

2. **Probability**
   - [ ] Basic probability rules
   - [ ] Conditional probability
   - [ ] Bayes' theorem
   - [ ] Common distributions (normal, binomial, Poisson)

3. **Statistical Inference**
   - [ ] Sampling and sampling distributions
   - [ ] Confidence intervals
   - [ ] Hypothesis testing
   - [ ] p-values and significance

4. **Experimental Design**
   - [ ] A/B testing fundamentals
   - [ ] Sample size calculation
   - [ ] Common pitfalls

---

## Main Project: A/B Test Analysis

Analyze an A/B test dataset and make a recommendation.

### Deliverables

1. **Analysis notebook** (`ab_test_analysis.ipynb`)
   - Exploratory data analysis
   - Statistical test selection
   - Results interpretation
   - Visualization of findings

2. **Executive summary** (`summary.md`)
   - Non-technical explanation
   - Clear recommendation
   - Confidence levels stated

3. **Statistical report** (`statistical_report.md`)
   - Methodology explained
   - Assumptions checked
   - Detailed results
   - Limitations acknowledged

### Definition of Done

- [ ] Correct statistical test used
- [ ] Assumptions validated
- [ ] Results interpreted correctly
- [ ] Confidence intervals included
- [ ] Recommendation is justified
- [ ] Both technical and non-technical docs complete

### Dataset Options

- [Kaggle A/B Testing Dataset](https://www.kaggle.com/datasets)
- Simulated e-commerce data
- Marketing campaign data
- Product feature experiment

---

## Stretch Goals

- [ ] Implement Bayesian A/B testing
- [ ] Add power analysis
- [ ] Create interactive dashboard
- [ ] Analyze multiple metrics

---

## Weekly Breakdown

### Week 1: Descriptive Statistics
- Summary statistics
- Distributions and shapes
- Correlation analysis
- Practice with real data

### Week 2: Probability
- Probability basics
- Conditional probability
- Bayes' theorem
- Common distributions

### Week 3: Statistical Inference
- Sampling theory
- Confidence intervals
- Hypothesis testing
- t-tests and chi-square

### Week 4: A/B Testing Project
- Design analysis plan
- Perform statistical tests
- Interpret results
- Write reports

---

## Claude Prompts

### Start of Month
```
/status

I'm starting Month 3: Statistics & Probability.
Help me understand the key concepts I need to master this month.
```

### Learning Concepts
```
Explain [statistical concept] in simple terms.
- What is it?
- When do I use it?
- Show me an example with Python code.
```

### Distribution Questions
```
I have data that looks like [description].
What distribution might this be?
How do I test my assumption?
```

### Hypothesis Testing
```
I want to test if [hypothesis].
- What test should I use?
- What are the assumptions?
- Walk me through the steps.
```

### A/B Test Planning
```
/plan-week

I'm analyzing an A/B test with:
- Control group: [n] users
- Treatment group: [m] users
- Primary metric: [metric]

Help me plan my analysis.
```

### Results Interpretation
```
My statistical test gave:
- t-statistic: [value]
- p-value: [value]
- Confidence interval: [range]

Help me interpret these results and write a recommendation.
```

---

## How to Publish

### Demo

Present your A/B test analysis:
1. The business question
2. Data exploration (key charts)
3. Statistical approach
4. Results and recommendation

### Write-up

Create a blog post covering:
- A/B testing explained simply
- Your analysis approach
- What you found
- Lessons for practitioners

### Portfolio

- Jupyter notebook on GitHub
- Clear visualizations
- Both technical and business summaries

---

## Resources

### Statistics
- [Statistics 110: Probability (Harvard)](https://projects.iq.harvard.edu/stat110)
- [Think Stats](https://greenteapress.com/thinkstats/)
- [Seeing Theory (Visual)](https://seeing-theory.brown.edu/)

### A/B Testing
- [Trustworthy Online Controlled Experiments](https://www.amazon.com/Trustworthy-Online-Controlled-Experiments-Practical/dp/1108724264)
- [Evan Miller's A/B Tools](https://www.evanmiller.org/ab-testing/)

### Python
- [scipy.stats Documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [statsmodels](https://www.statsmodels.org/)

---

## Next Month

[Month 4: Data Visualization](../month-04/README.md) - Tell stories with data
