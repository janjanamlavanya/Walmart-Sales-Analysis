
from pathlib import Path
import pandas as pd

# 1. Find the project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# 2. Load the cleaned dataset
DATA_PATH = PROJECT_DIR / "data" / "walmart_sales_cleaned.csv"
OUTPUT_DIR = PROJECT_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH)
df["date"] = pd.to_datetime(df["date"], errors="raise")

# 3. Overall sales summary
total_sales = df["total"].sum()
average_sale = df["total"].mean()
total_transactions = df["invoice_id"].nunique()
total_units = df["quantity"].sum()

print("\n--- OVERALL SALES SUMMARY ---")
print(f"Total recorded sales: {total_sales:,.2f}")
print(f"Average transaction value: {average_sale:,.2f}")
print(f"Unique invoices: {total_transactions}")
print(f"Total units sold: {total_units}")

# 4. Sales by product category
category_sales = (
    df.groupby("product_line")["total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- SALES BY PRODUCT CATEGORY ---")
print(category_sales)

category_sales.to_csv(OUTPUT_DIR / "sales_by_category.csv")

# 5. Sales by city
city_sales = (
    df.groupby("city")["total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- SALES BY CITY ---")
print(city_sales)

city_sales.to_csv(OUTPUT_DIR / "sales_by_city.csv")

# 6. Most commonly used payment methods
payment_counts = df["payment_method"].value_counts()

print("\n--- PAYMENT METHOD COUNTS ---")
print(payment_counts)

payment_counts.to_csv(OUTPUT_DIR / "payment_method_counts.csv")

# 7. Monthly sales trend
df["month"] = df["date"].dt.to_period("M").astype(str)

monthly_sales = (
    df.groupby("month")["total"]
    .sum()
    .sort_index()
)

print("\n--- MONTHLY SALES ---")
print(monthly_sales)

monthly_sales.to_csv(OUTPUT_DIR / "monthly_sales.csv")

# 8. Save overall summary
summary = pd.DataFrame({
    "metric": [
        "Total recorded sales",
        "Average transaction value",
        "Unique invoices",
        "Total units sold"
    ],
    "value": [
        total_sales,
        average_sale,
        total_transactions,
        total_units
    ]
})

summary.to_csv(OUTPUT_DIR / "sales_summary.csv", index=False)

print("\nAll sales analyses completed!")
print("Reports saved in:", OUTPUT_DIR)
