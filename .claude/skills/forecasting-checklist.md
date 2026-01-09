# Skill: Forecasting Checklist

## Trigger

Use this skill when building time series forecasting models.

## Prerequisites

- Time series data with datetime index
- Clear forecast horizon defined
- Understanding of business seasonality
- Python environment with statsmodels, pandas

**Level**: Intermediate+ (Tier 2)

## Steps

### 1. Data Preparation (30 min)

```python
import pandas as pd
import numpy as np

# Load data with datetime parsing
df = pd.read_csv("timeseries.csv", parse_dates=['date'])
df = df.set_index('date').sort_index()

# Check frequency
print(f"Date range: {df.index.min()} to {df.index.max()}")
print(f"Inferred frequency: {pd.infer_freq(df.index)}")

# Handle missing dates
df = df.asfreq('D')  # or 'H', 'W', 'M'
print(f"Missing values after reindex: {df.isnull().sum()}")

# Fill or interpolate
df = df.interpolate(method='time')
```

**Checkpoint**: Clean time series with consistent frequency.

### 2. Exploratory Analysis (30 min)

```python
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Plot the series
fig, axes = plt.subplots(4, 1, figsize=(12, 10))

# Original
df['value'].plot(ax=axes[0], title='Original Series')

# Decomposition
decomposition = seasonal_decompose(df['value'], model='additive', period=7)  # Adjust period
decomposition.trend.plot(ax=axes[1], title='Trend')
decomposition.seasonal.plot(ax=axes[2], title='Seasonal')
decomposition.resid.plot(ax=axes[3], title='Residual')

plt.tight_layout()
plt.savefig('decomposition.png')
```

**Checkpoint**: Understood trend, seasonality, residual patterns.

### 3. Stationarity Check (15 min)

```python
from statsmodels.tsa.stattools import adfuller

def check_stationarity(series, name='Series'):
    result = adfuller(series.dropna())
    print(f"{name}:")
    print(f"  ADF Statistic: {result[0]:.4f}")
    print(f"  p-value: {result[1]:.4f}")
    print(f"  Stationary: {'Yes' if result[1] < 0.05 else 'No'}")
    return result[1] < 0.05

is_stationary = check_stationarity(df['value'], 'Original')

if not is_stationary:
    # Try differencing
    df['diff'] = df['value'].diff()
    check_stationarity(df['diff'].dropna(), 'Differenced')
```

### 4. Train/Test Split (10 min)

```python
# Time series split - NO shuffle!
train_size = int(len(df) * 0.8)
train = df.iloc[:train_size]
test = df.iloc[train_size:]

print(f"Train: {train.index.min()} to {train.index.max()} ({len(train)} points)")
print(f"Test: {test.index.min()} to {test.index.max()} ({len(test)} points)")

# Visualize split
plt.figure(figsize=(12, 4))
train['value'].plot(label='Train')
test['value'].plot(label='Test')
plt.legend()
plt.savefig('train_test_split.png')
```

### 5. Baseline Models (30 min)

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Naive baseline: last value
naive_pred = np.full(len(test), train['value'].iloc[-1])
naive_mae = mean_absolute_error(test['value'], naive_pred)

# Seasonal naive: same day last week
seasonal_naive = train['value'].iloc[-7:].values  # Adjust for seasonality
seasonal_pred = np.tile(seasonal_naive, len(test) // 7 + 1)[:len(test)]
seasonal_mae = mean_absolute_error(test['value'], seasonal_pred)

# Moving average
ma_pred = train['value'].rolling(7).mean().iloc[-1]  # Repeat for forecast
ma_mae = mean_absolute_error(test['value'], np.full(len(test), ma_pred))

print(f"Naive MAE: {naive_mae:.2f}")
print(f"Seasonal Naive MAE: {seasonal_mae:.2f}")
print(f"Moving Average MAE: {ma_mae:.2f}")

best_baseline = min(naive_mae, seasonal_mae, ma_mae)
print(f"\nBest baseline: {best_baseline:.2f}")
```

### 6. ARIMA/SARIMA Model (45 min)

```python
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
import warnings

# Auto-select parameters (or use pmdarima for auto)
# Manual approach:
warnings.filterwarnings('ignore')

# Simple ARIMA
model = ARIMA(train['value'], order=(1, 1, 1))
arima_fit = model.fit()
arima_pred = arima_fit.forecast(steps=len(test))
arima_mae = mean_absolute_error(test['value'], arima_pred)

# SARIMA with seasonality
model = SARIMAX(train['value'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 7))
sarima_fit = model.fit()
sarima_pred = sarima_fit.forecast(steps=len(test))
sarima_mae = mean_absolute_error(test['value'], sarima_pred)

print(f"ARIMA MAE: {arima_mae:.2f}")
print(f"SARIMA MAE: {sarima_mae:.2f}")
print(f"Improvement over baseline: {(best_baseline - sarima_mae) / best_baseline * 100:.1f}%")
```

### 7. Evaluate and Visualize (20 min)

```python
# Plot predictions
plt.figure(figsize=(12, 6))
train['value'][-30:].plot(label='Train')
test['value'].plot(label='Actual')
pd.Series(sarima_pred, index=test.index).plot(label='Forecast', linestyle='--')
plt.fill_between(test.index,
                 sarima_pred - 1.96 * sarima_fit.resid.std(),
                 sarima_pred + 1.96 * sarima_fit.resid.std(),
                 alpha=0.2, label='95% CI')
plt.legend()
plt.savefig('forecast_results.png')

# Error distribution
residuals = test['value'] - sarima_pred
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
residuals.hist(bins=30)
plt.title('Residual Distribution')
plt.subplot(1, 2, 2)
residuals.plot()
plt.title('Residuals Over Time')
plt.savefig('forecast_residuals.png')
```

### 8. Document Results (15 min)

```markdown
## Forecasting Results: [Project Name]

### Data Summary
- **Series**: [Description]
- **Frequency**: Daily
- **Length**: X data points
- **Forecast Horizon**: Y days

### Model Comparison

| Model | MAE | RMSE | MAPE |
|-------|-----|------|------|
| Naive | X.XX | X.XX | X.X% |
| Seasonal Naive | X.XX | X.XX | X.X% |
| ARIMA(1,1,1) | X.XX | X.XX | X.X% |
| SARIMA(1,1,1)(1,1,1,7) | X.XX | X.XX | X.X% |

### Best Model
SARIMA with weekly seasonality, X% improvement over baseline.

### Limitations
- [Limitation 1]
- [Limitation 2]

### Next Steps
- [ ] Try Prophet for comparison
- [ ] Add exogenous variables
- [ ] Deploy as scheduled job
```

## Artifacts Produced

- `forecast_model.pkl` - Serialized model
- `forecast_results.png` - Visualization
- `forecast_report.md` - Documentation
- `forecasting.py` - Training script

## Quality Bar

- [ ] Stationarity assessed
- [ ] Multiple baselines compared
- [ ] Time-based train/test split (no leakage)
- [ ] Confidence intervals provided
- [ ] Beat naive baseline

## Common Pitfalls

1. **Data leakage** - Using future data in training
2. **Wrong frequency** - Mismatched data/model frequency
3. **Ignoring seasonality** - Missing obvious patterns
4. **Over-differencing** - Too much differencing kills signal
