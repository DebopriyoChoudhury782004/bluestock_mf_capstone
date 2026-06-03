# Data Dictionary

## Project: Bluestock Mutual Fund Analytics Capstone

### Data Sources

- Mutual Fund Master Dataset
- NAV History Dataset
- AUM Dataset
- SIP Inflows Dataset
- Category Inflows Dataset
- Industry Folio Dataset
- Scheme Performance Dataset
- Investor Transactions Dataset
- Portfolio Holdings Dataset
- Benchmark Indices Dataset
- mfapi.in NAV API

---

# dim_fund

**Description:** Master dimension table containing mutual fund scheme details.

| Column             | Type    | Description                                  |
| ------------------ | ------- | -------------------------------------------- |
| amfi_code          | INTEGER | Unique AMFI scheme identifier                |
| fund_house         | TEXT    | Asset Management Company (AMC)               |
| scheme_name        | TEXT    | Mutual fund scheme name                      |
| category           | TEXT    | Broad category (Equity, Debt)                |
| sub_category       | TEXT    | Detailed category (Large Cap, Mid Cap, etc.) |
| plan               | TEXT    | Regular or Direct plan                       |
| launch_date        | DATE    | Fund launch date                             |
| benchmark          | TEXT    | Benchmark index used for comparison          |
| expense_ratio_pct  | REAL    | Expense ratio percentage                     |
| exit_load_pct      | REAL    | Exit load percentage                         |
| min_sip_amount     | INTEGER | Minimum SIP investment amount                |
| min_lumpsum_amount | INTEGER | Minimum lump sum investment amount           |
| fund_manager       | TEXT    | Fund manager name                            |
| risk_category      | TEXT    | Risk classification                          |
| sebi_category_code | TEXT    | SEBI category code                           |

Source: 01_fund_master.csv

---

# fact_nav

**Description:** Daily Net Asset Value (NAV) history for all mutual fund schemes.

| Column    | Type    | Description           |
| --------- | ------- | --------------------- |
| amfi_code | INTEGER | Fund identifier       |
| date      | DATE    | NAV date              |
| nav       | REAL    | Daily Net Asset Value |

Source: 02_nav_history.csv

---

# fact_transactions

**Description:** Investor transaction records.

| Column             | Type    | Description                                |
| ------------------ | ------- | ------------------------------------------ |
| investor_id        | TEXT    | Unique investor identifier                 |
| transaction_date   | DATE    | Transaction date                           |
| amfi_code          | INTEGER | Fund identifier                            |
| transaction_type   | TEXT    | SIP, Lumpsum, Redemption                   |
| amount_inr         | REAL    | Transaction amount in INR                  |
| state              | TEXT    | Investor state                             |
| city               | TEXT    | Investor city                              |
| city_tier          | TEXT    | Tier 1, Tier 2, Tier 3 city classification |
| age_group          | TEXT    | Investor age segment                       |
| gender             | TEXT    | Investor gender                            |
| annual_income_lakh | REAL    | Annual income in lakhs                     |
| payment_mode       | TEXT    | UPI, Net Banking, Cheque, Mandate          |
| kyc_status         | TEXT    | KYC verification status                    |

Source: 08_investor_transactions.csv

---

# fact_performance

**Description:** Mutual fund performance and risk metrics.

| Column             | Type    | Description                       |
| ------------------ | ------- | --------------------------------- |
| amfi_code          | INTEGER | Fund identifier                   |
| return_1yr_pct     | REAL    | One-year return (%)               |
| return_3yr_pct     | REAL    | Three-year annualized return (%)  |
| return_5yr_pct     | REAL    | Five-year annualized return (%)   |
| benchmark_3yr_pct  | REAL    | Benchmark three-year return (%)   |
| alpha              | REAL    | Alpha measure                     |
| beta               | REAL    | Beta measure                      |
| sharpe_ratio       | REAL    | Sharpe ratio                      |
| sortino_ratio      | REAL    | Sortino ratio                     |
| std_dev_ann_pct    | REAL    | Annualized standard deviation (%) |
| max_drawdown_pct   | REAL    | Maximum drawdown (%)              |
| aum_crore          | REAL    | Assets Under Management in crore  |
| expense_ratio_pct  | REAL    | Expense ratio (%)                 |
| morningstar_rating | INTEGER | Morningstar rating                |
| risk_grade         | TEXT    | Risk classification               |

