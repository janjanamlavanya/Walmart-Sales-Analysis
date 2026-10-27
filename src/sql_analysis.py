
from pathlib import Path
import sqlite3
import pandas as pd

# 1. Find project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "walmart_sales_cleaned.csv"
DB_PATH = PROJECT_DIR / "data" / "walmart_sales.db"
OUTPUT_DIR = PROJECT_DIR / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 2. Load the cleaned CSV
df = pd.read_csv(DATA_PATH)

# 3. Create a SQLite database and table
with sqlite3.connect(DB_PATH) as connection:
    df.to_sql("sales", connection, if_exists="replace", index=False)

    # Query 1: Total sales and number of transactions
    print("\n--- OVERALL SALES ---")
    query = """
        SELECT
            ROUND(SUM(total), 2) AS total_sales,
            COUNT(DISTINCT invoice_id) AS transactions,
            ROUND(AVG(total), 2) AS average_transaction
        FROM sales;
    """
    print(pd.read_sql_query(query, connection))

    # Query 2: Sales by product category
    print("\n--- SALES BY CATEGORY ---")
    query = """
        SELECT
            product_line,
            ROUND(SUM(total), 2) AS sales
        FROM sales
        GROUP BY product_line
        ORDER BY sales DESC;
    """
    category_results = pd.read_sql_query(query, connection)
    print(category_results)
    category_results.to_csv(
        OUTPUT_DIR / "sql_sales_by_category.csv", index=False
    )

    # Query 3: Sales by city
    print("\n--- SALES BY CITY ---")
    query = """
        SELECT
            city,
            ROUND(SUM(total), 2) AS sales
        FROM sales
        GROUP BY city
        ORDER BY sales DESC;
    """
    city_results = pd.read_sql_query(query, connection)
    print(city_results)
    city_results.to_csv(
        OUTPUT_DIR / "sql_sales_by_city.csv", index=False
    )

    # Query 4: Payment method usage
    print("\n--- PAYMENT METHODS ---")
    query = """
        SELECT
            payment_method,
            COUNT(*) AS transactions
        FROM sales
        GROUP BY payment_method
        ORDER BY transactions DESC;
    """
    print(pd.read_sql_query(query, connection))

print("\nSQL analysis completed successfully!")
print("Database saved to:", DB_PATH)
