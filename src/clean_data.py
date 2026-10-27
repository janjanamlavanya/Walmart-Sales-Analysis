
from pathlib import Path
import pandas as pd

# Find the project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Input and output paths
INPUT_PATH = PROJECT_DIR / "data" / "walmart_sales.csv"
OUTPUT_PATH = PROJECT_DIR / "data" / "walmart_sales_cleaned.csv"

# Load the original dataset
df = pd.read_csv(INPUT_PATH)

print("Original rows:", len(df))

# Remove exact duplicate rows
duplicate_count = df.duplicated().sum()
df = df.drop_duplicates()

print("Duplicate rows removed:", duplicate_count)

# Convert the date column to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Check missing values after date conversion
print("\nMissing values by column:")
print(df.isnull().sum())

# Save the cleaned dataset
df.to_csv(OUTPUT_PATH, index=False)

print("\nCleaned rows:", len(df))
print("Cleaned dataset saved to:", OUTPUT_PATH)
