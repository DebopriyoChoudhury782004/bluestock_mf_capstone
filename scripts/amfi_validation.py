import pandas as pd

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav_history = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

master_codes = set(
    fund_master["amfi_code"]
)

nav_codes = set(
    nav_history["amfi_code"]
)

missing_codes = master_codes - nav_codes

print("\nAMFI Validation")
print("="*50)

print(
    f"Total Codes in Fund Master: "
    f"{len(master_codes)}"
)

print(
    f"Total Codes in NAV History: "
    f"{len(nav_codes)}"
)

print(
    f"Missing Codes: "
    f"{len(missing_codes)}"
)

if len(missing_codes) > 0:

    print("\nMissing Codes List")

    for code in missing_codes:
        print(code)

else:
    print(
        "\nAll fund master AMFI codes "
        "exist in nav_history."
    )