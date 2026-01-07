# Month 7: Time Series Analysis

**Focus**: Master forecasting and temporal data patterns

---

## Why It Matters

Time series analysis is essential for:
- Demand forecasting
- Financial modeling
- Resource planning
- Anomaly detection

Most businesses have time-indexed data, making this a highly practical skill.

---

## Prerequisites

- Months 1-6 completed
- Statistics foundation (Month 3)
- ML basics understood

---

## Learning Goals

By the end of this month, you will:

1. **Time Series Concepts**
   - [ ] Trend, seasonality, noise decomposition
   - [ ] Stationarity and tests
   - [ ] Autocorrelation (ACF/PACF)
   - [ ] Time series cross-validation

2. **Forecasting Methods**
   - [ ] Moving averages
   - [ ] Exponential smoothing
   - [ ] ARIMA models
   - [ ] Seasonal decomposition

3. **Evaluation**
   - [ ] MAE, RMSE, MAPE
   - [ ] Walk-forward validation
   - [ ] Forecast horizons

4. **Practical Skills**
   - [ ] Handling missing timestamps
   - [ ] Resampling and aggregation
   - [ ] Feature engineering for time

---

## Main Project: Demand Forecasting

Build a forecasting system for a time series dataset.

### Deliverables

1. **Forecasting notebook** (`forecasting.ipynb`)
   - Data exploration and visualization
   - Stationarity analysis
   - Model comparison
   - Forecast generation

2. **Forecasting module** (`forecast/`)
   - `preprocess.py` - Data preparation
   - `models.py` - Model implementations
   - `evaluate.py` - Metrics and validation
   - `predict.py` - Generate forecasts

3. **Forecast report** (`forecast_report.md`)
   - Methodology
   - Model selection rationale
   - Forecast accuracy
   - Recommendations

4. **Visualizations**
   - Time series decomposition
   - Model comparison chart
   - Forecast with confidence intervals

### Definition of Done

- [ ] Multiple models compared
- [ ] Walk-forward validation used
- [ ] Best model documented
- [ ] Forecast includes uncertainty
- [ ] Module is reusable
- [ ] Report is complete

### Dataset Suggestions

- [Store Sales Forecasting](https://www.kaggle.com/c/store-sales-time-series-forecasting)
- [Air Passengers](https://www.kaggle.com/chirag19/air-passengers)
- [Energy Consumption](https://archive.ics.uci.edu/ml/datasets/Individual+household+electric+power+consumption)
- Web traffic data

---

## Stretch Goals

- [ ] Add Prophet or neural forecasting
- [ ] Implement anomaly detection
- [ ] Create interactive forecast dashboard
- [ ] Handle multiple time series

---

## Weekly Breakdown

### Week 1: Time Series Fundamentals
- Time series components
- Visualization techniques
- Stationarity tests
- ACF/PACF interpretation

### Week 2: Basic Forecasting
- Naive methods
- Moving averages
- Exponential smoothing
- Evaluation metrics

### Week 3: ARIMA and Beyond
- ARIMA model building
- Seasonal ARIMA (SARIMA)
- Model selection
- Diagnostics

### Week 4: Project Completion
- Build forecasting system
- Compare models
- Generate forecasts
- Documentation

---

## Claude Prompts

### Start of Month
```
/status

I'm starting Month 7: Time Series Analysis.
Help me understand the key concepts.
```

### Skill Application
```
I want to apply the Forecasting Checklist skill.
Walk me through .claude/skills/forecasting-checklist.md
for my [dataset] dataset.
```

### Stationarity Help
```
My time series looks like [description].
The ADF test p-value is [value].

Is it stationary? What transformations should I try?
```

### ARIMA Selection
```
My ACF shows [description].
My PACF shows [description].

What ARIMA(p,d,q) parameters should I try?
Explain your reasoning.
```

### Model Comparison
```
I've tried these forecasting models:
- Naive: RMSE = X
- Exponential Smoothing: RMSE = Y
- ARIMA(1,1,1): RMSE = Z

Help me select the best model considering:
- Accuracy
- Interpretability
- Forecast horizon needs
```

### Forecast Interpretation
```
My forecast shows [trend/pattern].
The confidence interval is [range].

How should I communicate this to stakeholders?
What caveats should I mention?
```

---

## How to Publish

### Demo

Showcase your forecasting system:
1. The business problem
2. Data patterns (decomposition)
3. Model comparison
4. Final forecast with uncertainty

### Write-up

Cover:
- Time series concepts applied
- Model selection process
- Interpretation of results
- Practical recommendations

### Portfolio

- Notebook with clear progression
- Reusable forecasting module
- Visualizations of forecasts

---

## Resources

### Time Series
- [Forecasting: Principles and Practice](https://otexts.com/fpp3/)
- [statsmodels Time Series](https://www.statsmodels.org/stable/tsa.html)

### Python
- [pandas Time Series](https://pandas.pydata.org/docs/user_guide/timeseries.html)
- [Prophet](https://facebook.github.io/prophet/) (optional)

### Practice
- [Kaggle Time Series Course](https://www.kaggle.com/learn/time-series)

---

## Next Month

[Month 8: NLP Basics](../month-08/README.md) - Text processing and analysis
