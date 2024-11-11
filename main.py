# main.py

from config import PORTFOLIO
from data.crypto_data import CryptoData
from portfolio.portfolio import Portfolio
from analysis.calculations import calculate_portfolio_roi, calculate_volatility, calculate_sharpe_ratio
from analysis.optimization import optimize_portfolio, get_efficient_frontier
from analysis.visualization import plot_asset_allocation, plot_efficient_frontier, plot_correlation_heatmap
from data.api_client import get_fear_and_greed_index

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
    returns = portfolio.calculate_returns()
    volatility = portfolio.calculate_volatility()
    sharpe_ratio = portfolio.calculate_sharpe_ratio()

    print(f"\nVolatilité du portefeuille: {volatility:.2f}")
    print(f"Ratio de Sharpe: {sharpe_ratio:.2f}")

    # Optimisation du portefeuille
    optimized_weights = optimize_portfolio(portfolio.get_returns(), target_return=0.3)
        print("Poids optimisés du portefeuille :", optimized_weights)
    efficient_frontier = get_efficient_frontier(returns)

    # Visualisations
    plot_asset_allocation(portfolio)
    plot_efficient_frontier(efficient_frontier, {'Return': portfolio.calculate_returns().mean() * 252, 'Volatility': volatility})
    plot_correlation_heatmap(returns)

    # Fear and Greed Index
    fear_greed_index = get_fear_and_greed_index()
    print(f"\nFear and Greed Index: {fear_greed_index}")

if __name__ == "__main__":
    main()
