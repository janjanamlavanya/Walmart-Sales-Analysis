
from pathlib import Path
import pandas as pd

# 1. Find the project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# 2. Load the dataset
DATA_PATH = PROJECT_DIR / "data" / "walmart_sales.csv"
df = pd.read_csv(DATA_PATH)

# 3. Display dataset size
print("\n--- DATASET SIZE ---")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# 4. Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# 5. Check duplicate rows
print("\n--- DUPLICATE ROWS ---")
print("Duplicate rows:", df.duplicated().sum())

# 6. Check column data types
print("\n--- COLUMN DATA TYPES ---")
print(df.dtypes)

# 7. Display numerical statistics
print("\n--- NUMERICAL SUMMARY ---")
print(df.describe())

print("\nData quality check completed!")
