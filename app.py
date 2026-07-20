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
    
    # Clean up the Date column and extract the Year for filtering
    df['Date'] = df['Date'].astype(str)
    # Assumes date format starts with year (e.g., "2023.12.01")
    df['Year'] = df['Date'].apply(lambda x: x.split('.')[0] if '.' in x else x.split('-')[0])
    
    # 3. Sidebar Controls
    st.sidebar.header("Dashboard Controls")
    
    # Year Selection Controller
    unique_years = sorted(df['Year'].unique())
    selected_year = st.sidebar.selectbox("Select Year:", unique_years, index=len(unique_years)-1)
    
    # Filter data based on the selected year
    df_year = df[df['Year'] == selected_year].reset_index(drop=True)
    
    # Zoom Slider Controller (applied to the selected year's data)
    max_data_points = len(df_year)
    num_points = st.sidebar.slider(
        "Select number of recent data points to view:", 
        min_value=50, 
        max_value=min(2000, max_data_points) if max_data_points > 50 else 50, 
        value=min(200, max_data_points),  
        step=50
    )
    
    # Filter for the most recent data within that year
    df_filtered = df_year.tail(num_points).reset_index(drop=True)
    
    # 4. Data Preview
    st.subheader(f"Data Preview (USD/JPY) - Year {selected_year}")
    st.dataframe(df_filtered.head(100)) 
    
    # 5. Thinner, Cleaner Price Chart
    st.subheader("Price Movement Chart")
    fig, ax = plt.subplots(figsize=(10, 4))
    
    ax.plot(df_filtered['Close'], label='Close Price', color='blue', linewidth=1.0)
    
    ax.set_title(f"USD/JPY Closing Prices ({selected_year} - Last {num_points} Bars)")
    ax.set_xlabel("Data Points")
    ax.set_ylabel("Price")
    ax.grid(True, linestyle='--', alpha=0.5) 
    
    st.pyplot(fig)

except FileNotFoundError:
    st.error("Could not find the 'USDJPY15.csv' file in your repository. Please check your file name!")
