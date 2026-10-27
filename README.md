# Walmart Sales Analysis Dashboard

## Project Overview

The Walmart Sales Analysis Dashboard is a beginner-friendly data analytics project built using Python. It analyzes retail transaction data to identify sales trends, compare product categories, understand payment methods, and explore sales performance across cities.

The project includes data cleaning, exploratory analysis, visualizations, and an interactive dashboard.

## Objectives

- Analyze overall recorded sales and transaction values.
- Identify top-performing product categories.
- Compare sales across different cities.
- Understand customer payment method preferences.
- Analyze monthly sales trends.
- Create an interactive dashboard with filters and downloadable reports.

## Technologies Used

- **Python 3.14** — programming language
- **Pandas** — data cleaning and analysis
- **Matplotlib** — data visualization
- **Streamlit** — interactive dashboard
- **CSV** — dataset storage and analysis reports

## Project Structure

```text
WalmartSalesProject/
├── data/
│   ├── walmart_sales.csv
│   └── walmart_sales_cleaned.csv
├── notebooks/
├── outputs/
│   ├── sales_by_category.csv
│   ├── sales_by_city.csv
│   ├── payment_method_counts.csv
│   ├── monthly_sales.csv
│   └── sales_summary.csv
├── src/
│   ├── explore_data.py
│   ├── data_quality.py
│   ├── clean_data.py
│   ├── sales_analysis.py
│   ├── create_charts.py
│   └── dashboard.py
└── README.md
```

## Installation and Execution

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd WalmartSalesProject
```

### 2. Create and activate a virtual environment

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install pandas matplotlib streamlit
```

### 4. Run data cleaning

```powershell
python src/clean_data.py
```

### 5. Run sales analysis

```powershell
python src/sales_analysis.py
```

### 6. Generate charts

```powershell
python src/create_charts.py
```

### 7. Launch the dashboard

```powershell
python -m streamlit run src/dashboard.py
```

## Dashboard Features

- Key sales performance indicators
- Product category and city filters
- Payment method analysis
- Monthly sales trend visualization
- Interactive sales charts
- Filtered transaction table
- CSV download functionality

## Dataset

The project uses a Walmart-style retail transaction dataset containing invoice details, cities, product categories, unit prices, quantities, transaction totals, dates, payment methods, and customer ratings.

The dataset is used for educational analysis and is not verified official Walmart corporate data.

## Future Enhancements

- Add SQL queries for business analysis.
- Develop sales forecasting using machine learning.
- Add customer segmentation.
- Improve dashboard design and reporting.
- Deploy the dashboard online.

## Author

Developed as a hands-on Python data analytics project to practice data cleaning, exploratory data analysis, visualization, and dashboard development.   