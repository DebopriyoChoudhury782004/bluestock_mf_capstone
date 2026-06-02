import requests
import pandas as pd
import os

os.makedirs("data/api_nav", exist_ok=True)

schemes = {
    "HDFC_Top100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():

    try:
        print(f"Fetching {name}")

        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(url, timeout=20)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        output_file = f"data/api_nav/{name}.csv"

        nav_df.to_csv(output_file, index=False)

        print(f"Saved {output_file}")

    except Exception as e:
        print(f"Error in {name}: {e}")