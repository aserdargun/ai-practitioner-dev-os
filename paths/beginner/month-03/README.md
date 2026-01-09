# Month 3: Statistics & Probability

**Theme**: Build statistical foundations for data analysis and machine learning.

## Why It Matters

Statistics is the language of data. Understanding probability, distributions, and statistical testing lets you make valid conclusions from data. ML is essentially applied statistics—this foundation is non-negotiable.

## Prerequisites

- Month 2 completed (pandas proficiency)
- Basic math comfort (algebra level)

## Learning Goals

### Descriptive Statistics (Week 1)
- [ ] Mean, median, mode
- [ ] Variance and standard deviation
- [ ] Percentiles and quartiles
- [ ] Correlation and covariance
- [ ] Summarizing data distributions

### Probability (Week 2)
- [ ] Basic probability concepts
- [ ] Conditional probability
- [ ] Bayes' theorem
- [ ] Common distributions (normal, binomial, Poisson)
- [ ] Central Limit Theorem

### Inferential Statistics (Week 3-4)
- [ ] Sampling and populations
- [ ] Confidence intervals
- [ ] Hypothesis testing
- [ ] t-tests and chi-square tests
- [ ] p-values and significance
- [ ] Common statistical pitfalls

## Main Project: A/B Test Analyzer

Build a tool that analyzes A/B test results and determines statistical significance.

### Deliverables
1. A/B test analyzer script:
   - Load experiment data
   - Calculate conversion rates
   - Compute confidence intervals
   - Run statistical tests
   - Determine significance
   - Generate report

2. Analysis notebook demonstrating:
   - Sample size calculations
   - Power analysis basics
   - Multiple comparison correction

### Definition of Done
- [ ] Correctly calculates conversion rates
- [ ] Confidence intervals are accurate
- [ ] Statistical test results match scipy
- [ ] Clear interpretation of results
- [ ] Handles edge cases (small samples)
- [ ] Documentation explains methodology

## Stretch Goals

- [ ] Add power analysis
- [ ] Support multiple metrics
- [ ] Create visualization of results
- [ ] Add sequential testing option
- [ ] Generate executive summary

## Weekly Breakdown

### Week 1: Descriptive Stats
- Measures of central tendency
- Spread and variability
- Using numpy and scipy.stats
- Summarize a real dataset

### Week 2: Probability
- Probability fundamentals
- Distributions in scipy
- Simulation exercises
- Bayes theorem application

### Week 3: Hypothesis Testing
- Testing fundamentals
- t-tests in practice
- p-values and interpretation
- Start A/B test project

### Week 4: Complete Project
- Finish analyzer
- Test with real data
- Documentation
- Demo prep

## Claude Prompts

### Planning
```
/plan-week
Month 3 Week 2 - Focus on probability
I want to understand distributions practically
```

### Concept Help
```
Ask the Researcher to explain the Central Limit
Theorem with practical examples I can code.
```

### Building
```
Ask the Builder to help me implement a function
that calculates the confidence interval for a
proportion (like conversion rate).
```

### Review
```
Ask the Reviewer to check my statistical test
implementation. Is it correct? Any edge cases I'm missing?
```

## How to Publish

### Demo
1. Show sample A/B test data
2. Run the analyzer
3. Explain the statistical output
4. Show what "significant" means
5. Demonstrate edge case handling

### Write-up Topics
- Why statistical significance matters
- Common mistakes in A/B testing
- How to interpret results correctly
- What I learned about statistics

### Portfolio Entry
- Clear explanation of methodology
- Sample analysis with interpretation
- Code that others can use

## Resources

### Statistics
- [StatQuest YouTube](https://www.youtube.com/c/joshstarmer) — Best video explanations
- [Khan Academy Statistics](https://www.khanacademy.org/math/statistics-probability)
- [Seeing Theory](https://seeing-theory.brown.edu/) — Visual probability

### Python
- [scipy.stats Documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [statsmodels](https://www.statsmodels.org/stable/index.html)

### A/B Testing
- [Evan Miller's A/B Tools](https://www.evanmiller.org/ab-testing/)
- [Optimizely Stats Engine](https://www.optimizely.com/optimization-glossary/stats-engine/)

## Tips

1. **Build intuition** — Simulate to understand distributions
2. **Don't memorize formulas** — Understand when to use what
3. **Be skeptical** — Question significant results too
4. **Sample size matters** — Small samples = unreliable results
5. **Visualize** — Always plot your data before testing
