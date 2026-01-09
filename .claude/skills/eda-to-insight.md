# Skill: EDA to Insight

Transform raw data into actionable insights through structured exploratory data analysis.

## Trigger

Use this skill when:
- Starting a new project with unfamiliar data
- Preparing data for modeling
- Investigating data quality issues
- Looking for patterns and anomalies

## Prerequisites

- [ ] Data loaded into pandas DataFrame (or equivalent)
- [ ] Basic understanding of the data domain
- [ ] Jupyter notebook or Python environment ready

## Steps

### 1. Initial Assessment (15 min)

```python
# Shape and types
df.shape
df.dtypes
df.info()

# First look
df.head()
df.sample(5)
```

**Document**: Data source, size, column meanings.

### 2. Missing Values (10 min)

```python
# Missing value analysis
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
missing_report = pd.DataFrame({
    'missing': missing,
    'percent': missing_pct
}).sort_values('percent', ascending=False)
```

**Document**: Which columns have missing values, likely reasons, handling strategy.

### 3. Univariate Analysis (30 min)

**Numeric columns**:
```python
df.describe()
# For each numeric column:
# - Histogram
# - Box plot
# - Check for outliers
```

**Categorical columns**:
```python
df['column'].value_counts()
# - Bar chart
# - Cardinality check
```

**Document**: Distribution shapes, outliers, unexpected values.

### 4. Bivariate Analysis (30 min)

```python
# Correlation matrix (numeric)
corr = df.corr()
sns.heatmap(corr, annot=True)

# Target relationships
# For classification: group by target, compare distributions
# For regression: scatter plots with target
```

**Document**: Key relationships, surprising correlations, potential features.

### 5. Data Quality Checks (15 min)

- [ ] Duplicate rows?
- [ ] Inconsistent formats?
- [ ] Invalid values?
- [ ] Data type mismatches?
- [ ] Temporal consistency (if applicable)?

**Document**: Issues found and recommended fixes.

### 6. Synthesize Insights (15 min)

Write a summary covering:
1. **Key findings**: 3-5 most important observations
2. **Data quality**: Issues and mitigation plan
3. **Feature ideas**: Promising transformations or combinations
4. **Questions raised**: What needs further investigation
5. **Modeling implications**: How findings affect approach

## Artifacts

| Artifact | Description |
|----------|-------------|
| `eda_notebook.ipynb` | Jupyter notebook with all analysis |
| `data_profile.md` | Summary document of findings |
| `quality_report.md` | Data quality issues and fixes |

## Quality Bar

- [ ] All columns explored (not just a subset)
- [ ] Visualizations are clear and labeled
- [ ] Findings are documented, not just code output
- [ ] Quality issues are cataloged with severity
- [ ] Insights are actionable, not just descriptive
- [ ] Notebook runs end-to-end without errors

## Time Estimate

| Experience | Time |
|------------|------|
| First time | 3-4 hours |
| Practiced | 1.5-2 hours |
| Expert | 45-60 min |

## Common Pitfalls

- Skipping documentation ("I'll remember this")
- Not checking data types early
- Ignoring missing value patterns
- Over-relying on automated profiling tools
- Not connecting findings to business context

## Tools

- **pandas-profiling**: Automated EDA reports
- **sweetviz**: Compare datasets
- **dtale**: Interactive exploration
- **matplotlib/seaborn**: Custom visualizations
