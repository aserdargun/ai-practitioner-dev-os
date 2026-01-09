# Skill: Forecasting Checklist

Build reliable time series forecasting models with proper validation.

## Trigger

Use this skill when:
- Predicting future values based on historical data
- Working with temporal patterns (seasonality, trends)
- Building demand forecasting, sales prediction, etc.

## Prerequisites

- [ ] Time series data with datetime index
- [ ] Understanding of business seasonality
- [ ] Forecast horizon defined
- [ ] Baseline metrics from naive forecasts

## Steps

### 1. Time Series EDA (30 min)

```python
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Ensure datetime index
df.index = pd.to_datetime(df.index)
df = df.sort_index()

# Plot raw series
df['target'].plot(figsize=(12, 4), title='Time Series')

# Decomposition
decomposition = seasonal_decompose(df['target'], model='additive', period=12)
decomposition.plot()

# Check stationarity
from statsmodels.tsa.stattools import adfuller
result = adfuller(df['target'].dropna())
print(f'ADF Statistic: {result[0]:.4f}')
print(f'p-value: {result[1]:.4f}')
```

**Document**:
- Trend direction and strength
- Seasonality patterns (daily, weekly, yearly)
- Anomalies and outliers
- Stationarity status

### 2. Create Validation Strategy (20 min)

**Critical**: Use time-based splits, never random splits.

```python
# Walk-forward validation
def time_series_cv(df, n_splits=5, test_size=30):
    """Generate time-based train/test splits."""
    splits = []
    for i in range(n_splits):
        test_end = len(df) - (i * test_size)
        test_start = test_end - test_size
        train_end = test_start

        splits.append((
            df.iloc[:train_end],
            df.iloc[test_start:test_end]
        ))
    return splits

# Or use TimeSeriesSplit from sklearn
from sklearn.model_selection import TimeSeriesSplit
tscv = TimeSeriesSplit(n_splits=5)
```

### 3. Establish Baselines (15 min)

```python
# Naive forecast (last value)
naive_pred = df['target'].shift(1)

# Seasonal naive (same value last period)
seasonal_naive = df['target'].shift(12)  # for monthly with yearly seasonality

# Moving average
ma_pred = df['target'].rolling(window=7).mean()

# Calculate baseline metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

baseline_mae = mean_absolute_error(actual, naive_pred)
baseline_rmse = np.sqrt(mean_squared_error(actual, naive_pred))
```

**Document**: Baseline performance as the bar to beat.

### 4. Feature Engineering (30 min)

```python
# Calendar features
df['day_of_week'] = df.index.dayofweek
df['month'] = df.index.month
df['is_weekend'] = df.index.dayofweek >= 5

# Lag features
for lag in [1, 7, 14, 30]:
    df[f'lag_{lag}'] = df['target'].shift(lag)

# Rolling statistics
for window in [7, 30]:
    df[f'rolling_mean_{window}'] = df['target'].rolling(window).mean()
    df[f'rolling_std_{window}'] = df['target'].rolling(window).std()

# Handle missing values from lags
df = df.dropna()
```

### 5. Model Selection (varies)

| Approach | When to Use | Library |
|----------|-------------|---------|
| ARIMA/SARIMA | Single series, interpretable | statsmodels |
| Prophet | Strong seasonality, easy | prophet |
| XGBoost/LightGBM | Many features, complex patterns | xgboost/lightgbm |
| LSTM/Transformer | Long sequences, complex patterns | PyTorch/TensorFlow |

```python
# Example: Prophet
from prophet import Prophet

model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False
)
model.fit(train_df)
forecast = model.predict(future_df)
```

### 6. Evaluation (20 min)

```python
# Metrics
mae = mean_absolute_error(y_true, y_pred)
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100

# Skill score (improvement over baseline)
skill = 1 - (mae / baseline_mae)

# Plot predictions vs actuals
plt.figure(figsize=(12, 4))
plt.plot(y_true.index, y_true, label='Actual')
plt.plot(y_pred.index, y_pred, label='Predicted')
plt.fill_between(y_pred.index, lower_bound, upper_bound, alpha=0.3)
plt.legend()
```

**Document**:
- MAE, RMSE, MAPE
- Skill score vs baseline
- Performance by forecast horizon
- Known failure modes

### 7. Production Considerations (20 min)

- [ ] How will model be retrained?
- [ ] How to handle missing data in production?
- [ ] Monitoring for drift
- [ ] Fallback to baseline if model fails
- [ ] Confidence intervals for business decisions

## Artifacts

| Artifact | Description |
|----------|-------------|
| `forecast_eda.ipynb` | Time series exploration |
| `forecast_model.joblib` | Trained model |
| `forecast_metrics.json` | Evaluation results |
| `forecast_card.md` | Model documentation |

## Quality Bar

- [ ] Time-based validation used (not random split)
- [ ] Baseline performance established
- [ ] Multiple forecast horizons evaluated
- [ ] Seasonality properly handled
- [ ] Confidence intervals provided
- [ ] Performance compared to naive forecast

## Time Estimate

| Experience | Time |
|------------|------|
| First time | 4-6 hours |
| Practiced | 2-3 hours |
| Expert | 1-2 hours |

## Common Pitfalls

- Using random train/test splits
- Leaking future information
- Ignoring seasonality
- Not handling missing timestamps
- Over-engineering when naive works well
- Not providing uncertainty estimates
