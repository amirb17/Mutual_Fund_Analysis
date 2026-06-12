#!/usr/bin/env python
# coding: utf-8

# Cleaning nav_history.csv

# In[6]:


import pandas as pd
import os
import sqlalchemy as sq
import sqlite3
from pathlib import Path
import datetime


# In[7]:


data_path="../data/raw"

nav_history=pd.read_csv(os.path.join(data_path,"02_nav_history.csv"))

print(nav_history.head())

print("Shape: ",nav_history.shape)

print("Null Values: ",nav_history.isnull().sum())

print("Data Types: ",nav_history.dtypes)

print("Info: ",nav_history.info())



# In[8]:


nav_history["date"]=pd.to_datetime(nav_history["date"])
nav_history.head()


# In[9]:


nav_history.sort_values(by=["amfi_code","date"])


# In[10]:


print(nav_history.isnull().sum())


# In[11]:


nav_history["nav"]=(nav_history.groupby("amfi_code")["nav"].ffill())


# In[12]:


print("Length before Removing Duplicates",len(nav_history))

nav_history=nav_history.drop_duplicates()

print("Length after Removing duplicates: ",len(nav_history))


# In[13]:


invalid_nav= nav_history[nav_history["nav"]<=0]
print("Inavlid Nav : ",invalid_nav)


# In[14]:


nav_history=nav_history[nav_history['nav']>0]


# In[15]:


datapath="../data/processed"
nav_history.to_csv(os.path.join(datapath,"clean_nav.csv"),index=False)
print("Cleaned nav history file saved in processed folder")


# Cleaning investor_transaction.csv

# In[16]:


inv_trns=pd.read_csv(os.path.join(data_path,"08_investor_transactions.csv"))
print("Columns: ",inv_trns.columns)

print("Shape: ",inv_trns.shape)

print("Data types: ",inv_trns.dtypes)

print("Missing: ",inv_trns.isnull().sum())





# In[17]:


print(inv_trns["transaction_type"].value_counts())


# In[18]:


invalid_amount=inv_trns[inv_trns["amount_inr"]<=0]
print("Invalid amounts : ",len(invalid_amount))
inv_trns=inv_trns[inv_trns["amount_inr"]>0]


# In[19]:


inv_trns["kyc_status"].value_counts()


# In[20]:


inv_trns["transaction_date"]=pd.to_datetime(inv_trns["transaction_date"])


# In[21]:


inv_trns.to_csv(os.path.join(datapath,"clean_transactions.csv"),index=False)
print("Cleaned File stored in Processed folder.")


# Cleaning Scheme Performance file

# In[22]:


sch_per=pd.read_csv(os.path.join(data_path,"07_scheme_performance.csv"))
print("Data types: ",sch_per.dtypes)

sch_per.columns = sch_per.columns.str.strip()

print(sch_per.columns.tolist())


# In[23]:


return_cols=["return_1yr_pct","return_3yr_pct","return_5yr_pct"]
try:
    for col in return_cols:
        sch_per[col]=pd.to_numeric(sch_per[col],errors="coerce")
    print("Changed Return value to numeric")
except Exception as e:
    print(e)


# In[24]:


negative_sharpe=sch_per[sch_per["sharpe_ratio"]<0]
print("Negative Sharpe Ratios: ",len(negative_sharpe))


# In[25]:


invalid_expn_ratio=sch_per[~sch_per["expense_ratio_pct"].between(0.1,2.5)]
print("Invalid Expence ratio: ",len(invalid_expn_ratio))


# In[26]:


sch_per.to_csv(os.path.join(datapath,"clean_performance.csv"),index=False)
print("Cleaned File saved in processed folder")


# Loading Cleaned csv files data into database

# In[27]:


from sqlalchemy import create_engine
import sqlalchemy


# In[ ]:


dim_nav=pd.read_csv(os.path.join("../data/processed","clean_nav.csv"))
fact_performance=pd.read_csv(os.path.join("../data/processed","clean_performance.csv"))
fact_transaction=pd.read_csv(os.path.join("../data/processed","clean_transactions.csv"))





# In[42]:


engine=create_engine(
    "sqlite:///../data/processed/bluestock_mf.db"
)
dim_nav.to_sql(
    "dim_nav",
    engine,
    if_exists="replace",
    index=False
    )
fact_performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)
fact_transaction.to_sql(
    "fact_transaction",
    engine,
    if_exists="replace",
    index=False
)


# In[43]:


pd.read_sql("select * from dim_nav limit 4",engine)
pd.read_sql("select * from fact_transaction limit 4",engine)
pd.read_sql("select * from fact_performance limit 4 ",engine)


# In[47]:


print("Row counts of CSV files: \ndim_nav: ",len(dim_nav),"\nFact_performance: ",len(fact_performance),"\nFact_transaction: ",len(fact_transaction))
print("Row counts of Database")
pd.read_sql("select count(*) as dim_nav_count from dim_nav",engine)
pd.read_sql("select count(*) as fact_performance_count from fact_performance",engine)
pd.read_sql("select count(*) as fact_transaction_count from fact_transaction",engine)


# In[ ]:




