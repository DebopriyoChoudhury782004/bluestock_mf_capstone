import pandas as pd
import os

RAW = "data/raw"
PROCESSED = "data/processed"

os.makedirs(PROCESSED, exist_ok=True)

# -------------------------
# NAV HISTORY
# -------------------------

nav = pd.read_csv(f"{RAW}/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    f"{PROCESSED}/clean_nav.csv",
    index=False
)

# -------------------------
# TRANSACTIONS
# -------------------------

tx = pd.read_csv(
    f"{RAW}/08_investor_transactions.csv"
)

tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"]
)

tx["transaction_type"] = (
    tx["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

tx = tx[
    tx["transaction_type"]
    .isin(valid_types)
]

tx = tx[
    tx["amount_inr"] > 0
]

valid_kyc = [
    "Verified",
    "Pending"
]

tx = tx[
    tx["kyc_status"]
    .isin(valid_kyc)
]

tx.to_csv(
    f"{PROCESSED}/clean_transactions.csv",
    index=False
)

# -------------------------
# PERFORMANCE
# -------------------------

perf = pd.read_csv(
    f"{RAW}/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:

    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf["negative_sharpe"] = (
    perf["sharpe_ratio"] < 0
)

perf["expense_ratio_flag"] = (
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
)

perf.to_csv(
    f"{PROCESSED}/clean_performance.csv",
    index=False
)

# -------------------------
# COPY OTHER FILES
# -------------------------

mapping = {
    "01_fund_master.csv":
    "clean_fund_master.csv",

    "03_aum_by_fund_house.csv":
    "clean_aum.csv",

    "04_monthly_sip_inflows.csv":
    "clean_sip_inflows.csv",

    "05_category_inflows.csv":
    "clean_category_inflows.csv",

    "06_industry_folio_count.csv":
    "clean_folio_count.csv",

    "09_portfolio_holdings.csv":
    "clean_portfolio_holdings.csv",

    "10_benchmark_indices.csv":
    "clean_benchmark_indices.csv"
}

for src, dst in mapping.items():

    df = pd.read_csv(
        f"{RAW}/{src}"
    )

    df.to_csv(
        f"{PROCESSED}/{dst}",
        index=False
    )

print("All cleaned datasets created.")