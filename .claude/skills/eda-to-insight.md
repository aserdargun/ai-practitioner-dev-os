# Skill: EDA to Insight

## Trigger

Use this skill when you need to explore a new dataset and extract actionable insights.

## Prerequisites

- Dataset available (CSV, Parquet, database table, API)
- Python environment with pandas, matplotlib/seaborn
- Clear business question or exploration goal

## Steps

### 1. Load and Inspect (15 min)

```python
import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# First look
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(df.head())
print(df.info())
print(df.describe())
```

**Checkpoint**: Can describe dataset size, types, and basic stats.

### 2. Check Data Quality (20 min)

```python
# Missing values
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
print(missing_pct[missing_pct > 0])

# Duplicates
duplicates = df.duplicated().sum()
print(f"Duplicates: {duplicates}")

# Outliers (numeric columns)
for col in df.select_dtypes(include='number').columns:
    q1, q3 = df[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    outliers = ((df[col] < q1 - 1.5*iqr) | (df[col] > q3 + 1.5*iqr)).sum()
    if outliers > 0:
        print(f"{col}: {outliers} outliers")
```

**Checkpoint**: Documented missing values, duplicates, outliers.

### 3. Univariate Analysis (30 min)

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Numeric distributions
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
for i, col in enumerate(df.select_dtypes(include='number').columns[:6]):
    ax = axes[i // 3, i % 3]
    df[col].hist(ax=ax, bins=30)
    ax.set_title(col)
plt.tight_layout()
plt.savefig("univariate_numeric.png")

# Categorical distributions
for col in df.select_dtypes(include='object').columns[:5]:
    print(f"\n{col}:")
    print(df[col].value_counts().head(10))
```

**Checkpoint**: Visualizations for key variables.

### 4. Bivariate Analysis (30 min)

```python
# Correlations (numeric)
corr = df.select_dtypes(include='number').corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.savefig("correlation_matrix.png")

# Target variable relationships (if applicable)
target = 'target_column'  # Replace with actual
for col in df.columns[:5]:
    if col != target:
        if df[col].dtype in ['int64', 'float64']:
            plt.figure()
            plt.scatter(df[col], df[target], alpha=0.5)
            plt.xlabel(col)
            plt.ylabel(target)
            plt.savefig(f"scatter_{col}_vs_target.png")
```

**Checkpoint**: Identified key relationships.

### 5. Generate Insights (30 min)

Document findings in structured format:

```markdown
## EDA Insights: [Dataset Name]

### Dataset Summary
- Size: X rows, Y columns
- Date range: [if applicable]
- Key entities: [what does each row represent]

### Data Quality Issues
1. [Issue 1]: [Impact] → [Recommended action]
2. [Issue 2]: [Impact] → [Recommended action]

### Key Findings
1. **[Finding 1]**: [Description with supporting stat]
2. **[Finding 2]**: [Description with supporting stat]
3. **[Finding 3]**: [Description with supporting stat]

### Recommendations
1. [Actionable recommendation]
2. [Actionable recommendation]

### Next Steps
- [ ] [Follow-up analysis]
- [ ] [Data cleaning task]
- [ ] [Modeling consideration]
```

## Artifacts Produced

- `eda_notebook.ipynb` or `eda.py` - Analysis code
- `eda_insights.md` - Documented findings
- `figures/` - Visualization outputs
- `data_quality_report.md` - Quality issues

## Quality Bar

- [ ] All columns inspected and described
- [ ] Missing value strategy documented
- [ ] At least 3 visualizations created
- [ ] At least 3 insights with supporting data
- [ ] Actionable next steps defined

## Common Pitfalls

1. **Jumping to conclusions** - Correlation ≠ causation
2. **Ignoring data leakage** - Check for future information
3. **Over-plotting** - Too many charts obscure insights
4. **Missing context** - Always tie back to business question

## Example

See `examples/mini-example/` for a worked EDA example.
