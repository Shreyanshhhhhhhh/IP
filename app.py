import streamlit as st
import pandas as pd

# Load CSV data
file_path = 'lapdata.csv'  # Ensure this path is correct
laptop_data = pd.read_csv(file_path)

# Title of the app
st.title("Laptop Inventory Management & Recommendation System")

 # Display the data
st.header("Laptop Data")
st.write(laptop_data)

# Filter by price
st.subheader("Filter by Price Range")
min_price = st.number_input("Minimum Price", value=50000)
max_price = st.number_input("Maximum Price", value=100000)
if st.button("Filter by Price"):
    price_filtered = laptop_data[(laptop_data['Price'] >= min_price) & (laptop_data['Price'] <= max_price)]
    st.write(price_filtered)

# Filter by brand
st.subheader("Filter by Brand")
brand_name = st.text_input("Enter Brand Name", value="Dell")
if st.button("Filter by Brand"):
    brand_filtered = laptop_data[laptop_data['Company'].str.contains(brand_name, case=False)]
    st.write(brand_filtered)