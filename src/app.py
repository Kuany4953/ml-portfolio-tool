import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📊 ML Portfolio Optimization Tool")
st.write("Enter any stock ticker to view recent trends and analytics.")

# User input for ticker symbol
ticker = st.text_input("Enter stock ticker (e.g., AAPL, TSLA, GOOG, MSFT):", value="AAPL")

# Time period selection
period = st.selectbox("Select time period:", ['1mo', '3mo', '6mo', '1y', '2y'])

# Fetch data
data = yf.download(ticker, period=period)

# Validate and display
if not data.empty:
    # Compute Moving Averages
    data['MA_5'] = data['Close'].rolling(window=5).mean()
    data['MA_20'] = data['Close'].rolling(window=20).mean()

    # Display line chart with moving averages
    st.subheader(f"{ticker} Price Trend with Moving Averages")
    st.line_chart(data[['Close', 'MA_5', 'MA_20']])

    # Plot Volume
    st.subheader("📦 Trading Volume")
    st.bar_chart(data['Volume'])

    # Display recent data
    st.subheader("📅 Recent Stock Data")
    st.dataframe(data.tail(10))

    # Show basic statistics
    st.subheader("📈 Summary Statistics")
    st.write(data.describe())

else:
    st.error("⚠️ No data found. Please check the ticker symbol or try a different one.")
