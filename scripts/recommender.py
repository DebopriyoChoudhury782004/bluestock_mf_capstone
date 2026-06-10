import pandas as pd

performance = pd.read_csv(
    "../data/processed/clean_performance.csv"
)

fund_master = pd.read_csv(
    "../data/processed/clean_fund_master.csv"
)

df = performance.merge(
    fund_master,
    on="amfi_code",
    how="inner"
)

# Find scheme name column automatically
possible_cols = [
    "scheme_name",
    "scheme_name_x",
    "scheme_name_y",
    "fund_name"
]

scheme_col = None

for col in possible_cols:
    if col in df.columns:
        scheme_col = col
        break

if scheme_col is None:
    print("Available columns:")
    print(df.columns.tolist())
    raise ValueError(
        "No scheme name column found."
    )

risk = input(
    "Enter Risk (Low/Moderate/High): "
)

rec = (
    df[
        df["risk_category"]
        .astype(str)
        .str.contains(
            risk,
            case=False,
            na=False
        )
    ]
    .sort_values(
        by="sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")

print(
    rec[
        [
            scheme_col,
            "risk_category",
            "sharpe_ratio"
        ]
    ]
)