Source: 07_scheme_performance.csv

---

# fact_aum

**Description:** Assets Under Management by fund house.

| Column         | Type    | Description              |
| -------------- | ------- | ------------------------ |
| date           | DATE    | Reporting date           |
| fund_house     | TEXT    | AMC name                 |
| aum_lakh_crore | REAL    | AUM in lakh crore        |
| aum_crore      | REAL    | AUM in crore             |
| num_schemes    | INTEGER | Number of active schemes |

Source: 03_aum_by_fund_house.csv

---

# fact_sip_inflows

**Description:** Monthly SIP industry statistics.

| Column                    | Type | Description                      |
| ------------------------- | ---- | -------------------------------- |
| month                     | TEXT | Reporting month                  |
| sip_inflow_crore          | REAL | SIP inflows in crore             |
| active_sip_accounts_crore | REAL | Active SIP accounts              |
| new_sip_accounts_lakh     | REAL | New SIP accounts opened          |
| sip_aum_lakh_crore        | REAL | SIP AUM                          |
| yoy_growth_pct            | REAL | Year-over-year growth percentage |

Source: 04_monthly_sip_inflows.csv

---

# fact_category_inflows

**Description:** Monthly mutual fund category-wise net inflows.

| Column           | Type | Description                |
| ---------------- | ---- | -------------------------- |
| month            | TEXT | Reporting month            |
| category         | TEXT | Fund category              |
| net_inflow_crore | REAL | Net inflow amount in crore |

Source: 05_category_inflows.csv

---

# fact_folio_count

**Description:** Industry-wide folio statistics.

| Column              | Type | Description     |
| ------------------- | ---- | --------------- |
| month               | TEXT | Reporting month |
| total_folios_crore  | REAL | Total folios    |
| equity_folios_crore | REAL | Equity folios   |
| debt_folios_crore   | REAL | Debt folios     |
| hybrid_folios_crore | REAL | Hybrid folios   |
| others_folios_crore | REAL | Other folios    |

Source: 06_industry_folio_count.csv

---

# fact_portfolio

**Description:** Portfolio holdings of mutual fund schemes.

| Column            | Type    | Description                     |
| ----------------- | ------- | ------------------------------- |
| amfi_code         | INTEGER | Fund identifier                 |
| stock_symbol      | TEXT    | Stock ticker                    |
| stock_name        | TEXT    | Company name                    |
| sector            | TEXT    | Industry sector                 |
| weight_pct        | REAL    | Portfolio allocation percentage |
| market_value_cr   | REAL    | Market value in crore           |
| current_price_inr | REAL    | Current market price            |
| portfolio_date    | DATE    | Portfolio disclosure date       |

Source: 09_portfolio_holdings.csv

---

# fact_benchmark

**Description:** Benchmark index historical values.

| Column      | Type | Description          |
| ----------- | ---- | -------------------- |
| date        | DATE | Trading date         |
| index_name  | TEXT | Benchmark index name |
| close_value | REAL | Closing index value  |

Source: 10_benchmark_indices.csv

---

## Business Definitions

- AMFI Code: Unique identifier assigned to a mutual fund scheme.
- NAV (Net Asset Value): Per-unit market value of a mutual fund.
- AUM (Assets Under Management): Total market value of assets managed by a fund house.
- SIP (Systematic Investment Plan): Recurring investment into mutual funds.
- Expense Ratio: Annual fee charged by the fund.
- Alpha: Excess return relative to benchmark.
- Beta: Measure of volatility against benchmark.
- Sharpe Ratio: Risk-adjusted return metric.
- Sortino Ratio: Downside-risk-adjusted return metric.
- Folio: Investor account in a mutual fund.
- Benchmark Index: Market index used for fund performance comparison.
- Risk Category: SEBI-defined risk classification of mutual fund schemes.
