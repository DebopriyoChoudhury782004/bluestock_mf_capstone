import pandas as pd

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

print("\nUnique Fund Houses")
print("-"*50)
print(fund_master["fund_house"].unique())

print("\nUnique Categories")
print("-"*50)
print(fund_master["category"].unique())

print("\nUnique Sub Categories")
print("-"*50)
print(fund_master["sub_category"].unique())

print("\nRisk Grades")
print("-"*50)
print(
    fund_master["risk_category"]
    .value_counts()
)