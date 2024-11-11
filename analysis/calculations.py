# analysis/calculations.py

import numpy as np

def calculate_roi(initial_value, current_value):
    return ((current_value - initial_value) / initial_value) * 100

def calculate_portfolio_roi(portfolio, initial_value):
    current_value = portfolio.get_total_value()
    return calculate_roi(initial_value, current_value)

def calculate_volatility(returns):
    return np.std(returns) * np.sqrt(365)
