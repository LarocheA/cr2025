# main.py

from config import PORTFOLIO
from data.crypto_data import CryptoData
from portfolio.portfolio import Portfolio
from analysis.calculations import calculate_returns, calculate_volatility, calculate_sharpe_ratio

def main():
    # Initialisation des données
    crypto_data = CryptoData()
    portfolio = Portfolio(PORTFOLIO)

    # Mise à jour des prix
    symbols = [crypto['symbol'] for crypto in PORTFOLIO]
    crypto_data.update_prices(symbols)
    portfolio.update_prices(crypto_data)

    # Affichage des informations du portefeuille
    print(f"Valeur totale du portefeuille: ${portfolio.get_total_value():.2f}")
    print("\nAllocation des actifs:")
    print(portfolio.get_asset_allocation())

    # Analyse des performances
    historical_data = crypto_data.get_historical_data(symbols)
    for symbol, data in historical_data.items():
        df = pd.DataFrame(data)
        df = calculate_returns(df)
        volatility = calculate_volatility(df)
        sharpe_ratio = calculate_sharpe_ratio(df)
        print(f"\nAnalyse pour {symbol}:")
        print(f"Volatilité: {volatility:.2f}")
        print(f"Ratio de Sharpe: {sharpe_ratio:.2f}")

if __name__ == "__main__":
    main()
