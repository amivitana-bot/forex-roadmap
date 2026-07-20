
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Title of your dashboard
st.title("📊 Forex Roadmap Dashboard")
st.write("Welcome! This app analyzes your currency data.")

# 2. Try to load your data file
try:
    df = pd.read_csv("USDJPY15.csv")
    
    st.subheader("Data Preview (USD/JPY)")
    st.dataframe(df.head(100)) # Shows the first 100 rows
    
    # 3. Simple Chart
    st.subheader("Price Movement Chart")
    if 'Close' in df.columns:
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(df['Close'], label='Close Price', color='blue')
        ax.set_title("USD/JPY Closing Prices")
        ax.set_xlabel("Time")
        ax.set_ylabel("Price")
        st.pyplot(fig)
    else:
        # Check if the column is capitalized differently, e.g., 'close'
        close_col = [col for col in df.columns if col.lower() == 'close']
        if close_col:
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(df[close_col[0]], label='Close Price', color='blue')
            ax.set_title("USD/JPY Closing Prices")
            st.pyplot(fig)
        else:
            st.info("To see a chart, make sure your CSV file has a price column like 'Close'.")

except FileNotFoundError:
    st.error("Could not find the 'USDJPY15.csv' file in your repository. Please check your file name!")
