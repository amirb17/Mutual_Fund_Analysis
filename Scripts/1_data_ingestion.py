#!/usr/bin/env python
# coding: utf-8

# Load all 10 CSV files data Info

# In[4]:


import pandas as pd
import requests
from pathlib import Path
import os


# In[5]:


Data_path="../data/raw"

csv_files=[f for f in os.listdir(Data_path) if f.endswith(".csv")]
for file in csv_files:
    print("\n"+"="*50)

    print(f"Dataset: {file}")

    df=pd.read_csv(os.path.join(Data_path,file))

    print("Shape: ",df.shape)

    print("Types: ",df.dtypes)

    print("Missing values: ",df.isnull().sum())




# Fetching live NAV data from mfapi

# In[8]:


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


# In[15]:


df=pd.read_csv(os.path.join(Data_path,"01_fund_master.csv"))
print("Unique Fund Houses: ",df["fund_house"].nunique)
print("Unique Fund Houses: ",df["fund_house"].unique)


# In[17]:


print("Categories: ")
print(df["category"].value_counts())


# In[18]:


print("Risk Categories: \n",df["risk_category"].value_counts())


# In[20]:


fund_master_code=set(df["amfi_code"])
ndf=pd.read_csv(os.path.join(Data_path,"02_nav_history.csv"))
nav_master_code=set(ndf["amfi_code"])
missing_code=fund_master_code-nav_master_code
print("="*50)
print("Fund Master Codes :", len(fund_master_code))
print("NAV History Codes :", len(nav_master_code))
print("Missing Codes     :", len(missing_code))
print("Missing Code List :", missing_code)


# In[ ]:




