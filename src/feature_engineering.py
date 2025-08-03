import pandas as pd

def add_features(prices):
    features = {}
    for ticker in prices.columns:
        features[f'{ticker}_momentum'] = prices[ticker].pct_change(20)
        features[f'{ticker}_volatility'] = prices[ticker].rolling(20).std()
        features[f'{ticker}_ma_ratio'] = prices[ticker].rolling(5).mean() / prices[ticker].rolling(20).mean()
    return pd.DataFrame(features).dropna()
