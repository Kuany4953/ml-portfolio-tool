
import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# App title
st.title("ML Portfolio Optimization Tool")
st.write("📈 Select a stock and view its recent performance")

# Stock ticker input
ticker = st.selectbox("Choose a stock ticker:", ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA'])

# Date range
period = st.selectbox("Select time period:", ['1mo', '3mo', '6mo', '1y', '2y'])

# Fetch data
data = yf.download(ticker, period=period)

if not data.empty:
    # Plotting
    st.line_chart(data['Adj Close'])
    st.write(f"Recent data for **{ticker}**")
    st.dataframe(data.tail())
else:
    st.warning("No data found. Please try another ticker.")
