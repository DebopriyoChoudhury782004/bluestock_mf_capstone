-- 1 Top 5 funds by AUM

SELECT fund_house,
SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;


-- 2 Average NAV per month

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;


-- 3 SIP YoY Growth

-- 3 SIP Inflow YoY Growth

SELECT
month,
sip_inflow_crore,
yoy_growth_pct
FROM fact_sip_inflows
ORDER BY month;


-- 4 Transactions by State

SELECT
state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 5 Funds with expense ratio below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;


-- 6 Fund count by category

SELECT
category,
COUNT(*)
FROM dim_fund
GROUP BY category;


-- 7 Average Sharpe Ratio

SELECT
AVG(sharpe_ratio)
FROM fact_performance;


-- 8 Risk category distribution

SELECT
risk_category,
COUNT(*)
FROM dim_fund
GROUP BY risk_category;


-- 9 Transaction amount by type

SELECT
transaction_type,
SUM(amount_inr)
FROM fact_transactions
GROUP BY transaction_type;


-- 10 Top performing fund houses

SELECT
df.fund_house,
AVG(fp.return_3yr_pct) AS avg_return
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code=df.amfi_code
GROUP BY df.fund_house
ORDER BY avg_return DESC;