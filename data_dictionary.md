# Data Dictionary

## Mutual Fund Analysis Project

### Overview

This document describes all datasets used in the Mutual Fund Analysis project, including column definitions, data types, business meanings, and data sources.

---

# Dataset 1: Fund Master

**File:** `01_fund_master.csv`

**Description:** Master reference table containing mutual fund scheme details.

| Column Name        | Data Type | Description                                |
| ------------------ | --------- | ------------------------------------------ |
| amfi_code          | INTEGER   | Unique AMFI scheme identifier              |
| fund_house         | TEXT      | Asset Management Company (AMC)             |
| scheme_name        | TEXT      | Mutual fund scheme name                    |
| category           | TEXT      | Fund category (Equity, Debt, Hybrid, etc.) |
| sub_category       | TEXT      | Detailed fund classification               |
| plan               | TEXT      | Plan type (Direct, Regular, Growth, etc.)  |
| launch_date        | DATE      | Scheme launch date                         |
| benchmark          | TEXT      | Benchmark index used for comparison        |
| expense_ratio_pct  | FLOAT     | Expense ratio charged by the fund (%)      |
| exit_load_pct      | FLOAT     | Exit load charged on redemption (%)        |
| min_sip_amount     | INTEGER   | Minimum SIP investment amount              |
| min_lumpsum_amount | INTEGER   | Minimum lump sum investment amount         |
| fund_manager       | TEXT      | Name of fund manager                       |
| risk_category      | TEXT      | Risk classification                        |
| sebi_category_code | TEXT      | SEBI category code                         |

**Source:** AMFI Scheme Master Data

---

# Dataset 2: NAV History

**File:** `02_nav_history.csv`

**Description:** Historical Net Asset Value (NAV) data for selected mutual fund schemes.

| Column Name | Data Type | Description        |
| ----------- | --------- | ------------------ |
| amfi_code   | INTEGER   | AMFI scheme code   |
| date        | DATE      | NAV reporting date |
| nav         | FLOAT     | Net Asset Value    |

### Data Collection Method

NAV history was fetched programmatically using Python from the MFAPI endpoint:

https://api.mfapi.in/mf/{scheme_code}

Example Schemes:

* HDFC Top 100 (125497)
* SBI Bluechip (119551)
* ICICI Bluechip (120503)
* Nippon Large Cap (118632)
* Axis Bluechip (119092)
* Kotak Bluechip (120841)

Each scheme's historical NAV data was downloaded, converted to CSV, and consolidated into a single dataset.

**Source:** MFAPI Historical NAV Data

---

# Dataset 3: AUM by Fund House

**File:** `03_aum_by_fund_house.csv`

**Description:** Assets Under Management statistics at AMC level.

| Column Name    | Data Type | Description               |
| -------------- | --------- | ------------------------- |
| date           | DATE      | Reporting date            |
| fund_house     | TEXT      | Asset Management Company  |
| aum_lakh_crore | FLOAT     | AUM in lakh crore         |
| aum_crore      | INTEGER   | AUM in crore              |
| num_schemes    | INTEGER   | Number of schemes managed |

**Source:** Industry AUM Statistics

---

# Dataset 4: Monthly SIP Inflows

**File:** `04_monthly_sip_inflows.csv`

**Description:** Monthly SIP investment trends.

| Column Name               | Data Type | Description                 |
| ------------------------- | --------- | --------------------------- |
| month                     | DATE      | Reporting month             |
| sip_inflow_crore          | INTEGER   | SIP inflow amount (₹ crore) |
| active_sip_accounts_crore | FLOAT     | Active SIP accounts         |
| new_sip_accounts_lakh     | FLOAT     | New SIP registrations       |
| sip_aum_lakh_crore        | FLOAT     | SIP AUM                     |
| yoy_growth_pct            | FLOAT     | Year-over-year SIP growth   |

**Source:** AMFI SIP Statistics

---

# Dataset 5: Category Inflows

**File:** `05_category_inflows.csv`

**Description:** Monthly category-wise net fund flows.

| Column Name      | Data Type | Description       |
| ---------------- | --------- | ----------------- |
| month            | DATE      | Reporting month   |
| category         | TEXT      | Fund category     |
| net_inflow_crore | FLOAT     | Net inflow amount |

**Source:** Category Flow Reports

---

# Dataset 6: Industry Folio Count

**File:** `06_industry_folio_count.csv`

**Description:** Industry-wide mutual fund folio statistics.

