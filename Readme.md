# 📊 Mutual Fund Analytics, Risk Modeling & Business Intelligence

## 📌 Overview

This project is an end-to-end Mutual Fund Analytics solution built using Python, SQL, SQLite, and Power BI.

The project covers the complete analytics lifecycle, including data ingestion, data validation, data warehousing, exploratory data analysis, performance analytics, financial risk modeling, investor analytics, and business intelligence reporting.

Using historical NAV data, investor transactions, SIP inflows, portfolio holdings, benchmark indices, and fund performance datasets, the project generates actionable insights into mutual fund performance, investor behavior, portfolio concentration, and market trends.

---

## 🎯 Objectives

* Build a scalable analytics pipeline for mutual fund datasets.
* Analyze mutual fund performance using return and risk metrics.
* Study investor behavior and SIP participation patterns.
* Measure downside risk using advanced financial analytics.
* Develop interactive dashboards for business reporting.
* Generate investment recommendations using risk-adjusted metrics.

---

## ⚙️ Project Workflow

### 1. Data Ingestion

* Collected historical NAV data through MFAPI.
* Ingested mutual fund master, transaction, SIP, AUM, portfolio, and benchmark datasets.
* Stored raw datasets for downstream processing.

### 2. Data Cleaning & Validation

* Performed data quality checks and validation.
* Standardized date formats and categorical values.
* Removed duplicates and handled missing values.
* Validated transaction amounts, NAV values, and performance metrics.

### 3. Data Warehousing

* Designed a Star Schema-based analytical model.
* Built a SQLite data warehouse.
* Created fact and dimension tables for efficient analytics.

### 4. SQL Analytics

Performed business-focused SQL analysis including:

* AUM Analysis
* SIP Growth Analysis
* Fund Ranking
* Risk Grade Analysis
* Investor Segmentation
* Transaction Analysis
* Fund House Performance Analysis

### 5. Exploratory Data Analysis (EDA)

Conducted comprehensive analysis on:

* NAV Trends
* AUM Growth
* SIP Inflows
* Investor Demographics
* Geographic Distribution
* Portfolio Allocation
* Industry Growth Trends

Generated 17+ visualizations and business insights.

### 6. Fund Performance Analytics

Implemented advanced fund evaluation metrics:

* CAGR (1Y, 3Y, 5Y)
* Sharpe Ratio
* Alpha
* Beta



Developed a composite Fund Scorecard framework to rank mutual funds using risk-adjusted performance metrics.

### 7. Risk Analytics

Implemented advanced financial risk models:

* Historical Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Rolling 90-Day Sharpe Ratio
* Downside Risk Analysis
* Sector Concentration Analysis (HHI)

### 8. Investor Analytics

Performed investor-focused analysis including:

* Investor Cohort Analysis
* SIP Continuity Analysis
* Age Group Analysis
* State-wise Investment Analysis
* Transaction Behavior Analysis

### 9. Fund Recommendation Engine

Developed a rule-based recommendation system that recommends funds based on:

* Risk Appetite
* Risk Grade
* Sharpe Ratio Ranking

### 10. Business Intelligence Dashboard

Developed a multi-page Power BI Dashboard featuring:

#### Industry Overview

* AUM Trends
* SIP Inflows
* Fund House Analysis
* Industry KPIs

#### Fund Performance

* Risk vs Return Analysis
* Fund Scorecard
* Benchmark Comparison
* Performance Ranking

#### Investor Analytics

* Investor Demographics
* Geographic Analysis
* Transaction Insights

#### SIP & Market Trends

* SIP Inflow vs Nifty Analysis
* Category Inflow Heatmaps
* Market Trend Analysis

---

## 📈 Key Business Insights

* Identified top-performing funds using risk-adjusted performance metrics.
* Measured downside risk using VaR and CVaR methodologies.
* Evaluated investor participation and SIP behavior patterns.
* Analyzed portfolio diversification through HHI concentration analysis.
* Identified high-value investor cohorts.
* Built a recommendation engine for investment decision support.

---

## 🛠 Technology Stack

### Programming

* Python
* Pandas
* NumPy

### Database

* SQLite
* SQL
* SQLAlchemy

### Visualization

* Matplotlib
* Plotly
* Power BI

### Development Tools

* Jupyter Notebook
* Git
* GitHub

---

## 📂 Deliverables

* Cleaned & Validated Datasets
* SQLite Data Warehouse
* SQL Analytics Queries
* EDA Reports & Visualizations
* Fund Performance Analytics Reports
* Power BI Dashboard (.pbix)
* Risk Analytics Reports
* Fund Recommendation Engine
* Business Insights Documentation

---

## 👨‍💻 Author

**Amir Bensekar**

MCA | Data Analytics | Business Intelligence | Data Engineering

### Skills

Python • SQL • Power BI • SQLite • Pandas • NumPy • Data Analytics • Data Engineering • Financial Analytics • Risk Modeling • Business Intelligence • Data Visualization • ETL/ELT
