git init
git add .
git commit -m "Initial commit"
import streamlit as st
import pandas as pd
from src.data_pipeline import fetch_data, compute_returns
from src.feature_engineering import add_features
from src.model import train_predict
from src.optimizer import optimize_portfolio

tickers = st.multiselect("Choose Assets", ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'NVDA'], default=['AAPL', 'MSFT'])
prices = fetch_data(tickers)
returns = compute_returns(prices)
features = add_features(prices)
features, returns = features.align(returns.shift(-1), join='inner', axis=0)

preds = train_predict(features, returns)
latest_preds = preds.iloc[-1]
cov_matrix = returns.cov()
weights = optimize_portfolio(latest_preds, cov_matrix)

st.write("### Optimized Weights:")
for t, w in zip(tickers, weights):
    st.write(f"{t}: {w:.2%}")
