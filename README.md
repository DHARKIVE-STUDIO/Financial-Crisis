# 📉 Financial Crisis Analysis Studio
**Quantitative Deep-Dive into Global Systemic Risk (1800 – Present)**

## 📌 Project Overview
This repository provides a longitudinal study of global financial instability, analyzing over two centuries of economic shocks. By synthesizing banking, currency, inflation, and systemic crisis data, the studio identifies historical precursors to market collapses and forecasts future regimes of instability using time-series econometrics.

---

## 🌎 Geospatial Crisis Distribution
A core component of this research is mapping the regional density of crises. The geospatial analysis reveals that while "Inflation Crises" are historically concentrated in Latin America and portions of Africa, "Banking Crises" show significant historical clusters in North America and Western Europe.

<p align="center">
  <img src="images/global_summary_map.jpg" width="850" alt="Global Crisis Summary Map">
</p>

---

## 🔍 Quantitative Insights & Features

### 1. Cumulative Risk Growth
Tracking cumulative frequency since 1800 highlights a significant "inflection point" post-1970. This period correlates with increased global financial integration and the shift away from the Gold Standard, leading to a visible acceleration in Banking and Currency shocks.

<p align="center">
  <img src="images/cumulative_crises.png" width="900" alt="Cumulative Crisis Analysis">
</p>

### 2. Statistical Correlation Heatmap
The Pearson Correlation Heatmap identifies critical dependencies between crisis types. A standout finding is the **0.73 correlation** between Banking Crises and Systemic Crises, suggesting that banking sector failures are the primary driver of broader systemic collapses in modern economies.

<p align="center">
  <img src="images/correlation_heatmap.png" width="650" alt="Correlation Heatmap">
</p>

---

## 🧪 Model Diagnostics & Predictive Modeling

### Residual Validation
To ensure the integrity of the predictive models, I performed exhaustive **Residual Diagnostics**. Below is the diagnostic panel for the Banking Crisis model, which confirms the model is well-specified with normally distributed residuals and minimal autocorrelation (ACF).

<p align="center">
  <img src="images/residual_diagnostics.png" width="850" alt="Banking Crisis Residual Panel">
</p>

* **ACF Plot:** Validates that residuals are White Noise (no remaining patterns).
* **Kernel Density Plot:** Confirms the error distribution is centered around zero, indicating unbiased predictions.

### Future Forecasting (2020 – 2050)
Using multi-step time-series forecasting, I projected potential crisis regimes into 2050. These models highlight expected periods of volatility based on historical cycle lengths and long-term economic trends.

<p align="center">
  <img src="images/banking_forecast.png" width="900" alt="Banking Crisis Forecast">
  <br>
  <em>Multi-step Forecast for Banking Crisis (Red) alongside Observed Data (Blue).</em>
</p>

---

## 🛠 Tech Stack
* **Data Engineering:** Python, Pandas, NumPy
* **Statistical Analysis:** Statsmodels (ARIMA/SARIMA Diagnostics), Scipy
* **Visualization:** Matplotlib, Seaborn, Geopandas
* **Environment:** Google Colab / Jupyter Notebooks

## 📂 Repository Architecture
```text
├── data/               # Raw economic datasets (1800-Present)
├── images/             # High-resolution research charts
├── notebooks/          # Full EDA and Time-Series Forecasting
├── src/                # Modular Python scripts for data cleaning
└── requirements.txt    # Production dependencies
