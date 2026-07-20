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
    
    # 3. Simple Chart using the newly defined 'Close' column
    st.subheader("Price Movement Chart")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df['Close'], label='Close Price', color='blue')
    ax.set_title("USD/JPY Closing Prices")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    st.pyplot(fig)

except FileNotFoundError:
    st.error("Could not find the 'USDJPY15.csv' file in your repository. Please check your file name!")
