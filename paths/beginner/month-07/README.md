# Month 7: Time Series Fundamentals

**Theme**: Learn to analyze and forecast temporal data.

## Why It Matters

Time series is everywhere—sales forecasting, stock prices, demand planning, resource allocation. Companies rely on forecasts for planning. This skill is highly valued and often undertaught.

## Prerequisites

- Month 3 completed (statistics)
- Month 5 completed (regression concepts)
- Pandas datetime handling

## Learning Goals

### Time Series Basics (Week 1)
- [ ] Time series concepts and terminology
- [ ] DateTime indexing in pandas
- [ ] Resampling and frequency conversion
- [ ] Rolling statistics
- [ ] Handling missing timestamps

### Components & Patterns (Week 2)
- [ ] Trend analysis
- [ ] Seasonality detection
- [ ] Decomposition (additive, multiplicative)
- [ ] Stationarity and tests (ADF)
- [ ] Autocorrelation (ACF, PACF)

### Forecasting (Week 3-4)
- [ ] Naive forecasts (baselines)
- [ ] Moving averages
- [ ] Exponential smoothing
- [ ] ARIMA fundamentals
- [ ] Evaluation metrics (MAE, RMSE, MAPE)

## Main Project: Sales Forecaster

Build a forecasting system for retail sales data.

### Dataset
Use a retail sales time series (daily or weekly) from Kaggle.

### Deliverables
1. Time series analysis notebook:
   - Visualization of trends
   - Seasonal decomposition
   - Stationarity testing
   - ACF/PACF analysis

2. Forecasting pipeline:
   - Multiple baseline methods
   - ARIMA model
   - Model comparison
   - Out-of-sample evaluation

3. 7-day forecast with confidence intervals

### Definition of Done
- [ ] Complete time series EDA
- [ ] Decomposition visualized
- [ ] 3+ forecasting methods compared
- [ ] ARIMA model tuned
- [ ] Confidence intervals included
- [ ] Clear interpretation of results

## Stretch Goals

- [ ] Try Facebook Prophet
- [ ] Add holiday effects
- [ ] Create weekly forecast refresh
- [ ] Build simple forecast API
- [ ] Cross-validation for time series

## Weekly Breakdown

### Week 1: Time Series Basics
- DateTime handling
- Resampling
- Rolling statistics
- Explore sales dataset

### Week 2: Analysis & Decomposition
- Trend and seasonality
- Decomposition
- Stationarity testing
- ACF/PACF plots

### Week 3: Forecasting Methods
- Baseline methods
- Moving averages
- Start ARIMA
- Compare methods

### Week 4: Complete Project
- Tune ARIMA
- Generate forecasts
- Documentation
- Demo prep

## Claude Prompts

### Planning
```
/plan-week
Month 7 Week 2 - Focus on time series decomposition
I want to understand seasonal patterns in my data
```

### Skill Guidance
```
Guide me through the Forecasting Checklist skill
for my sales data.
```

### Building
```
Ask the Builder to help me implement ARIMA
with automatic parameter selection using pmdarima.
```

### Concept Help
```
Ask the Researcher to explain stationarity
and why it matters for forecasting.
Include practical tests I can run.
```

## How to Publish

### Demo
1. Show the time series
2. Present decomposition
3. Explain the forecast method
4. Show predictions vs actuals
5. Discuss confidence intervals

### Write-up Topics
- Why time series is different from regular ML
- Patterns found in the data
- Choosing forecast horizon
- Interpreting forecast uncertainty

### Portfolio Entry
- Interactive time series visualizations
- Clear forecast explanation
- Business interpretation

## Resources

### Time Series
- [statsmodels Time Series](https://www.statsmodels.org/stable/tsa.html)
- [Prophet Documentation](https://facebook.github.io/prophet/)
- [Forecasting Principles and Practice](https://otexts.com/fpp3/) — Free online book

### Videos
- [StatQuest: Time Series](https://www.youtube.com/watch?v=DeORzP0go5I)
- [ARIMA Explained](https://www.youtube.com/watch?v=3UmyHed0iYE)

### Practice
- [Kaggle Store Sales Competition](https://www.kaggle.com/c/store-sales-time-series-forecasting)

## Tips

1. **Plot first** — Always visualize before modeling
2. **Use proper splits** — Time-based, never random
3. **Start with naive** — Simple baselines are surprisingly good
4. **Check residuals** — They should look like noise
5. **Communicate uncertainty** — Forecasts are estimates, not facts
