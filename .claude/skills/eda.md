# Skill: EDA to Insight

Exploratory Data Analysis workflow for turning raw data into actionable insights.

---

## When to Use

- Starting a new data project
- Investigating data quality issues
- Preparing data for modeling
- Creating data documentation

---

## Prerequisites

```python
# Required packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Optional but recommended
from ydata_profiling import ProfileReport  # For automated profiling
```

---

## The EDA Playbook

### Phase 1: First Look (10 minutes)

```python
# Load and inspect
df = pd.read_csv("data.csv")

# Basic info
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
df.info()
df.head()
```

**Questions to answer:**
- How many rows and columns?
- What are the data types?
- Are there obvious issues visible in head()?

### Phase 2: Missing Data Analysis (15 minutes)

```python
# Missing value summary
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_df = pd.DataFrame({
    'missing_count': missing,
    'missing_pct': missing_pct
}).sort_values('missing_pct', ascending=False)

print(missing_df[missing_df['missing_count'] > 0])

# Visualize missing patterns
import missingno as msno
msno.matrix(df)
plt.show()
```

**Questions to answer:**
- Which columns have missing data?
- Is missingness random or systematic?
- What's the strategy for each column?

### Phase 3: Univariate Analysis (20 minutes)

```python
# Numerical columns
numerical_cols = df.select_dtypes(include=[np.number]).columns

for col in numerical_cols:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # Distribution
    df[col].hist(ax=axes[0], bins=30)
    axes[0].set_title(f'{col} Distribution')

    # Box plot
    df.boxplot(column=col, ax=axes[1])
    axes[1].set_title(f'{col} Box Plot')

    plt.tight_layout()
    plt.show()

    # Summary stats
    print(df[col].describe())
    print(f"Skewness: {df[col].skew():.2f}")
    print("-" * 40)
```

```python
# Categorical columns
categorical_cols = df.select_dtypes(include=['object', 'category']).columns

for col in categorical_cols:
    print(f"\n{col}:")
    print(df[col].value_counts())

    # Bar plot for top categories
    df[col].value_counts().head(10).plot(kind='bar')
    plt.title(f'{col} Value Counts')
    plt.show()
```

**Questions to answer:**
- What's the distribution shape?
- Are there outliers?
- What are the most common categories?

### Phase 4: Bivariate Analysis (20 minutes)

```python
# Correlation matrix for numerical features
corr_matrix = df[numerical_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.show()

# High correlations
high_corr = []
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        if abs(corr_matrix.iloc[i, j]) > 0.7:
            high_corr.append({
                'var1': corr_matrix.columns[i],
                'var2': corr_matrix.columns[j],
                'corr': corr_matrix.iloc[i, j]
            })

print("High correlations (|r| > 0.7):")
for item in high_corr:
    print(f"  {item['var1']} <-> {item['var2']}: {item['corr']:.2f}")
```

```python
# Target variable analysis (if applicable)
target = 'target_column'  # Replace with actual target

for col in numerical_cols:
    if col != target:
        plt.figure(figsize=(8, 5))
        plt.scatter(df[col], df[target], alpha=0.5)
        plt.xlabel(col)
        plt.ylabel(target)
        plt.title(f'{col} vs {target}')
        plt.show()
```

### Phase 5: Document Findings (15 minutes)

Create a summary document:

```markdown
# EDA Summary: [Dataset Name]

## Dataset Overview
- **Rows**: X
- **Columns**: Y
- **Date Range**: [if applicable]

## Data Quality Issues
1. Missing values in columns: [list]
2. Outliers detected in: [list]
3. Data type issues: [list]

## Key Findings
1. [Finding 1 with evidence]
2. [Finding 2 with evidence]
3. [Finding 3 with evidence]

## Recommendations
1. [Action item 1]
2. [Action item 2]

## Next Steps
- [ ] Address missing values
- [ ] Handle outliers
- [ ] Feature engineering ideas
```

---

## Automated Profiling (Alternative)

For quick automated EDA:

```python
from ydata_profiling import ProfileReport

profile = ProfileReport(df, title="Data Profiling Report")
profile.to_file("eda_report.html")
```

---

## Checklist

- [ ] Data loaded successfully
- [ ] Basic shape and types documented
- [ ] Missing values analyzed
- [ ] Distributions visualized
- [ ] Outliers identified
- [ ] Correlations explored
- [ ] Target relationships examined
- [ ] Findings documented
- [ ] Next steps defined

---

## Common Pitfalls

1. **Skipping documentation**: Always write down findings
2. **Ignoring data types**: Check and fix before analysis
3. **Assuming clean data**: Always verify quality
4. **Over-plotting**: Focus on actionable visualizations
5. **Missing context**: Understand what the data represents
