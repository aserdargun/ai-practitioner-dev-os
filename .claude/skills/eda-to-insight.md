# Skill: EDA to Insight

Exploratory Data Analysis workflow that produces actionable insights.

## Trigger

Use this skill when:
- Starting a new data project
- Receiving a new dataset
- Trying to understand data patterns
- Preparing data for modeling

## Prerequisites

- Dataset loaded (CSV, database, API)
- Python environment with pandas, matplotlib/seaborn
- Jupyter notebook or similar environment
- Business context (what questions are we answering?)

## Steps

### 1. First Look (10 min)
```python
# Shape and types
df.shape
df.dtypes
df.head()
df.info()
```

Document:
- Number of rows and columns
- Column types (numeric, categorical, datetime)
- Any obvious issues visible

### 2. Missing Data Analysis (15 min)
```python
# Missing values
df.isnull().sum()
df.isnull().sum() / len(df) * 100  # Percentage

# Visualize missingness
import seaborn as sns
sns.heatmap(df.isnull(), cbar=True, yticklabels=False)
```

Document:
- Columns with missing data
- Patterns in missingness
- Strategy for handling (drop, impute, flag)

### 3. Univariate Analysis (20 min)

For numeric columns:
```python
df.describe()

# Distributions
for col in numeric_cols:
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    df[col].hist(bins=30)
    plt.subplot(1, 2, 2)
    df[col].plot(kind='box')
    plt.title(col)
    plt.show()
```

For categorical columns:
```python
for col in categorical_cols:
    print(df[col].value_counts())
    df[col].value_counts().plot(kind='bar')
    plt.title(col)
    plt.show()
```

Document:
- Distributions (normal, skewed, bimodal)
- Outliers
- Unexpected values

### 4. Bivariate Analysis (20 min)
```python
# Correlations (numeric)
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')

# Scatter plots for key relationships
sns.pairplot(df[key_cols])

# Categorical vs numeric
for cat in categorical_cols:
    for num in numeric_cols[:3]:
        df.boxplot(column=num, by=cat)
        plt.show()
```

Document:
- Strong correlations
- Surprising relationships
- Potential feature interactions

### 5. Time Patterns (if applicable, 15 min)
```python
# Parse datetime
df['date'] = pd.to_datetime(df['date_col'])
df.set_index('date', inplace=True)

# Time series plot
df[target].plot()

# Seasonal patterns
df.groupby(df.index.month)[target].mean().plot(kind='bar')
df.groupby(df.index.dayofweek)[target].mean().plot(kind='bar')
```

Document:
- Trends (up, down, stable)
- Seasonality (weekly, monthly, yearly)
- Anomalies

### 6. Synthesize Insights (15 min)

Write 3-5 key insights in plain language:
- What did we learn about the data?
- What are the data quality issues?
- What features look promising for modeling?
- What questions remain?

## Artifacts Produced

- [ ] `eda_notebook.ipynb` — Documented EDA notebook
- [ ] `eda_summary.md` — Key insights summary (1 page)
- [ ] `data_quality_report.md` — Issues and recommendations
- [ ] Saved visualizations (PNG/PDF)

## Quality Bar

- [ ] All columns examined
- [ ] Missing data documented with strategy
- [ ] Distributions visualized and described
- [ ] Key relationships identified
- [ ] Insights are actionable, not just descriptive
- [ ] Notebook runs end-to-end without errors

## Common Pitfalls

1. **Jumping to modeling too fast**
   - Spend at least 1 hour on EDA for any non-trivial dataset

2. **Not documenting findings**
   - Write insights as you go, not just code

3. **Ignoring data quality**
   - Flag issues early, don't assume clean data

4. **Looking at everything equally**
   - Focus on columns relevant to your question

5. **Forgetting business context**
   - Always tie insights back to the problem

## Example

```markdown
# EDA Summary: Sales Data

## Dataset Overview
- 50,000 transactions over 2 years
- 12 features including date, product, store, amount

## Key Insights
1. Sales have 30% weekly seasonality (Sat-Sun peak)
2. Product category A drives 60% of revenue
3. 15% of stores account for 50% of sales
4. Missing data in 'promo_code' (23%) — likely means no promo

## Data Quality Issues
- Duplicate transactions: 0.5%
- Future dates: 12 records (data entry error)
- Negative amounts: 45 records (returns?)

## Recommendations
1. Focus modeling on weekday/weekend split
2. Create store tier feature
3. Investigate negative amounts before modeling
```
