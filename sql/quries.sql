--1) Top 5 funds by AUM
select fund_house from fact_performance order by aum_crore limit 5;

--2) Average nav by month
SELECT strftime('%m', date) AS month,
       AVG(nav) AS avg_nav
FROM dim_nav
GROUP BY strftime('%m', date)
ORDER BY month;

--3) SIP YoY growth
select strftime('%Y', transaction_date) AS year,
	sum(amount_inr) as SIP
	from fact_transaction
	GROUP by strftime('%Y', transaction_date);
	
--4) Transactions by state

select state, count(*) as transactions from fact_transaction group by state order by state;

--5) Funds with expense_ratio < 1%

select fund_house from fact_performance where expense_ratio_pct<1 group by fund_house;

--6)avg return 1yr,3yr,5yt pct according to risk_grade
select risk_grade as Risk_Grade,
	round(avg(return_1yr_pct),2) as AVG_return_1yr_pct,
	round(avg(return_3yr_pct),2) as AVG_return_3yr_pct,
	round(avg(return_5yr_pct),2) as AVG_return_5yr_pct
from fact_performance
group by risk_grade;

--7)Transaction type stats
select transaction_type as Transaction_types,
count(*) as Total_transactions,
round(sum(amount_inr),2) as Total_amount,
round(avg(amount_inr),2) as Average_transaction_amount
from fact_transaction
group by transaction_type
order by Total_amount desc;

--8)Category wise avg return
select category,
count(*) as total_count,
round(avg(return_1yr_pct),2) as Avg_1yr_pct,
round(avg(return_3yr_pct),2) as Avg_3yr_pct,
round(avg(return_5yr_pct),2) as Avg_5yr_pct
from fact_performance
group by category
order by total_count desc;

--9)Average Expense Ratio by Category
SELECT
    category,
    ROUND(AVG(expense_ratio_pct),2) AS avg_expense_ratio
FROM fact_performance
GROUP BY category
ORDER BY avg_expense_ratio DESC;

--10)Fund House Performance Comparison
SELECT
    fund_house,
    ROUND(AVG(return_5yr_pct),2) AS avg_5yr_return
FROM fact_performance
GROUP BY fund_house
ORDER BY avg_5yr_return DESC;

