# Skill: Forecasting Checklist

**Tier**: 1 (Beginner)

Build and validate time series forecasting models with proper methodology.

---

## Trigger

Use this skill when:
- Predicting future values over time
- Working with time series data
- Building demand, sales, or metric forecasts

## Prerequisites

- [ ] Time series dataset with datetime index
- [ ] Understanding of the forecast horizon needed
- [ ] Python with pandas, matplotlib, statsmodels

## Steps

### Step 1: Prepare Time Series Data (15 min)

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load and set datetime index
df = pd.read_csv('data.csv', parse_dates=['date'])
df = df.set_index('date').sort_index()

# Check for gaps
date_range = pd.date_range(start=df.index.min(), end=df.index.max(), freq='D')
missing_dates = date_range.difference(df.index)
print(f"Missing dates: {len(missing_dates)}")

# Resample if needed (e.g., to daily)
df = df.resample('D').sum()  # or mean(), first(), etc.

# Fill missing values
df = df.fillna(method='ffill')  # or interpolate()

print(f"Date range: {df.index.min()} to {df.index.max()}")
print(f"Records: {len(df)}")
```

**Checkpoint**: Clean time series with proper datetime index.

### Step 2: Visualize and Decompose (15 min)

```python
from statsmodels.tsa.seasonal import seasonal_decompose

# Plot raw series
df['value'].plot(figsize=(12, 4), title='Time Series')
plt.show()

# Decompose (if enough data)
if len(df) >= 2 * 365:  # At least 2 years for yearly seasonality
    decomposition = seasonal_decompose(df['value'], period=365)
    decomposition.plot()
    plt.tight_layout()
    plt.show()

# Check for trend
rolling_mean = df['value'].rolling(window=30).mean()
rolling_std = df['value'].rolling(window=30).std()

plt.figure(figsize=(12, 4))
plt.plot(df['value'], label='Original')
plt.plot(rolling_mean, label='Rolling Mean')
plt.plot(rolling_std, label='Rolling Std')
plt.legend()
plt.title('Trend Analysis')
plt.show()
```

**Checkpoint**: Understand trend, seasonality, and noise patterns.

### Step 3: Check Stationarity (10 min)

```python
from statsmodels.tsa.stattools import adfuller

def check_stationarity(series):
    result = adfuller(series.dropna())
    print(f'ADF Statistic: {result[0]:.4f}')
    print(f'p-value: {result[1]:.4f}')
    print('Stationary' if result[1] < 0.05 else 'Non-stationary')
    return result[1] < 0.05

is_stationary = check_stationarity(df['value'])

# If not stationary, try differencing
if not is_stationary:
    df['value_diff'] = df['value'].diff()
    check_stationarity(df['value_diff'])
```

**Checkpoint**: Know if series is stationary; differencing order if needed.

### Step 4: Train-Test Split (Time-based) (5 min)

```python
# IMPORTANT: Time series split must be chronological
split_date = df.index[-30]  # Hold out last 30 days

train = df[df.index < split_date]
test = df[df.index >= split_date]

print(f"Train: {len(train)} records ({train.index.min()} to {train.index.max()})")
print(f"Test: {len(test)} records ({test.index.min()} to {test.index.max()})")

# Visualize split
plt.figure(figsize=(12, 4))
train['value'].plot(label='Train')
test['value'].plot(label='Test')
plt.axvline(x=split_date, color='r', linestyle='--', label='Split')
plt.legend()
plt.show()
```

**Checkpoint**: Chronological train/test split (no data leakage).

### Step 5: Build Baseline Forecasts (15 min)

```python
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Naive forecast (last value)
naive_pred = np.full(len(test), train['value'].iloc[-1])

# Seasonal naive (same day last week/year)
seasonal_pred = train['value'].iloc[-len(test):].values

# Moving average
ma_pred = np.full(len(test), train['value'].rolling(7).mean().iloc[-1])

# Evaluate baselines
def evaluate_forecast(y_true, y_pred, name):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    print(f"{name}: MAE={mae:.2f}, RMSE={rmse:.2f}, MAPE={mape:.2f}%")
    return {'name': name, 'mae': mae, 'rmse': rmse, 'mape': mape}

evaluate_forecast(test['value'], naive_pred, 'Naive')
evaluate_forecast(test['value'], ma_pred, 'Moving Average')
```

**Checkpoint**: Baseline forecasts established.

### Step 6: Build Statistical Model (20 min)

```python
from statsmodels.tsa.arima.model import ARIMA
# or from statsmodels.tsa.holtwinters import ExponentialSmoothing

# ARIMA model
# p = AR order, d = differencing, q = MA order
model = ARIMA(train['value'], order=(1, 1, 1))
fitted = model.fit()

print(fitted.summary())

# Forecast
forecast = fitted.forecast(steps=len(test))

# Evaluate
evaluate_forecast(test['value'], forecast, 'ARIMA(1,1,1)')

# Plot
plt.figure(figsize=(12, 4))
train['value'].plot(label='Train')
test['value'].plot(label='Actual')
plt.plot(test.index, forecast, label='Forecast', color='red')
plt.legend()
plt.title('ARIMA Forecast')
plt.show()
```

**Checkpoint**: Statistical model trained and evaluated.

### Step 7: Document Results (10 min)

```markdown
## Forecasting Results: [Project Name]

### Data Summary
- Date range: [Start] to [End]
- Frequency: [Daily/Weekly/etc.]
- Seasonality: [Yearly/Weekly/None]

### Model Comparison

| Model | MAE | RMSE | MAPE |
|-------|-----|------|------|
| Naive | X | X | X% |
| Moving Avg | X | X | X% |
| ARIMA | X | X | X% |

### Best Model
- Model: [Best model]
- Parameters: [If applicable]
- Why: [Justification]

### Forecast Horizon
- Reliable: [X days/weeks]
- Uncertainty increases after: [Y days]

### Recommendations
- [Next steps]
- [Improvements to try]
```

**Checkpoint**: Results documented with model comparison.

## Artifacts Produced

- [ ] Cleaned time series dataset
- [ ] Visualization of decomposition
- [ ] Trained forecasting model
- [ ] Model comparison table
- [ ] Forecast documentation

## Quality Bar

✅ **Done when**:
- Data is properly indexed by time
- Train/test split is chronological
- Baselines are established
- Model beats naive baseline
- Results are documented
- Forecast horizon is defined

## Common Pitfalls

- **Random train/test split**: Time series must be split chronologically
- **Ignoring seasonality**: Check for daily, weekly, yearly patterns
- **Over-fitting**: Use holdout set for final evaluation
- **Wrong evaluation metric**: MAPE struggles with zeros; use MAE/RMSE

## Example Prompt

```
I have daily sales data for the past 2 years. Help me:

1. Prepare the data for forecasting
2. Build baseline models
3. Create an ARIMA forecast for the next 30 days

The business needs weekly forecasts for inventory planning.
```

## Related Skills

- [EDA to Insight](eda-to-insight.md) - Explore data first
- [Experiment Plan](experiment-plan.md) - Plan model improvements
