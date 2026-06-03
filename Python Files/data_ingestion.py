import pandas as pd
import requests
from pathlib import Path
import os

Data_path="../data/raw"

csv_files=[f for f in os.listdir(Data_path) if f.endswith(".csv")]
for file in csv_files:
    print("\n"+"="*50)

    print(f"Dataset: {file}")

    df=pd.read_csv(os.path.join(Data_path,file))

    print("Shape: ",df.shape)

    print("Types: ",df.dtypes)

    print("Missing values: ",df.isnull().sum())


