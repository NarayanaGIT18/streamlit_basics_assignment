import streamlit as st
import pandas as pd

# --------------------
# Step 1: Create Data
# --------------------
data = {
    "Product": ["Apples", "Bananas", "Carrots", "Dates", "Eggs"],
    "Category": ["Fruit", "Fruit", "Vegetable", "Fruit", "Dairy"],
    "Sales": [120, 85, 60, 200, 150]
}

df = pd.DataFrame(data)

# --------------------
# Step 2: Sidebar Filter
# --------------------
st.sidebar.title("Filter Options")

categories = df["Category"].unique().tolist()

selected_category = st.sidebar.selectbox(
    "Select Category",
    categories
)

# --------------------
# Step 3: Filter Data
# --------------------
filtered_df = df[df["Category"] == selected_category]

# --------------------
# Step 4: Main Page
# --------------------
st.title("Sales Summary Dashboard")

st.subheader("Filtered Data")
st.dataframe(filtered_df)

# --------------------
# Step 5: Line Chart
# --------------------
st.subheader("Sales Chart")

chart_data = filtered_df.set_index("Product")["Sales"]

st.line_chart(chart_data)