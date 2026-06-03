from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum",
    "fact_sip_inflows",
    "fact_category_inflows",
    "fact_folio_count",
    "fact_portfolio",
    "fact_benchmark"
]

for table in tables:

    query = f"SELECT COUNT(*) as cnt FROM {table}"

    cnt = pd.read_sql(
        query,
        engine
    )

    print(
        table,
        cnt.iloc[0]["cnt"]
    )