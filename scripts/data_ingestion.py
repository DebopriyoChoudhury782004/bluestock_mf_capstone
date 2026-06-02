import pandas as pd
import os

RAW_PATH = "data/raw"

files = [f for f in os.listdir(RAW_PATH)
         if f.endswith(".csv")]

for file in files:

    print("\n" + "=" * 60)
    print(file)
    print("=" * 60)

    df = pd.read_csv(
        os.path.join(RAW_PATH, file)
    )

    print("\nShape:")
    print(df.shape)

    print("\nDtypes:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())