# Month 2: Data Manipulation with Pandas

**Theme**: Master data manipulation using pandas, the essential data science library.

## Why It Matters

Pandas is the backbone of data work in Python. Data scientists spend 60-80% of their time cleaning and transforming data. Mastering pandas makes everything else easier and is expected in any data role.

## Prerequisites

- Month 1 completed (Python basics, environment setup)
- Comfortable with Python data structures

## Learning Goals

### Pandas Fundamentals (Week 1-2)
- [ ] DataFrames and Series
- [ ] Reading/writing CSV, Excel, JSON
- [ ] Selecting and filtering data
- [ ] Handling missing values
- [ ] Data types and conversions

### Data Transformation (Week 3-4)
- [ ] Sorting and ranking
- [ ] Groupby and aggregation
- [ ] Merging and joining DataFrames
- [ ] Reshaping data (pivot, melt)
- [ ] String operations
- [ ] Date/time operations

## Main Project: Sales Data Analyzer

Build a Python script that analyzes retail sales data.

### Dataset
Use a public retail dataset (e.g., from Kaggle) or create synthetic data with:
- Order ID, Date, Product, Category, Amount, Customer ID, Region

### Deliverables
1. Data cleaning script:
   - Load raw data
   - Handle missing values
   - Fix data types
   - Remove duplicates
   - Output clean dataset

2. Analysis script that answers:
   - Total sales by month
   - Top 10 products by revenue
   - Sales by region
   - Customer purchase frequency
   - Category performance comparison

3. Summary report (markdown or text output)

### Definition of Done
- [ ] Scripts run without errors
- [ ] Raw → Clean data pipeline works
- [ ] 5 analysis questions answered
- [ ] Results exportable to CSV
- [ ] README documents usage
- [ ] Code on GitHub

## Stretch Goals

- [ ] Add data validation checks
- [ ] Create reusable functions for common operations
- [ ] Handle edge cases (empty data, all nulls)
- [ ] Performance optimization for large files
- [ ] Add command-line arguments

## Weekly Breakdown

### Week 1: Pandas Basics
- DataFrames and Series
- Reading data
- Basic selection and filtering
- Start with sample data

### Week 2: Data Cleaning
- Missing values
- Data types
- Duplicates
- Build cleaning pipeline

### Week 3: Transformation
- Groupby and aggregation
- Merging data
- Answer analysis questions

### Week 4: Polish & Ship
- Create summary report
- Documentation
- Error handling
- Demo prep

## Claude Prompts

### Planning
```
/plan-week
Month 2 Week 2 - Focus on data cleaning
I have [X] hours, working with the sales dataset
```

### Getting Help
```
Ask the Builder to help me create a function that
calculates rolling 7-day sales averages by region.
Show me pandas best practices.
```

### EDA Guidance
```
Guide me through the EDA to Insight skill
for my sales dataset. What should I look for?
```

### Code Review
```
Ask the Reviewer to review my data cleaning pipeline.
Check for pandas best practices and potential issues.
```

## How to Publish

### Demo
1. Show raw data (with issues)
2. Run cleaning pipeline
3. Show clean data
4. Run analysis
5. Show summary results

### Write-up Topics
- Data quality issues found
- Cleaning decisions made
- Interesting insights discovered
- pandas techniques learned

### Portfolio Entry
- GitHub with clean code
- Sample data (or instructions to get it)
- Jupyter notebook with analysis

## Resources

### Pandas
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Exercises](https://github.com/guipsamora/pandas_exercises)

### Data Cleaning
- [Kaggle Data Cleaning Course](https://www.kaggle.com/learn/data-cleaning)

### Datasets
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php)

## Tips

1. **Use method chaining** — Makes code readable: `df.dropna().sort_values().head()`
2. **Check dtypes early** — Many bugs come from wrong types
3. **Document your cleaning** — Future you will thank you
4. **Vectorize operations** — Avoid loops, use pandas built-ins
5. **Practice on real data** — Messy data teaches more than clean data
