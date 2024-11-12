import numpy as np
import pandas as pd

def calculate_portfolio_return(portfolio, initial_value=4500.00):
    """
    Calcule le rendement du portefeuille.

    Args:
        portfolio (Portfolio): L'objet portefeuille contenant les données actuelles.
        initial_value (float): La valeur initiale du portefeuille. Par défaut 4500.00.

    Returns:
        float: Le rendement du portefeuille en pourcentage.

    Raises:
        ValueError: Si la valeur initiale est négative ou nulle.
    """
    if initial_value <= 0:
        raise ValueError("La valeur initiale du portefeuille doit être positive.")

    try:
        current_value = portfolio.get_total_value()
        return ((current_value - initial_value) / initial_value) * 100
    except Exception as e:
        print(f"Erreur lors du calcul du rendement du portefeuille : {e}")
        return None

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
