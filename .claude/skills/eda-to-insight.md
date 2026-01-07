# Skill: EDA to Insight

**Tier**: 1 (Beginner)

Transform raw data into actionable insights through systematic exploratory data analysis.

---

## Trigger

Use this skill when:
- Starting a new data project
- Receiving a new dataset
- Need to understand data before modeling

## Prerequisites

- [ ] Dataset available (CSV, parquet, database)
- [ ] Python environment with pandas, matplotlib, seaborn
- [ ] Jupyter notebook or Python script

## Steps

### Step 1: Load and Inspect (10 min)

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data.csv')

# Basic inspection
print(f"Shape: {df.shape}")
print(f"\nColumn types:\n{df.dtypes}")
print(f"\nFirst rows:\n{df.head()}")
print(f"\nBasic stats:\n{df.describe()}")
```

**Checkpoint**: Can describe dataset size, columns, and types.

### Step 2: Check Data Quality (15 min)

```python
# Missing values
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
print(f"Missing values:\n{missing[missing > 0]}")

# Duplicates
dupes = df.duplicated().sum()
print(f"\nDuplicate rows: {dupes}")

# Unique values per column
for col in df.select_dtypes(include='object').columns:
    print(f"\n{col}: {df[col].nunique()} unique values")
```

**Checkpoint**: Know missing %, duplicates, cardinality.

### Step 3: Univariate Analysis (20 min)

```python
# Numeric distributions
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in numeric_cols:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    df[col].hist(ax=axes[0], bins=30)
    axes[0].set_title(f'{col} - Histogram')
    df.boxplot(column=col, ax=axes[1])
    axes[1].set_title(f'{col} - Boxplot')
    plt.tight_layout()
    plt.show()

# Categorical distributions
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    if df[col].nunique() < 20:
        df[col].value_counts().plot(kind='bar')
        plt.title(f'{col} Distribution')
        plt.xticks(rotation=45)
        plt.show()
```

**Checkpoint**: Understand distribution of each variable.

### Step 4: Bivariate Analysis (20 min)

```python
# Correlation matrix for numerics
corr = df[numeric_cols].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.show()

# Scatter plots for key relationships
# (customize based on your target variable)
if 'target' in df.columns:
    for col in numeric_cols:
        if col != 'target':
            plt.scatter(df[col], df['target'], alpha=0.5)
            plt.xlabel(col)
            plt.ylabel('target')
            plt.show()
```

**Checkpoint**: Identify key correlations and relationships.

### Step 5: Document Insights (15 min)

Create a summary with:

```markdown
## EDA Summary: [Dataset Name]

### Dataset Overview
- Records: X
- Features: Y (Z numeric, W categorical)
- Date range: [if applicable]

### Data Quality
- Missing values: [summary]
- Duplicates: X rows
- Issues found: [list]

### Key Distributions
- [Variable 1]: [description - normal, skewed, etc.]
- [Variable 2]: [description]

### Key Relationships
- [Strong correlation between X and Y]
- [Category Z has higher values for target]

### Recommended Next Steps
1. [Handle missing values by...]
2. [Create feature X because...]
3. [Remove outliers in Y because...]

### Questions for Stakeholders
- [Any unclear aspects]
```

**Checkpoint**: Have written summary with actionable insights.

## Artifacts Produced

- [ ] Jupyter notebook with all analysis
- [ ] EDA summary document (markdown)
- [ ] Key visualizations saved as images
- [ ] List of data quality issues

## Quality Bar

✅ **Done when**:
- All columns inspected
- Missing values quantified
- Distributions visualized
- Correlations computed
- Summary document written
- Next steps defined

## Common Pitfalls

- **Skipping quality checks**: Always check for missing values and duplicates first
- **Too many plots**: Focus on informative visualizations
- **No documentation**: Write insights as you go, not at the end
- **Ignoring outliers**: Note them even if you don't remove them yet

## Example Prompt

```
I have a new dataset for predicting customer churn. Help me run through the EDA skill:

1. Load the data from 'churn_data.csv'
2. Walk me through each step
3. Help me document the key insights
```

## Related Skills

- [Baseline Model and Card](baseline-model-and-card.md) - Next step after EDA
- [Experiment Plan](experiment-plan.md) - Plan experiments based on EDA insights
