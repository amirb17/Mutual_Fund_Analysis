# Mutual Fund Analytics, Risk Modeling & Business Intelligence

**Bluestock Fintech Capstone Project**
Author: Amir Bensekar

## Overview

This is an end-to-end Mutual Fund Analytics solution built using Python, SQL, SQLite, and Power BI. It covers the full analytics lifecycle: data ingestion, cleaning and validation, data warehousing, exploratory data analysis (EDA), performance analytics, advanced risk modeling, investor analytics, a fund recommendation engine, and a multi-page business intelligence dashboard.

The project uses historical NAV data (live-fetched via the MFAPI API), AMFI-style industry statistics (AUM, SIP inflows, category flows, folio counts), a 40-scheme performance dataset, ~32,800 simulated investor transactions, portfolio holdings, and benchmark index data to generate insights into mutual fund performance, investor behaviour, portfolio concentration, and market trends.

Full project documentation, including the final report and presentation, is available in this repository:

- **Final_Report.pdf** — 15-20 page final report (executive summary, ETL design, EDA findings, performance analysis, dashboard screenshots, limitations, recommendations)
- **Bluestock_MF_Presentation.pptx** — 12-slide capstone presentation
- **data_dictionary.md** — full column-level documentation for all 10 datasets

## Project Structure

```
Mutual_Fund_Analysis/
├── data/
│   ├── raw/                  # 10 raw input CSVs (fund master, NAV, AUM, SIP, etc.)
│   └── processed/            # Cleaned datasets + SQLite warehouse (bluestock_mf.db)
├── notebooks/                 # Jupyter notebook versions of each pipeline stage
├── Scripts/                   # Python scripts (.py) — ingestion, cleaning, EDA, analytics
│   ├── 1_data_ingestion.py
│   ├── 2_data_cleaning.py
│   ├── 3_EDA_Analysis.py
│   ├── 4_Performance_Analytics.py
│   ├── 6_Advanced Analytics_Risk Metrics.py
│   ├── recommender.py
│   └── run_pipeline.py        # Orchestrates the full pipeline end-to-end
├── sql/
│   ├── schema.sql              # Star-schema warehouse DDL
│   └── quries.sql              # Business-analytics SQL queries
├── reports/
│   ├── EDA_Report_images/      # 17 EDA visualizations
│   ├── Dashboards Images/      # Power BI dashboard page screenshots
│   ├── Bluestock_MF_Dashboard.pbix  # Power BI dashboard
│   ├── Dashboard.pdf            # Exported dashboard PDF
│   ├── fund_scorecard.csv       # Composite ranked fund scorecard (40 schemes)
│   ├── var_cvar_report.csv      # Historical VaR / CVaR (95%) per scheme
│   ├── alpha_beta.csv           # Alpha/beta vs. benchmark per scheme
│   ├── sector_hhi_report.csv    # Sector concentration (HHI) per scheme
│   ├── rolling_sharpe_chart.png
│   └── benchmark_comparison.png
├── data_dictionary.md
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/amirb17/Mutual_Fund_Analysis.git
cd Mutual_Fund_Analysis
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

> The project requires Python 3.10+ and an internet connection for the live NAV data fetch step (MFAPI).

## How to Run the ETL Pipeline

All pipeline stages are designed to be run from the `Scripts/` directory, with raw data read from `../data/raw` and outputs written to `../data/processed` and `../reports`.

### Run the full pipeline end-to-end

```bash
cd Scripts
python run_pipeline.py
```

This sequentially runs:

1. `1_data_ingestion.py` — profiles the 10 raw datasets and fetches live NAV history (6 schemes) from the MFAPI API
2. `2_data_cleaning.py` — cleans, validates, and writes `clean_nav.csv`, `clean_transactions.csv`, `clean_performance.csv`, and loads the SQLite warehouse (`bluestock_mf.db`)
3. `3_EDA_Analysis.py` — generates the 17 EDA visualizations in `reports/EDA_Report_images/`
4. `4_Performance_Analytics.py` — computes CAGR, Sharpe/Sortino ratios, alpha/beta, and the Fund Scorecard
5. `6_Advanced Analytics_Risk Metrics.py` — computes VaR/CVaR, rolling 90-day Sharpe ratio, and sector HHI

### Run individual stages

Each script can also be run independently (e.g., `python "6_Advanced Analytics_Risk Metrics.py"`), provided the cleaned data from earlier stages already exists in `data/processed/`.

### Fund Recommendation Engine

```python
import pandas as pd
from recommender import recommend_funds