| Column Name         | Data Type | Description           |
| ------------------- | --------- | --------------------- |
| month               | DATE      | Reporting month       |
| total_folios_crore  | FLOAT     | Total folio count     |
| equity_folios_crore | FLOAT     | Equity fund folios    |
| debt_folios_crore   | FLOAT     | Debt fund folios      |
| hybrid_folios_crore | FLOAT     | Hybrid fund folios    |
| others_folios_crore | FLOAT     | Other category folios |

**Source:** Industry Folio Reports

---

# Dataset 7: Scheme Performance

**File:** `07_scheme_performance.csv`

**Description:** Fund performance and risk metrics.

| Column Name        | Data Type | Description                      |
| ------------------ | --------- | -------------------------------- |
| amfi_code          | INTEGER   | Scheme code                      |
| scheme_name        | TEXT      | Mutual fund scheme               |
| fund_house         | TEXT      | Asset Management Company         |
| category           | TEXT      | Fund category                    |
| plan               | TEXT      | Fund plan                        |
| return_1yr_pct     | FLOAT     | One-year return (%)              |
| return_3yr_pct     | FLOAT     | Three-year annualized return (%) |
| return_5yr_pct     | FLOAT     | Five-year annualized return (%)  |
| benchmark_3yr_pct  | FLOAT     | Benchmark return (%)             |
| alpha              | FLOAT     | Excess return over benchmark     |
| beta               | FLOAT     | Relative volatility measure      |
| sharpe_ratio       | FLOAT     | Risk-adjusted return metric      |
| sortino_ratio      | FLOAT     | Downside risk-adjusted return    |
| std_dev_ann_pct    | FLOAT     | Annualized volatility            |
| max_drawdown_pct   | FLOAT     | Maximum drawdown                 |
| aum_crore          | INTEGER   | Assets under management          |
| expense_ratio_pct  | FLOAT     | Expense ratio                    |
| morningstar_rating | INTEGER   | Morningstar rating (1–5)         |
| risk_grade         | TEXT      | Risk classification              |

**Source:** Scheme Performance Dataset

---

# Dataset 8: Investor Transactions

**File:** `08_investor_transactions.csv`

**Description:** Simulated investor transaction records.

| Column Name        | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | TEXT      | Unique investor identifier |
| transaction_date   | DATE      | Transaction date           |
| amfi_code          | INTEGER   | Scheme code                |
| transaction_type   | TEXT      | SIP / Lumpsum / Redemption |
| amount_inr         | INTEGER   | Transaction amount         |
| state              | TEXT      | Investor state             |
| city               | TEXT      | Investor city              |
| city_tier          | TEXT      | Tier classification        |
| age_group          | TEXT      | Investor age segment       |
| gender             | TEXT      | Investor gender            |
| annual_income_lakh | FLOAT     | Annual income in lakhs     |
| payment_mode       | TEXT      | Mode of payment            |
| kyc_status         | TEXT      | KYC verification status    |

**Source:** Simulated Investor Data

---

# Dataset 9: Portfolio Holdings

**File:** `09_portfolio_holdings.csv`

**Description:** Fund portfolio composition.

| Column Name       | Data Type | Description              |
| ----------------- | --------- | ------------------------ |
| amfi_code         | INTEGER   | Scheme code              |
| stock_symbol      | TEXT      | Stock ticker             |
| stock_name        | TEXT      | Company name             |
| sector            | TEXT      | Industry sector          |
| weight_pct        | FLOAT     | Portfolio weight (%)     |
| market_value_cr   | FLOAT     | Market value (crore)     |
| current_price_inr | FLOAT     | Current stock price      |
| portfolio_date    | DATE      | Portfolio reporting date |

**Source:** Portfolio Holdings Dataset

---

# Dataset 10: Benchmark Indices

**File:** `10_benchmark_indices.csv`

**Description:** Historical benchmark index values.

| Column Name | Data Type | Description         |
| ----------- | --------- | ------------------- |
| date        | DATE      | Trading date        |
| index_name  | TEXT      | Benchmark index     |
| close_value | FLOAT     | Closing index value |

**Source:** Benchmark Market Data

---

# Data Quality Checks

* Converted date columns to datetime format.
* Removed duplicate records.
* Sorted NAV history by scheme and date.
* Forward-filled NAV values for non-trading days.
* Validated NAV values greater than zero.
* Standardized transaction types.
* Validated transaction amounts.
* Verified KYC status values.
* Converted return metrics to numeric data types.
* Flagged negative Sharpe ratios.
* Validated expense ratio range (0.1% – 2.5%).
* Verified AMFI code consistency across datasets.

---

## Author

**Amir Bensekar**
MCA | Data Analytics | Data Engineering
