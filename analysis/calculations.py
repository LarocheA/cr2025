# analysis/calculations.py

import numpy as np
import pandas as pd

def calculate_returns(df):
    df['daily_return'] = df['close'].pct_change()
    df['cumulative_return'] = (1 + df['daily_return']).cumprod() - 1
    return df

def calculate_volatility(df):
    return df['daily_return'].std() * np.sqrt(365)

def calculate_sharpe_ratio(df, risk_free_rate=0.01):
    volatility = calculate_volatility(df)
    annual_return = df['daily_return'].mean() * 365
    return (annual_return - risk_free_rate) / volatility