scorecard = pd.read_csv("../reports/fund_scorecard.csv")
top_picks = recommend_funds("Moderate", scorecard)  # risk_appetite: e.g. Low / Moderate / High / Very High
print(top_picks)
```

This returns the top-3 schemes matching the given risk grade, ranked by Sharpe ratio.

### SQL Analytics

The star-schema warehouse (`data/processed/bluestock_mf.db`) can be queried directly:

```bash
sqlite3 data/processed/bluestock_mf.db < sql/quries.sql
```

See `sql/schema.sql` for the full table definitions (`dim_fund`, `fact_nav`, `fact_transactions`, `fact_performance`).

## How to Open the Dashboard

The Power BI dashboard file is at `reports/Bluestock_MF_Dashboard.pbix`.

1. Install [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (free, Windows only).
2. Open `reports/Bluestock_MF_Dashboard.pbix`.
3. If prompted, update the data source paths to point to your local `data/processed/bluestock_mf.db` and the relevant CSVs in `data/raw/`.
4. The dashboard has four pages: **Industry Overview**, **Fund Performance**, **Investor Analytics**, and **SIP & Market Trends**.

A static export of all four dashboard pages is available at `reports/Dashboard.pdf` and as individual images in `reports/Dashboards Images/` for quick viewing without Power BI Desktop.

## Dataset Descriptions

The project uses 10 datasets. Full column-level definitions, data types, and sources are documented in [`data_dictionary.md`](./data_dictionary.md). Summary:

| # | Dataset | File | Description |
|---|---------|------|-------------|
| 1 | Fund Master | `01_fund_master.csv` | Scheme-level reference data (AMC, category, expense ratio, risk grade, etc.) |
| 2 | NAV History | `02_nav_history.csv` | Daily NAV for 6 large-cap schemes (Jan 2022–May 2026), fetched live via MFAPI |
| 3 | AUM by Fund House | `03_aum_by_fund_house.csv` | AMC-level Assets Under Management over time |
| 4 | Monthly SIP Inflows | `04_monthly_sip_inflows.csv` | Industry-wide SIP inflow, accounts, AUM, YoY growth |
| 5 | Category Inflows | `05_category_inflows.csv` | Monthly net fund flows by category |
| 6 | Industry Folio Count | `06_industry_folio_count.csv` | Total/equity/debt/hybrid folio counts over time |
| 7 | Scheme Performance | `07_scheme_performance.csv` | Returns, alpha, beta, Sharpe/Sortino, AUM, ratings for 40 schemes |
| 8 | Investor Transactions | `08_investor_transactions.csv` | ~32,800 simulated SIP/Lumpsum/Redemption transactions with demographics |
| 9 | Portfolio Holdings | `09_portfolio_holdings.csv` | Stock-level holdings, sector, and weight per scheme |
| 10 | Benchmark Indices | `10_benchmark_indices.csv` | Historical closing values for benchmark indices |

## Key Outputs & Insights

- **Fund Scorecard** (`reports/fund_scorecard.csv`) — composite 0-100 ranking of all 40 schemes blending 5-year return, Sharpe ratio, alpha, expense ratio, and max drawdown.
- **Risk Analytics** — Historical VaR/CVaR (95%), rolling 90-day Sharpe ratio, and sector concentration (HHI) per scheme.
- **Category Insights** — Small Cap and Mid Cap categories lead 5-year returns; Liquid/Short Duration debt funds show the highest Sharpe ratios due to low volatility.
- **Investor Insights** — SIP inflows and folio counts trend upward across Tier-1/2/3 cities, reflecting growing retail/SIP participation.

See `Final_Report.pdf` for the complete analysis and `Bluestock_MF_Presentation.pptx` for the summary deck.

## Technology Stack

- **Languages/Libraries:** Python, Pandas, NumPy, SciPy, scikit-learn
- **Database:** SQLite, SQL, SQLAlchemy
- **Visualization:** Matplotlib, Plotly, Power BI
- **Tools:** Jupyter Notebook, Git, GitHub

## Author

**Amir Bensekar**
MCA | Data Analytics | Data Engineering | Business Intelligence
[LinkedIn](https://linkedin.com/in/aamirbensekar)
