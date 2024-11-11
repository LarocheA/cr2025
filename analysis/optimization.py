# analysis/optimization.py

import numpy as np
import pandas as pd
from scipy.optimize import minimize

def optimize_portfolio(returns, target_return, risk_free_rate=0.02):
    def objective(weights, returns):
        portfolio_return = np.sum(returns.mean() * weights) * 252
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility
        return -sharpe_ratio

    def constraint(weights):
        return np.sum(weights) - 1

    num_assets = len(returns.columns)
    args = (returns,)
    constraints = ({'type': 'eq', 'fun': constraint})
    bounds = tuple((0, 1) for asset in range(num_assets))
    
    result = minimize(objective, num_assets*[1./num_assets], args=args, 
                      method='SLSQP', bounds=bounds, constraints=constraints)
    
    return result.x

def get_efficient_frontier(returns, num_portfolios=100):
    results = []
    for i in range(num_portfolios):
        weights = np.random.random(len(returns.columns))
        weights /= np.sum(weights)
        portfolio_return = np.sum(returns.mean() * weights) * 252
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
        results.append([portfolio_return, portfolio_volatility, weights])
    
    return pd.DataFrame(results, columns=['Return', 'Volatility', 'Weights'])
