# Month 2: Data Fundamentals

**Focus**: Master pandas, NumPy, and SQL for data manipulation

---

## Why It Matters

Data manipulation is the foundation of all data science work. You'll spend 60-80% of your time cleaning and preparing data. Employers expect:
- Fluency with pandas for data wrangling
- Understanding of NumPy for numerical operations
- SQL skills for database queries
- Ability to clean messy real-world data

---

## Prerequisites

- Month 1 completed (Python basics, environment setup)
- Comfortable with Python functions and files
- Git workflow understood

---

## Learning Goals

By the end of this month, you will:

1. **NumPy**
   - [ ] Arrays and array operations
   - [ ] Broadcasting
   - [ ] Basic linear algebra
   - [ ] Random number generation

2. **pandas**
   - [ ] DataFrames and Series
   - [ ] Reading/writing CSV, Excel, JSON
   - [ ] Filtering and selection
   - [ ] Groupby and aggregation
   - [ ] Merging and joining
   - [ ] Handling missing data

3. **SQL**
   - [ ] SELECT, WHERE, ORDER BY
   - [ ] JOIN operations
   - [ ] GROUP BY and aggregations
   - [ ] Subqueries basics

---

## Main Project: Data Cleaning Pipeline

Build a pipeline that cleans a messy dataset and produces analysis-ready output.

### Deliverables

1. **Data pipeline** (`pipeline/`)
   - `load.py` - Load data from multiple sources
   - `clean.py` - Clean and validate data
   - `transform.py` - Feature engineering
   - `main.py` - Orchestrate the pipeline

2. **Cleaned dataset**
   - Output CSV with clean data
   - Data dictionary documenting columns

3. **Quality report**
   - Before/after statistics
   - Missing value handling explanation
   - Validation checks performed

4. **Tests**
   - Test data loading
   - Test cleaning functions
   - Test edge cases

### Definition of Done

- [ ] Pipeline runs end-to-end
- [ ] Handles at least 3 data quality issues
- [ ] Output data is validated
- [ ] Tests pass
- [ ] Documentation complete
- [ ] Code follows style guide

### Data Sources

Choose a messy dataset:
- Kaggle datasets (many have quality issues)
- [Data.gov](https://data.gov)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/)
- Your own data (with permission)

---

## Stretch Goals

- [ ] Add SQL database as input/output
- [ ] Implement data profiling (pandas-profiling)
- [ ] Add data validation with Great Expectations
- [ ] Create a Jupyter notebook walkthrough

---

## Weekly Breakdown

### Week 1: NumPy
- Array creation and manipulation
- Mathematical operations
- Broadcasting concepts
- Practice exercises

### Week 2: pandas Basics
- DataFrames and Series
- Reading/writing data
- Filtering and selection
- Basic operations

### Week 3: pandas Advanced
- Groupby and aggregation
- Merging and joining
- Handling missing data
- String operations

### Week 4: Project & SQL
- Build data pipeline
- SQL fundamentals
- Integration testing
- Documentation

---

## Claude Prompts

### Start of Month
```
/status

I'm starting Month 2: Data Fundamentals. I've completed Month 1 and have
Python basics down. Help me plan this month.
```

### Learning NumPy
```
I'm learning NumPy. Explain [broadcasting/slicing/etc] with examples.
Then give me a practice problem.
```

### pandas Help
```
I'm trying to [describe task] with pandas.
Here's my DataFrame: [describe structure]
What's the best approach?
```

### SQL Practice
```
Help me write a SQL query to:
[describe what you want to extract]

The tables are:
- table1: columns [a, b, c]
- table2: columns [x, y, z]
```

### Project Planning
```
/plan-week

I'm building a data cleaning pipeline for [dataset].
The main issues are: [list problems]
Help me plan this week's tasks.
```

### Code Review
```
Here's my data cleaning code. Please review for:
- pandas best practices
- Performance issues
- Edge cases I might have missed

[paste code]
```

### Using Skills
```
I want to apply the EDA to Insight skill to my dataset.
Walk me through the steps from .claude/skills/eda-to-insight.md
```

---

## How to Publish

### Demo

Show your pipeline in action:
1. Original messy data (screenshot)
2. Pipeline running
3. Clean output data
4. Quality metrics

### Write-up

Cover:
- What data quality issues you found
- How you solved each one
- Before/after comparisons
- Lessons learned

### Portfolio

- GitHub repo with clear README
- Include sample data (if shareable)
- Document your process

---

## Resources

### NumPy
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
- [100 NumPy Exercises](https://github.com/rougier/numpy-100)

### pandas
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [pandas Exercises](https://github.com/guipsamora/pandas_exercises)

### SQL
- [SQLBolt](https://sqlbolt.com/)
- [Mode SQL Tutorial](https://mode.com/sql-tutorial/)

---

## Next Month

[Month 3: Statistics & Probability](../month-03/README.md) - Statistical foundations for ML
