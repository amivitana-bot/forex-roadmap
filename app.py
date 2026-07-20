import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Title of your dashboard
st.title("📊 Forex Roadmap Dashboard")
st.write("Welcome! This app analyzes your currency data.")

# 2. Try to load your data file
try:
    # Since the CSV has no header row, we define the names manually
    column_names = ['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    df = pd.read_csv("USDJPY15.csv", header=None, names=column_names)
    
    st.subheader("Data Preview (USD/JPY)")
    st.dataframe(df.head(100)) # Shows the first 100 rows
    
    # 3. Sidebar Slider Control to fix the thickness/zoom
    st.sidebar.header("Chart Settings")
    max_data_points = len(df)
    num_points = st.sidebar.slider(
        "Select number of recent data points to view:", 
        min_value=50, 
        max_value=min(2000, max_data_points), 
        value=200,  # Default view is 200 bars so it looks clean
        step=50
    )
    
    # Filter for the most recent data chosen by the slider
    df_filtered = df.tail(num_points).reset_index(drop=True)
    
    # 4. Thinner, Cleaner Price Chart
    st.subheader("Price Movement Chart")
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # linewidth=1.0 makes the line much thinner and crisper
    ax.plot(df_filtered['Close'], label='Close Price', color='blue', linewidth=1.0)
    
    ax.set_title(f"USD/JPY Closing Prices (Last {num_points} Bars)")
    ax.set_xlabel("Data Points")
    ax.set_ylabel("Price")
    ax.grid(True, linestyle='--', alpha=0.5) # Adds a clean background grid
    
    st.pyplot(fig)

except FileNotFoundError:
    st.error("Could not find the 'USDJPY15.csv' file in your repository. Please check your file name!")
