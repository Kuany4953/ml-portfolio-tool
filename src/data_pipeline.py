import yfinance as yf
import pandas as pd

def fetch_data(tickers, start='2020-01-01', end='2024-12-31'):
    df = yf.download(tickers, start=start, end=end)['Adj Close']
    return df.dropna()

def compute_returns(price_df):
    return price_df.pct_change().dropna()
