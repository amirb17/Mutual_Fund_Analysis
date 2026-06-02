import pandas as pd
import requests
from pathlib import Path
import os

Data_path="data/raw"

Funds={
    "HDFC Top 100":125497,
    "SBI Bluechip":119551,
    "ICICI Bluechip":120503,
    "Nippon Large Cap":118632,
    "Axis Bluechip":119092,
    "Kotak Bluechip":120841
}
try:
    for funds_name,scheme_code in Funds.items():
        url=f'https://api.mfapi.in/mf/{scheme_code}'
        response=requests.get(url,timeout=30)

        response.raise_for_status()

        json_data=response.json()

        nav_df=pd.DataFrame(json_data["data"])

        output_file=os.path.join(Data_path,f"{funds_name}_NAV.csv")

        nav_df.to_csv(output_file,index=False)

        print("="*60)

        print(f'Fund: {funds_name}')
        print(f'Scheme Code: {scheme_code}')
        print(f'Record Saved :{len(nav_df)}')
        print(f'File: {output_file}')
except Exception as e:
    print(e)

