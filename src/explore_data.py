
from pathlib import Path
import pandas as pd

# Find the main project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Find the sales dataset
DATA_PATH = PROJECT_DIR / "data" / "walmart_sales.csv"

# Load the CSV file into a DataFrame
df = pd.read_csv(DATA_PATH)

# Display the first five rows
print("\n--- FIRST FIVE ROWS ---")
print(df.head())

# Display the number of rows and columns
print("\n--- DATASET SHAPE ---")
print(df.shape)

# Display all column names
print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

# Display information about the dataset
print("\n--- DATASET INFORMATION ---")
df.info()
