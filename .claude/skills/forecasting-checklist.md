# Skill: Forecasting Checklist

Time series forecasting workflow from data to predictions.

## Trigger

Use this skill when:
- Predicting future values (sales, demand, prices)
- Working with time-indexed data
- Building forecasting dashboards
- Evaluating forecast accuracy

## Prerequisites

- Time series data with datetime index
- Clear forecast horizon (how far ahead)
- Business context for the forecast
- Understanding of seasonality patterns

## Steps

### 1. Time Series EDA (20 min)

```python
import pandas as pd
import matplotlib.pyplot as plt

# Ensure datetime index
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df = df.asfreq('D')  # Set frequency (D=daily, M=monthly, etc.)

# Check for gaps
print(f"Missing dates: {df.index.isnull().sum()}")
print(f"Date range: {df.index.min()} to {df.index.max()}")

# Plot the series
fig, axes = plt.subplots(3, 1, figsize=(12, 8))

# Raw series
df['value'].plot(ax=axes[0], title='Raw Time Series')

# Rolling mean and std
df['value'].rolling(window=30).mean().plot(ax=axes[1], title='30-Day Rolling Mean')
df['value'].rolling(window=30).std().plot(ax=axes[2], title='30-Day Rolling Std')

plt.tight_layout()
```

### 2. Stationarity Check (10 min)

```python
from statsmodels.tsa.stattools import adfuller

def check_stationarity(series, name='Series'):
    result = adfuller(series.dropna())
    print(f"{name}:")
    print(f"  ADF Statistic: {result[0]:.4f}")
    print(f"  p-value: {result[1]:.4f}")
    print(f"  Stationary: {'Yes' if result[1] < 0.05 else 'No'}")

check_stationarity(df['value'], 'Original')

# If not stationary, try differencing
if adfuller(df['value'].dropna())[1] > 0.05:
    df['value_diff'] = df['value'].diff()
    check_stationarity(df['value_diff'], 'Differenced')
```

### 3. Decomposition (15 min)

```python
from statsmodels.tsa.seasonal import seasonal_decompose

# Decompose (use period based on your data)
decomposition = seasonal_decompose(df['value'], model='additive', period=7)

fig, axes = plt.subplots(4, 1, figsize=(12, 10))
decomposition.observed.plot(ax=axes[0], title='Observed')
decomposition.trend.plot(ax=axes[1], title='Trend')
decomposition.seasonal.plot(ax=axes[2], title='Seasonal')
decomposition.resid.plot(ax=axes[3], title='Residual')
plt.tight_layout()
```

Document:
- Trend direction (up, down, flat)
- Seasonal period (weekly, monthly, yearly)
- Residual patterns

### 4. Train/Test Split (5 min)

```python
# Time-based split (no shuffle!)
train_size = int(len(df) * 0.8)
train = df.iloc[:train_size]
test = df.iloc[train_size:]

print(f"Train: {train.index.min()} to {train.index.max()}")
print(f"Test: {test.index.min()} to {test.index.max()}")
```

### 5. Baseline Forecast (10 min)

```python
# Naive: use last value
naive_forecast = [train['value'].iloc[-1]] * len(test)

# Seasonal naive: use value from same period last cycle
seasonal_naive = test.index.map(
    lambda x: train['value'].loc[x - pd.Timedelta(days=7)]
)

# Moving average
ma_forecast = train['value'].iloc[-7:].mean()

from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def evaluate_forecast(actual, predicted, name):
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    print(f"{name}: MAE={mae:.2f}, RMSE={rmse:.2f}, MAPE={mape:.1f}%")

evaluate_forecast(test['value'], naive_forecast, 'Naive')
```

### 6. Model Selection and Training (30 min)

```python
# ARIMA (traditional)
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(train['value'], order=(1, 1, 1))  # (p, d, q)
fitted = model.fit()
arima_forecast = fitted.forecast(steps=len(test))

# Auto ARIMA (if pmdarima installed)
# from pmdarima import auto_arima
# auto_model = auto_arima(train['value'], seasonal=True, m=7)

# Prophet (if installed)
# from prophet import Prophet
# prophet_model = Prophet()
# prophet_model.fit(train.reset_index().rename(columns={'date': 'ds', 'value': 'y'}))

evaluate_forecast(test['value'], arima_forecast, 'ARIMA(1,1,1)')
```

### 7. Evaluation (15 min)

```python
# Comprehensive evaluation
results = pd.DataFrame({
    'Actual': test['value'].values,
    'ARIMA': arima_forecast.values,
    'Naive': naive_forecast,
})

# Plot forecasts
plt.figure(figsize=(12, 6))
plt.plot(train.index[-30:], train['value'].iloc[-30:], label='Train')
plt.plot(test.index, test['value'], label='Actual', marker='o')
plt.plot(test.index, arima_forecast, label='ARIMA', linestyle='--')
plt.legend()
plt.title('Forecast Comparison')
```

### 8. Document Forecast (10 min)

```markdown
## Forecast Summary

**Model**: ARIMA(1,1,1)
**Horizon**: 14 days
**Training Period**: 2024-01-01 to 2025-12-31

### Performance
| Metric | Baseline (Naive) | ARIMA |
|--------|------------------|-------|
| MAE | 125.3 | 89.7 |
| RMSE | 156.2 | 112.4 |
| MAPE | 8.2% | 5.9% |

### Key Findings
- Strong weekly seasonality (weekends peak)
- Upward trend of 2% per month
- Holidays cause spikes (account separately)

### Limitations
- Trained on 2 years of data
- Does not account for external factors
- Accuracy decreases after 7 days

### Recommendations
- Use 7-day forecasts for operations
- Update model monthly
- Add holiday effects for better accuracy
```

## Artifacts Produced

- [ ] `forecasting_notebook.ipynb` — Full analysis
- [ ] `forecast_summary.md` — Results documentation
- [ ] `model.pkl` — Saved model
- [ ] Forecast plots (PNG)
- [ ] `forecast_output.csv` — Predictions

## Quality Bar

- [ ] Stationarity addressed
- [ ] Baseline comparison included
- [ ] Multiple metrics reported (MAE, RMSE, MAPE)
- [ ] Forecast horizon appropriate for use case
- [ ] Limitations documented
- [ ] Visual comparison of predictions vs actual

## Common Pitfalls

1. **Using future data in training**
   - Always time-based split, never random

2. **Ignoring seasonality**
   - Decompose and account for patterns

3. **Only reporting RMSE**
   - MAPE is more interpretable for business

4. **Forecasting too far ahead**
   - Accuracy drops quickly; know your limits

5. **Not having a baseline**
   - Naive forecasts are surprisingly good
