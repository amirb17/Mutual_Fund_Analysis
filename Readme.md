# Mutual Fund Analysis

## Project Overview

This project analyzes Indian mutual fund performance, investor behavior, AUM trends, SIP inflows, and portfolio holdings using historical NAV data and industry datasets.

The project follows a complete data analytics workflow:

* Data Ingestion
* Data Cleaning & Validation
* SQLite Data Warehouse Design
* SQL Analytics
* Dashboard Development (Power BI)
* Business Insights Generation

---

## Tech Stack

* Python
* Pandas
* NumPy
* SQLAlchemy
* SQLite
* Jupyter Notebook
* SQL
* Git & GitHub
* Power BI (Upcoming)

---

## Project Structure

```text
Mutual_Fund_Analysis
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   ├── 01_Data_Ingestion.ipynb
│   └── 02_Data_Cleaning_SQLite.ipynb
│
├── reports
│   ├── data_dictionary.md
│   └── validation_report.md
│
├── sql
│   ├── schema.sql
│   └── queries.sql
│
├── dashboards
│
├── requirements.txt
│
└── README.md
```

---

## Day 1 Completed

### Data Ingestion

* Fetched historical NAV data from MFAPI using Python Requests.
* Retrieved NAV history for multiple mutual fund schemes.
* Converted JSON API responses into CSV files.
* Created project folder structure.
* Stored raw datasets in data/raw.
* Performed dataset profiling and validation.
* Validated AMFI scheme codes across datasets.
* Documented ingestion workflow.

### Deliverables

* Raw NAV datasets
* Fund Master dataset
* Initial validation report
* GitHub repository setup

---

## Day 2 Completed

### Data Cleaning & Validation

* Cleaned NAV history dataset.
* Parsed date columns into datetime format.
* Sorted NAV data by AMFI code and date.
* Removed duplicate records.
* Validated NAV values greater than zero.
* Standardized transaction types (SIP, Lumpsum, Redemption).
* Validated transaction amounts and KYC status values.
* Validated return metrics and performance indicators.
* Flagged negative Sharpe Ratio values.
* Validated expense ratio range (0.1% – 2.5%).

### Database Design

* Designed SQLite Star Schema.
* Created:

  * dim_fund
  * dim_date
  * fact_nav
  * fact_transactions
  * fact_performance
  * fact_aum

### Data Loading

* Loaded cleaned datasets into SQLite using SQLAlchemy.
* Verified row counts and table integrity.
* Created centralized analytics database:

  * `bluestock_mf.db`

### SQL Analytics

Created analytical queries including:

* Top 5 Funds by AUM
* Average NAV per Month
* SIP Year-over-Year Growth
* Transactions by State
* Funds with Expense Ratio below 1%
* Average Returns by Risk Grade
* Transaction Type Analysis
* Fund House Performance Analysis
* Sharpe Ratio Ranking
* Investment Trend Analysis

### Documentation

* Created Data Dictionary
* Created SQL Schema Documentation
* Created SQL Query Repository

### Deliverables

* 10 Cleaned CSV Files
* SQLite Database (`bluestock_mf.db`)
* `schema.sql`
* `queries.sql`
* `data_dictionary.md`

---

## Learning Outcomes

* API Data Ingestion
* Data Cleaning & Validation
* Data Quality Checks
* Relational Database Design
* Star Schema Modeling
* SQLite & SQLAlchemy
* Advanced SQL Analytics
* Financial Data Analysis
* Documentation Best Practices
* Git & GitHub Workflow

---

## Author

**Amir Bensekar**

MCA | Data Analytics | Data Engineering

Skills:
Python • SQL • Power BI • Snowflake • dbt • MongoDB
