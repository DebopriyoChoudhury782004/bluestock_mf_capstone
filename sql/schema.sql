CREATE TABLE dim_fund(
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    expense_ratio_pct REAL,
    risk_category TEXT
);

CREATE TABLE fact_nav(
    amfi_code INTEGER,
    date DATE,
    nav REAL
);

CREATE TABLE fact_transactions(
    investor_id TEXT,
    transaction_date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL
);

CREATE TABLE fact_performance(
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL
);

CREATE TABLE fact_aum(
    fund_house TEXT,
    date DATE,
    aum_crore REAL
);

CREATE TABLE fact_sip_inflows(
    month TEXT,
    sip_inflow_crore REAL
);

CREATE TABLE fact_category_inflows(
    month TEXT,
    category TEXT,
    net_inflow_crore REAL
);

CREATE TABLE fact_folio_count(
    month TEXT,
    total_folios_crore REAL
);

CREATE TABLE fact_portfolio(
    amfi_code INTEGER,
    stock_symbol TEXT,
    sector TEXT,
    weight_pct REAL
);

CREATE TABLE fact_benchmark(
    date DATE,
    index_name TEXT,
    close_value REAL
);