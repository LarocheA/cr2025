from config import PORTFOLIO
from data.crypto_data import get_historical_prices, calculate_returns
from analysis.optimization import optimize_portfolio, get_efficient_frontier

def main():
    symbols = [crypto['symbol'] for crypto in PORTFOLIO]
    
    # Récupérer les données historiques
    historical_data = get_historical_prices(symbols)
    
    # Calculer les rendements
    returns = calculate_returns(historical_data)
    
    # Optimiser le portefeuille
    optimal_weights = optimize_portfolio(returns)
    
    # Calculer la frontière efficiente
    efficient_frontier = get_efficient_frontier(returns)
    
    # Afficher les résultats
    print("Poids optimaux :")
    for symbol, weight in zip(symbols, optimal_weights):
        print(f"{symbol}: {weight:.4f}")
    
    # Vous pouvez ajouter ici du code pour visualiser la frontière efficiente

if __name__ == "__main__":
    main()
