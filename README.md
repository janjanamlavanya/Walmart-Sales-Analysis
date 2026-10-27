# Walmart Sales Analysis Dashboard

A Python-based retail analytics project that transforms Walmart-style transaction data into actionable business insights using data cleaning, exploratory data analysis, SQL analysis, data visualization, and an interactive Streamlit dashboard.

## Table of Contents

- [Project Overview](#project-overview)
- [Business Objectives](#business-objectives)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [How to Run the Project](#how-to-run-the-project)
- [Business Questions Answered](#business-questions-answered)
- [Dataset](#dataset)
- [Future Enhancements](#future-enhancements)
- [Author](#author)

## Project Overview

The Walmart Sales Analysis Dashboard is an end-to-end data analytics project designed to explore retail transaction data and identify patterns in sales performance.

The project covers the data analytics workflow, from data quality checks and data cleaning to business analysis, SQL queries, visualizations, and interactive dashboard development.

The analysis focuses on understanding product category performance, sales distribution across cities, payment method preferences, and monthly sales trends.

## Business Objectives

- Analyze recorded sales and transaction values.
- Identify top-performing product categories.
- Compare sales performance across cities.
- Examine customer payment method preferences.
- Explore monthly sales trends.
- Assess data quality and prepare datasets for analysis.
- Present insights through interactive visualizations and downloadable reports.

## Key Features

### Data Cleaning and Quality

- Inspect and validate retail transaction data.
- Prepare cleaned datasets for downstream analysis.
- Generate data quality reports.

### Exploratory Data Analysis

- Analyze sales and transaction patterns.
- Compare product categories and city-level performance.
- Explore monthly trends and payment methods.

### SQL Analysis

- Perform SQL-based sales analysis.
- Generate category-level and city-level sales reports.

### Data Visualization

- Generate charts using Matplotlib.
- Export analysis results and visualizations for reporting.

### Interactive Dashboard

- Display key sales performance indicators.
- Filter data by product category and city.
- Explore payment method distributions.
- Visualize monthly sales trends.
- Review filtered transaction records.
- Download filtered data as CSV files.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.14 | Core programming language |
| Pandas | Data cleaning and analysis |
| Matplotlib | Data visualization |
| Streamlit | Interactive dashboard |
| SQL | Business-oriented data analysis |
| CSV | Dataset storage and report exports |
| Git and GitHub | Version control and project hosting |

## Project Structure

```text
WalmartSalesProject/
├── data/
│   ├── walmart_sales.csv
│   └── walmart_sales_cleaned.csv
├── notebooks/
├── outputs/
│   ├── monthly_sales.csv
│   ├── monthly_sales_trend.png
│   ├── payment_method_counts.csv
│   ├── sales_by_category.csv
│   ├── sales_by_category.png
│   ├── sales_by_city.csv
│   ├── sales_by_city.png
│   ├── sales_summary.csv
│   ├── sql_sales_by_category.csv
│   └── sql_sales_by_city.csv
├── src/
│   ├── clean_data.py
│   ├── create_charts.py
│   ├── dashboard.py
│   ├── data_quality.py
│   ├── explore_data.py
│   ├── sales_analysis.py
│   └── sql_analysis.py
├── .gitignore
├── README.md
└── requirements.txt
```

*The tree highlights the main project files; additional generated outputs may be present.*

## Installation and Setup

### Prerequisites

- Python 3.14, matching the development environment
- Git
- Visual Studio Code or another Python-compatible editor

### 1. Clone the repository

```bash
git clone https://github.com/janjanamlavanya/Walmart-Sales-Analysis.git
cd Walmart-Sales-Analysis
```

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
py -3.14 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Run data quality checks and cleaning

```powershell
python src/data_quality.py
python src/clean_data.py
```

### 5. Run exploratory analysis

```powershell
python src/explore_data.py
```

### 6. Run sales analysis

```powershell
python src/sales_analysis.py
```

### 7. Run SQL analysis

```powershell
python src/sql_analysis.py
```

### 8. Generate charts

```powershell
python src/create_charts.py
```

### 9. Launch the dashboard

```powershell
python -m streamlit run src/dashboard.py
```

Streamlit will provide a local URL in the terminal. Open that URL in your browser to explore the dashboard.

**Note:** Run the scripts in the order required by their data dependencies. If a script uses a database or generated file, ensure that the required input has been created first.

## Business Questions Answered

This project is designed to investigate questions such as:

1. What is the total recorded sales value?
2. Which product categories contribute the most to sales?
3. How does sales performance vary across cities?
4. Which payment methods are used most frequently?
5. How do sales change from month to month?
6. What data quality issues need to be addressed before analysis?

The answers should be interpreted using the actual outputs generated by the project.

## Dashboard Preview

Add screenshots of your running Streamlit dashboard here to help visitors understand the interface and visualizations.

Suggested screenshots:

- Dashboard overview and key performance indicators
- Sales by product category
- Sales comparison across cities
- Monthly sales trends
- Payment method analysis

Save the screenshots in a dedicated folder such as `screenshots/` and embed them using relative image paths once they are available.

## Dataset

The project uses a Walmart-style retail transaction dataset containing fields such as invoice details, cities, product categories, unit prices, quantities, transaction totals, dates, payment methods, and customer ratings.

**Data disclaimer:** The dataset is used for educational analysis and is not verified official Walmart corporate data.

The CSV files are included in the repository for reproducibility. If the dataset is subject to licensing or redistribution restrictions, replace it with a permitted sample or provide instructions for obtaining it.

## Future Enhancements

- Expand SQL analysis with additional business queries.
- Develop and evaluate a sales forecasting model.
- Introduce customer segmentation.
- Improve dashboard design and reporting.
- Add automated data validation and testing.
- Document analytical findings with verified metrics.
- Explore deployment options for online dashboard access.

## Author

Developed as a hands-on Python data analytics project to practice data preparation, exploratory data analysis, SQL, visualization, and interactive dashboard development.

---

**If you find this project useful, consider starring the repository.**
