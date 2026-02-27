# 📊 Finance Analytics Dashboard (Power BI)

![Dashboard Preview](dashboard_preview.png)

## 🧾 Project Overview

A complete Finance Analytics Dashboard built in Power BI, designed to provide actionable business insights across revenue, expenses, profit margins, and sales forecasting.

This project bridges **6 years of Accounts Management experience** with modern data analytics — turning raw financial data into executive-level decision-making visuals.

---

## 🎯 Business Problem

Finance teams often struggle to get a clear, real-time picture of:
- Where money is being made and lost
- Which segments drive the highest costs
- How profit margins are trending over time
- What sales will look like in the next 6 months

This dashboard answers all of these questions in a single view.

---

## 📌 Key KPIs

| Metric | Value |
|---|---|
| Total Sales | 118.73M |
| Total Profit | 16.89M |
| Total COGS | 101.83M |
| Average Profit Margin | 27.90% |

---

## 📈 Dashboard Visuals

| Visual | Type | Insight |
|---|---|---|
| Revenue vs Expense by Month | Clustered Bar Chart | Sales consistently exceeds COGS across all months |
| Profit Margin % Trends | Line Chart | Margin stays between 27–29%; dips in November |
| Cash Flow by Month | Waterfall Chart | Steady profit accumulation — no loss months |
| Department-wise Cost Analysis | Treemap | Government segment has highest operational cost |
| Sales Forecast (Next 6 Months) | Line + Forecast | Stable sales projected at 8–10M/month into 2015 |

---

## 🔍 Key Business Insights

- **Q4 Seasonality**: Sales peak significantly in October–December
- **Government Dominates Costs**: Largest segment by COGS — requires cost optimization review
- **Healthy Margins**: 27–29% profit margin maintained consistently across 2013–2014
- **No Loss Months**: Every month contributed positively to cumulative profit
- **Forecast**: Sales expected to stabilize around 8–10M/month for first half of 2015

---

## 🛠️ Tools & Skills Used

- **Python (pandas)** — Data cleaning, null handling, feature engineering
- **Power BI Desktop** — Dashboard design, DAX, forecasting
- **Excel** — Raw data source

---

## 📂 Project Structure

```
Project 1/
│
├── Financial Sample.xlsx      # Raw dataset (Microsoft Financial Sample)
├── finance_clean.csv          # Cleaned dataset (output of Python script)
├── Project 1.py               # Python data cleaning script
├── Finance_Dashboard.pbix     # Power BI Dashboard file
└── dashboard_preview.png      # Dashboard screenshot
```

---

## ⚙️ Data Cleaning Steps (Python)

- Stripped leading/trailing spaces from column names
- Filled 53 null values in `Discount Band` column with `'None'`
- Engineered `Profit Margin %` column: `(Profit / Sales) * 100`
- Created `Month-Year` column for clean time-axis display in Power BI

---

## 💡 How to Use

1. Clone this repository
2. Open `Finance_Dashboard.pbix` in Power BI Desktop
3. If data connection breaks, point it to `finance_clean.csv` in the same folder
4. Use the **Year slicer** (top right) to filter by 2013 or 2014

---

## 👤 About

Built by **Syed Kafeel Ahamed** — transitioning from 6 years as an Accounts Manager into Data Science & Analytics.

This project demonstrates that domain expertise + technical skills = better data products.

📧 Connect with me on [LinkedIn](https://www.linkedin.com/in/syed-kafeel-ahamed-ab465036b)
