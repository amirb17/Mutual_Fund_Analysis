# 📊 Mutual Fund Analysis

## 📌 Project Overview

This project analyzes Indian mutual fund performance, investor behavior, AUM trends, SIP inflows, portfolio holdings, and industry growth using historical NAV data and industry datasets.

The project follows a complete Data Analytics and Data Engineering workflow:

* Data Ingestion
* Data Cleaning & Validation
* SQLite Data Warehouse Design
* SQL Analytics
* Exploratory Data Analysis (EDA)
* Business Insights Generation
* Dashboard Development (Power BI)

---

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* SQLAlchemy
* SQLite
* Jupyter Notebook
* SQL
* Matplotlib
* Seaborn
* Plotly
* Git & GitHub
* Power BI

---

## 📂 Project Structure

```text
Mutual_Fund_Analysis
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   ├── 01_Data_Ingestion.ipynb
│   ├── 02_Data_Cleaning_SQLite.ipynb
│   └── 03_EDA_Analysis.ipynb
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

# 🚀 Day 1 Completed

## Data Ingestion

* Fetched historical NAV data from MFAPI using Python Requests.
* Retrieved NAV history for multiple mutual fund schemes.
* Parsed JSON responses and converted them into CSV datasets.
* Stored raw datasets in structured folders.
* Performed initial data profiling and validation.
* Validated AMFI scheme codes across datasets.

### Deliverables

* Raw NAV datasets
* Fund Master dataset
* Data profiling report
* GitHub repository setup

---

# 🚀 Day 2 Completed

## Data Cleaning & Validation

* Cleaned and validated 10 mutual fund datasets.
* Parsed date columns into datetime format.
* Sorted NAV history by AMFI code and date.
* Removed duplicate records.
* Forward-filled missing NAV values.
* Validated NAV values greater than zero.
* Standardized transaction types.
* Validated transaction amounts and KYC status values.
* Validated return metrics and performance indicators.
* Flagged negative Sharpe Ratio values.
* Validated expense ratio range (0.1% – 2.5%).

## SQLite Data Warehouse

Designed a Star Schema and loaded cleaned datasets into SQLite.

### Tables Created

#### Dimension Tables

* dim_fund
* dim_date

#### Fact Tables

* fact_nav
* fact_transactions
* fact_performance
* fact_aum

## SQL Analytics

Created analytical SQL queries including:

* Top 5 Funds by AUM
* Average NAV per Month
* SIP Year-over-Year Growth
* Transactions by State
* Funds with Expense Ratio below 1%
* Average Returns by Risk Grade
* Fund House Performance Analysis
* Sharpe Ratio Ranking
* Investment Trend Analysis
* Transaction Type Distribution

## Documentation

* Data Dictionary
* SQL Schema Documentation
* Query Documentation

### Deliverables

* 10 Cleaned CSV Files
* SQLite Database (`bluestock_mf.db`)
* `schema.sql`
* `queries.sql`
* `data_dictionary.md`

---

## 🌟 Day 2 Standout Achievements

* Cleaned and validated 10 mutual fund datasets containing over 80,000 records.
* Built a complete SQLite-based analytics database using Star Schema design.
* Implemented comprehensive data quality checks and validation rules.
* Integrated Python, Pandas, SQLAlchemy, and SQLite into an end-to-end analytics pipeline.
* Developed business-focused SQL queries for investment insights.
* Created project documentation and data governance artifacts.

---

# 🚀 Day 3 Completed

## Exploratory Data Analysis (EDA)

Conducted comprehensive exploratory data analysis to uncover trends, patterns, and investment insights across mutual fund performance, investor behavior, AUM growth, SIP inflows, and portfolio allocations.

---

## 📈 NAV Analysis

* Analyzed daily NAV trends across mutual fund schemes from 2022–2026.
* Identified strong NAV growth during the 2023 market bull run.
* Examined average NAV movement and long-term performance trends.
* Visualized fund-wise NAV performance using interactive and static charts.

---

## 💰 AUM Analysis

* Evaluated Assets Under Management (AUM) growth across major fund houses.
* Compared market share distribution among leading Asset Management Companies (AMCs).
* Identified dominant fund houses based on total industry assets.

---

## 📊 SIP & Inflow Analysis

* Analyzed monthly SIP inflow trends from 2022–2025.
* Tracked growth in net inflows across the mutual fund industry.
* Identified periods of accelerated investor participation and capital inflows.
* Created category-wise inflow heatmaps to visualize investment preferences.

---

## 👥 Investor Demographics Analysis

* Studied investor age-group distribution.
* Analyzed SIP investment behavior across demographic segments.
* Examined gender-based participation patterns in mutual fund investments.

---

## 🌍 Geographic Analysis

* Evaluated state-wise SIP contribution patterns.
* Compared investment participation between T30 and B30 cities.
* Identified regions contributing the highest mutual fund investments.

---

## 📈 Industry Growth Analysis

* Analyzed folio count growth from 2022 to 2025.
* Measured growth in retail investor participation.
* Identified long-term industry expansion trends.

---

## 📉 Portfolio & Risk Analysis

* Built mutual fund return correlation matrix for selected schemes.
* Performed sector allocation analysis across equity fund portfolios.
* Examined risk-grade distribution among mutual fund categories.
* Compared category-wise fund counts and return performance.

---

## 🔍 Key Insights Generated

* Large Cap funds delivered the strongest long-term returns among analyzed categories.
* Monthly SIP inflows increased significantly throughout the analysis period.
* Mutual fund folio counts nearly doubled, indicating rising retail participation.
* Banking, IT, Pharma, and Automobile sectors represented major portfolio allocations.
* A small number of fund houses controlled a significant share of industry assets.

---

## 📊 Visualizations Created

Generated **17+ analytical charts** including:

* Daily NAV Trend Analysis
* AUM Growth by Fund House
* SIP Inflow Trend
* Category-wise Inflow Heatmap
* Investor Demographics Analysis
* Geographic Investment Distribution
* Folio Growth Trend
* Correlation Matrix
* Sector Allocation Donut Chart
* Category-wise Returns
* Risk Grade Distribution
* Fund House Market Share
* Monthly Net Inflow Trend

---

### Deliverables

* `03_EDA_Analysis.ipynb`
* 17+ Business Analytics Visualizations
* Exported PNG Charts
* 10 Documented EDA Findings
* EDA Conclusion & Business Insights

---

## 🎯 Learning Outcomes

* API Data Ingestion
* Data Cleaning & Validation
* Data Quality Management
* Relational Database Design
* Star Schema Modeling
* SQLite & SQLAlchemy
* Advanced SQL Analytics
* Exploratory Data Analysis (EDA)
* Financial Data Visualization
* Business Intelligence & Storytelling
* Investor Behavior Analytics
* Portfolio Analysis
* Risk Analysis
* Seaborn & Matplotlib Visualization
* Plotly Interactive Dashboards
* Insight Generation & Reporting
* Git & GitHub Workflow

---
🚀 Day 4 Completed
Fund Performance Analytics

Performed comprehensive performance evaluation of mutual fund schemes using return, risk, and benchmark-based analytics.

📈 Daily Return Analysis
Calculated daily returns for all mutual fund schemes using historical NAV data.
Validated return distributions and identified normal market behavior patterns.
Generated return distribution visualizations for risk assessment.
📊 CAGR Analysis
Computed 1-Year, 3-Year, and 5-Year CAGR for all schemes.
Compared long-term wealth creation potential across mutual fund categories.
Ranked funds based on historical annualized performance.
Identified top-performing funds using CAGR metrics.
⚖️ Risk-Adjusted Performance Analysis
Sharpe Ratio
Calculated Sharpe Ratio using a 6.5% risk-free rate.
Evaluated risk-adjusted returns across all schemes.
Ranked funds based on return generated per unit of risk.
Sortino Ratio
Calculated Sortino Ratio using downside volatility.
Measured fund performance considering only negative-return periods.
Identified funds with superior downside-risk management.
📉 Alpha & Beta Analysis
Performed benchmark-relative analysis against Nifty 100.
Calculated Alpha values to measure excess returns.
Computed Beta values to evaluate market sensitivity.
Generated Alpha-Beta comparison tables and distributions.
📉 Maximum Drawdown Analysis
Calculated maximum drawdown for all schemes.
Measured downside risk during adverse market conditions.
Identified funds with the strongest capital preservation characteristics.
Compared drawdown behavior across categories.
🏆 Fund Scorecard Development

Developed a composite scoring framework based on:

30% – 3-Year Return Rank
25% – Sharpe Ratio Rank
20% – Alpha Rank
15% – Expense Ratio Rank
10% – Maximum Drawdown Rank

Generated standardized fund scores on a 0–100 scale and ranked all mutual fund schemes.

📊 Benchmark Comparison
Compared top-performing funds against Nifty 50 and Nifty 100 benchmarks.
Calculated tracking error for benchmark-relative performance measurement.
Evaluated active fund management effectiveness.
Identified schemes outperforming benchmark indices.
🔍 Key Insights Generated
Top-performing funds consistently delivered strong CAGR and Sharpe Ratio values.
Several schemes generated positive Alpha, indicating benchmark outperformance.
Most funds exhibited Beta values close to 1, reflecting market-linked behavior.
Risk-adjusted performance varied significantly across categories.
Funds with lower drawdowns generally demonstrated superior long-term stability.
The Fund Scorecard successfully identified consistently high-performing schemes.
📊 Visualizations Created

Generated performance analytics visualizations including:

Daily Return Distribution
Top CAGR Funds
Sharpe Ratio Ranking
Sortino Ratio Ranking
Alpha Distribution
Beta Distribution
Maximum Drawdown Analysis
Risk vs Return Scatter Plot
Fund Scorecard Ranking
Benchmark Comparison Analysis
Deliverables
04_Performance_Analytics.ipynb
fund_scorecard.csv
alpha_beta.csv
benchmark_comparison.png
Performance Analytics Insights Report

## 👨‍💻 Author

**Amir Bensekar**

MCA | Data Analytics | Data Engineering

### Skills

Python • SQL • Power BI • Snowflake • dbt • MongoDB • SQLite • Pandas • Plotly • Seaborn
