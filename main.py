# main.py

from config import PORTFOLIO
from data.crypto_data import update_portfolio_prices, get_historical_dataframe
from portfolio.portfolio import Portfolio
from analysis.calculations import calculate_portfolio_roi, calculate_volatility

def main():
    # Mettre à jour les prix du portefeuille
    updated_portfolio = update_portfolio_prices(PORTFOLIO)

    # Créer l'objet Portfolio
    portfolio = Portfolio(updated_portfolio)

    # Calculer et afficher la valeur totale du portefeuille
    total_value = portfolio.get_total_value()
    print(f"Valeur totale du portefeuille: ${total_value:.2f}")

    # Afficher les valeurs individuelles des cryptos
    crypto_values = portfolio.get_crypto_values()
    for symbol, value in crypto_values.items():
        print(f"{symbol}: ${value:.2f}")

    # Afficher les pourcentages du portefeuille
    crypto_percentages = portfolio.get_crypto_percentages()
    for symbol, percentage in crypto_percentages.items():
        print(f"{symbol}: {percentage:.2f}%")

    # Calculer et afficher le ROI (supposons une valeur initiale de 10000 pour cet exemple)
    initial_value = 10000
    roi = calculate_portfolio_roi(portfolio, initial_value)
    print(f"ROI du portefeuille: {roi:.2f}%")

    # Obtenir les données historiques et calculer la volatilité
    historical_data = get_historical_dataframe(PORTFOLIO)
    returns = historical_data.pct_change().dropna()
    volatility = calculate_volatility(returns)
    print(f"Volatilité du portefeuille: {volatility:.2f}%")

if __name__ == "__main__":
    main()
