
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Find project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "outputs"

# Load analysis reports
category_sales = pd.read_csv(OUTPUT_DIR / "sales_by_category.csv")
city_sales = pd.read_csv(OUTPUT_DIR / "sales_by_city.csv")
monthly_sales = pd.read_csv(OUTPUT_DIR / "monthly_sales.csv")

# Chart 1: Sales by product category
plt.figure(figsize=(10, 6))
plt.bar(
    category_sales.iloc[:, 0],
    category_sales.iloc[:, 1]
)
plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Recorded Sales")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sales_by_category.png", dpi=150)
plt.close()

# Chart 2: Sales by city
plt.figure(figsize=(8, 5))
plt.bar(
    city_sales.iloc[:, 0],
    city_sales.iloc[:, 1]
)
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Recorded Sales")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sales_by_city.png", dpi=150)
plt.close()

# Chart 3: Monthly sales trend
plt.figure(figsize=(8, 5))
plt.plot(
    monthly_sales.iloc[:, 0],
    monthly_sales.iloc[:, 1],
    marker="o"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Recorded Sales")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_sales_trend.png", dpi=150)
plt.close()

print("All three charts created successfully!")
print("Check the outputs folder.")
