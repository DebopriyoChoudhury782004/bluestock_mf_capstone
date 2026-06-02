import pandas as pd
import os

RAW_PATH = "data/raw"

csv_files = sorted([
    f for f in os.listdir(RAW_PATH)
    if f.endswith(".csv")
])

print(f"\nTotal CSV Files Found: {len(csv_files)}")

for file in csv_files:

    file_path = os.path.join(RAW_PATH, file)

    df = pd.read_csv(file_path)

    print("\n" + "="*70)
    print(file)
    print("="*70)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())