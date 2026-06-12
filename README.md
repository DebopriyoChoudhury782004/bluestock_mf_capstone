# Bluestock Mutual Fund Analytics Capstone

## Overview

The **Bluestock Mutual Fund Analytics Capstone** is an end-to-end financial analytics project that transforms raw mutual fund datasets into actionable business insights through data engineering, performance analysis, risk analytics, investor behaviour analysis, and interactive dashboard reporting.

The project integrates **Python, SQL, SQLite, and Power BI** to build a complete analytics pipeline covering data ingestion, cleaning, exploratory analysis, performance evaluation, advanced risk metrics, and business intelligence dashboards.

---

## Business Objectives

- Analyze mutual fund industry growth and trends.
- Evaluate fund performance using risk-adjusted metrics.
- Study investor behaviour and SIP contribution patterns.
- Measure downside risk using VaR and CVaR.
- Identify portfolio concentration risk using HHI.
- Build a mutual fund recommendation engine.
- Deliver interactive dashboards for business users.

---

## Technology Stack

### Programming & Database

- Python
- SQL
- SQLite

### Analytics Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn

### Visualization & Reporting

- Power BI
- Jupyter Notebook

### Version Control

- Git
- GitHub

---

## Project Architecture

```text
Raw CSV Datasets
        ↓
Data Ingestion
        ↓
Data Cleaning & Validation
        ↓
SQLite Database
        ↓
Exploratory Data Analysis
        ↓
Performance Analytics
        ↓
Advanced Analytics
        ↓
Power BI Dashboard
        ↓
Business Insights & Reporting
```

---

## Dataset Overview

The project uses multiple mutual fund datasets:

| Dataset               | Description                   |
| --------------------- | ----------------------------- |
| Fund Master           | Scheme metadata               |
| NAV History           | Historical NAV values         |
| AUM Data              | Assets under management       |
| SIP Inflows           | Monthly SIP contribution data |
| Category Inflows      | Category-wise inflows         |
| Investor Transactions | Investor behaviour            |
| Folio Counts          | Investor participation        |
| Portfolio Holdings    | Sector allocation             |
| Benchmark Indices     | Market comparison             |

---

## Project Structure

```text
bluestock_mf_capstone/

├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── api_nav/
│   └── db/
│
├── notebooks/
│   ├── EDA_Findings.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── reports/
│   ├── Dashboard.pdf
│   ├── Industry_Overview.png
│   ├── Fund_Performance.png
│   ├── Investor_Analytics.png
│   ├── SIP_Market_Trends.png
│   └── Analytics Reports
│
├── scripts/
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── load_to_sqlite.py
│   ├── amfi_validation.py
│   ├── recommender.py
│   └── verify_database.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── run_pipeline.py
├── requirements.txt
└── README.md
```

---

## Exploratory Data Analysis

The EDA phase focused on:

- NAV growth trends
- Industry AUM expansion
- SIP inflow patterns
- Investor demographics
- Geographic participation
- Risk distributions

### Key Findings

- SIP inflows showed consistent growth throughout the analysis period.
- Industry AUM expanded significantly between 2022 and 2025.
- The 26–35 age group contributed the highest transaction volume.
- Equity-oriented schemes dominated investor participation.

---

## Performance Analytics

The following performance metrics were calculated:

- Daily Returns
- CAGR
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown

### Top Overall Funds

| AMFI Code | Score |
| --------- | ----- |
| 120505    | 77.75 |
| 148569    | 75.25 |
| 119598    | 75.13 |
| 149324    | 74.75 |
| 120843    | 71.88 |

### Highest Sharpe Ratio Funds

| AMFI Code | Sharpe Ratio |
| --------- | ------------ |
| 148567    | 1.45         |
| 120843    | 1.31         |
| 148569    | 1.23         |
| 119551    | 1.21         |
| 120505    | 1.18         |

---

## Advanced Analytics

### Historical VaR & CVaR

95% Historical Value at Risk (VaR) and Conditional VaR (CVaR) were computed for all schemes.

#### Highest Downside Risk Funds

| AMFI Code | VaR (95%) |
| --------- | --------- |
| 119599    | -2.69%    |
| 119095    | -2.62%    |
| 101207    | -2.60%    |
| 118634    | -2.54%    |
| 119598    | -2.45%    |

---

### Rolling 90-Day Sharpe Ratio

Formula used:

```text
Rolling Sharpe =
Rolling Mean(Returns)
÷
Rolling Std(Returns)
× √252
```

This metric helped identify changes in risk-adjusted performance through time.

---

### Investor Cohort Analysis

Investors were grouped by first transaction year.

#### 2024 Cohort

- Average SIP Amount: ₹107,423
- Total Invested: ₹3.49 Billion

#### 2025 Cohort

- Average SIP Amount: ₹109,159
- Total Invested: ₹30.45 Million

**Observation:**
The 2024 cohort contributed significantly more capital than newer investors.

---

### SIP Continuity Analysis

Investors with six or more SIP transactions were analysed.

Criteria:

```text
Average Gap > 35 Days
=
At Risk Investor
```

This analysis helps identify investors likely to discontinue SIP investments.

---

### Sector Concentration Analysis

Portfolio concentration risk was measured using:

```text
HHI = Σ(weight²)
```

#### Most Concentrated Funds

| AMFI Code | HHI  |
| --------- | ---- |
| 119092    | 2064 |
| 101207    | 2007 |
| 119599    | 1747 |
| 102885    | 1747 |
| 118632    | 1683 |

---

### Recommendation Engine

A rule-based recommendation engine was developed.

**Input:**

- Low Risk
- Moderate Risk
- High Risk

**Output:**

Top 3 funds ranked by Sharpe Ratio within the selected risk category.

---

## Power BI Dashboard

The dashboard consists of four pages:

### 1. Industry Overview

- Total AUM: 39M
- Total SIP: 940K
- Total Folios: 26.12
- Total Schemes: 40

Features:

- KPI Cards
- Industry AUM Trend
- Fund House Analysis

### 2. Fund Performance

Features:

- Risk vs Return Analysis
- NAV Trends
- Fund Comparison
- Fund House Filters

### 3. Investor Analytics

Features:

- State-wise Transactions
- Age Group Analysis
- Transaction Type Analysis
- Investor Segmentation

### 4. SIP & Market Trends

Features:

- Monthly SIP Trend
- Benchmark Comparison
- Top Category Inflows
- SIP Growth KPI

---

## Key Business Insights

### Insight 1

SIP inflows demonstrated a steady upward trend, indicating growing retail participation.

### Insight 2

Funds with higher Sharpe Ratios consistently outperformed peers on a risk-adjusted basis.

### Insight 3

The majority of industry investments originated from the 2024 investor cohort.

### Insight 4

Several equity funds exhibited high concentration risk based on HHI values.

### Insight 5

Rolling Sharpe analysis revealed significant variation in risk-adjusted returns over time.

---

## Future Enhancements

- Machine Learning based recommendation engine.
- Predictive NAV forecasting.
- Real-time NAV API integration.
- Automated dashboard refresh.
- Cloud deployment and monitoring.

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Execute Project

```bash
python run_pipeline.py
```

### Open Dashboard

```text
dashboard/bluestock_mf_dashboard.pbix
```

using Power BI Desktop.

---

## Author

**Debopriyo Choudhury**

Bluestock Fintech Internship Project
