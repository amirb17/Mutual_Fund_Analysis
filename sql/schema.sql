CREATE TABLE dim_fund(
    amfi_code TEXT PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    launch_date date,
    benchmark TEXT,
    expense_ration_pct FLOAT,
    exit_load_pct FLOAT,
    min_sip_amount INTEGER,
    min_lumpsum_amount INTEGER,
    fund_manager TEXT,
    risk_category TEXT,
    sebi_category_code TEXT
);

CREATE TABLE dim_date(
    amfi_code TEXT,
    ddate date,
    nav FLOAT,
    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(nav)
    REFERENCES fact_nav(nav)
);
 CREATE TABLE fact_nav(
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code TEXT FK,
    nav_date DATE, 
    nav REAL,
    daily_return REAL,
    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
 );

 CREATE TABLE fact_transactions(
    investor_id TEXT PRIMARY KEY,
    transaction_date DATE,
    amfi_code TEXT,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT
    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
 );

 CREATE TABLE fact_performance(
    amfi_code TEXT,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    plan TEXT,
    return_1yr_pct FLOAT,
    return_3yr_pct FLOAT,
    return_5yr_pct FLOAT,
    benchmark_3yr_pct TEXT,
    alpha TEXT,
    beta TEXT,
    sharpe_ratio TEXT,
    sortino_ratio TEXT,
    std_dev_ann_pct TEXT,
    max_drawdown_pct TEXT,
    aum_crore TEXT,
    expense_ratio_pct TEXT,
    morningstar_rating TEXT,
    risk_grade TEXT
    FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
 );

 CREATE TABLE fact_aum(
    ddate date,
    fund_house TEXT,
    aum_lakh_crore TEXT,
    aum_crore TEXT,
    num_schemes TEXT
 );
 




