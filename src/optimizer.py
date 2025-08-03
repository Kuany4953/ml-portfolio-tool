from scipy.optimize import minimize
import numpy as np

def optimize_portfolio(expected_returns, cov_matrix):
    n = len(expected_returns)
    bounds = [(0, 1)] * n
    init = np.ones(n) / n
    constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}

    def neg_sharpe(w):
        ret = np.dot(w, expected_returns)
        vol = np.sqrt(np.dot(w.T, np.dot(cov_matrix, w)))
        return -ret / vol

    result = minimize(neg_sharpe, init, bounds=bounds, constraints=constraints)
    return result.x
