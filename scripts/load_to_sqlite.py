from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

files = {
    "clean_fund_master.csv": "dim_fund",
    "clean_nav.csv": "fact_nav",
    "clean_transactions.csv": "fact_transactions",
    "clean_performance.csv": "fact_performance",
    "clean_aum.csv": "fact_aum",
    "clean_sip_inflows.csv": "fact_sip_inflows",
    "clean_category_inflows.csv": "fact_category_inflows",
    "clean_folio_count.csv": "fact_folio_count",
    "clean_portfolio_holdings.csv": "fact_portfolio",
    "clean_benchmark_indices.csv": "fact_benchmark"
}

for file, table in files.items():

    df = pd.read_csv(
        f"data/processed/{file}"
    )

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"{table}: {len(df)} rows loaded"
    )

print("\nDatabase loaded successfully.")