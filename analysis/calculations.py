import numpy as np
import pandas as pd

def calculate_portfolio_return(portfolio):
    initial_value = 10264.92  # Valeur initiale du portefeuille
    current_value = portfolio.get_total_value()
    return ((current_value - initial_value) / initial_value) * 100

def calculate_sharpe_ratio(portfolio, risk_free_rate=0.02):
    returns = portfolio.calculate_returns()
    volatility = portfolio.calculate_volatility()
    return (returns.mean() - risk_free_rate) / volatility.mean()

def calculate_correlation_matrix(portfolio):
    df_close = pd.DataFrame()
    for symbol in portfolio.df['symbol']:
        hist_data = pd.DataFrame(portfolio.crypto_data.historical_data[symbol])
        df_close[symbol] = hist_data['close']
    return df_close.corr()

def interpret_fear_greed_index(index):
    if index <= 20:
        return "Extreme Fear"
    elif index <= 40:
        return "Fear"
    elif index <= 60:
        return "Neutral"
    elif index <= 80:
        return "Greed"
    else:
        return "Extreme Greed"
