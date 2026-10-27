
from pathlib import Path
import pandas as pd
import streamlit as st

# 1. Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "walmart_sales_cleaned.csv"

# 2. Page settings
st.set_page_config(
    page_title="Walmart Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# 3. Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"], errors="raise")
    return df

df = load_data()

# 4. Dashboard heading
st.title("📊 Walmart Sales Analytics Dashboard")
st.caption("Explore retail sales, product categories, cities, and payment methods.")

# 5. Sidebar filters
st.sidebar.header("Filter Sales")

categories = sorted(df["product_line"].dropna().unique())
cities = sorted(df["city"].dropna().unique())
payments = sorted(df["payment_method"].dropna().unique())

selected_categories = st.sidebar.multiselect(
    "Product Categories",
    categories,
    default=categories
)

selected_cities = st.sidebar.multiselect(
    "Cities",
    cities,
    default=cities
)

selected_payments = st.sidebar.multiselect(
    "Payment Methods",
    payments,
    default=payments
)

min_date = df["date"].min().date()
max_date = df["date"].max().date()

selected_dates = st.sidebar.date_input(
    "Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# 6. Apply filters
filtered_df = df[
    df["product_line"].isin(selected_categories)
    & df["city"].isin(selected_cities)
    & df["payment_method"].isin(selected_payments)
].copy()

if isinstance(selected_dates, (tuple, list)) and len(selected_dates) == 2:
    start_date, end_date = selected_dates
    filtered_df = filtered_df[
        filtered_df["date"].dt.date.between(start_date, end_date)
    ]
elif isinstance(selected_dates, (tuple, list)) and len(selected_dates) == 1:
    selected_date = selected_dates[0]
    filtered_df = filtered_df[
        filtered_df["date"].dt.date == selected_date
    ]
else:
    filtered_df = filtered_df[
        filtered_df["date"].dt.date == selected_dates
    ]

# 7. Calculate dashboard metrics
total_sales = filtered_df["total"].sum()
average_sale = filtered_df["total"].mean()
transaction_count = filtered_df["invoice_id"].nunique()
total_units = filtered_df["quantity"].sum()

# 8. Display KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Recorded Sales", f"{total_sales:,.2f}")
col2.metric("Unique Invoices", f"{transaction_count:,}")
col3.metric(
    "Average Transaction Value",
    f"{average_sale:,.2f}" if pd.notna(average_sale) else "0.00"
)
col4.metric("Units Sold", f"{total_units:,}")

st.divider()

if filtered_df.empty:
    st.warning("No sales records match the selected filters.")
else:
    # 9. Sales by product category
    st.subheader("Sales by Product Category")
    category_sales = (
        filtered_df.groupby("product_line")["total"]
        .sum()
        .sort_values(ascending=False)
    )
    st.bar_chart(category_sales)

    # 10. Sales by city
    st.subheader("Sales by City")
    city_sales = (
        filtered_df.groupby("city")["total"]
        .sum()
        .sort_values(ascending=False)
    )
    st.bar_chart(city_sales)

    # 11. Monthly sales trend
    st.subheader("Monthly Sales Trend")
    filtered_df["month"] = filtered_df["date"].dt.to_period("M").astype(str)
    monthly_sales = (
        filtered_df.groupby("month")["total"]
        .sum()
        .sort_index()
    )
    st.line_chart(monthly_sales)

    # 12. Payment method analysis
    st.subheader("Payment Method Usage")
    payment_counts = filtered_df["payment_method"].value_counts()
    st.bar_chart(payment_counts)

    # 13. Show detailed records
    st.subheader("Filtered Sales Records")
    st.dataframe(
        filtered_df.sort_values("date", ascending=False),
        use_container_width=True
    )

    # 14. Download filtered records
    csv_data = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Filtered Sales as CSV",
        data=csv_data,
        file_name="filtered_walmart_sales.csv",
        mime="text/csv"
    )

st.caption("Data source: project sales dataset. Figures represent recorded transaction totals, not verified official Walmart revenue.")
