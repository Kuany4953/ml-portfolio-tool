from sklearn.ensemble import RandomForestRegressor
import pandas as pd

def train_predict(X, y):
    model = RandomForestRegressor()
    model.fit(X, y)
    preds = pd.DataFrame(model.predict(X), index=X.index, columns=y.columns)
    return preds
