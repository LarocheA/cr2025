# main.py

# Suivez les instructions à l'écran pour interagir avec l'application.

# Structure du projet
#- `main.py`: Point d'entrée principal de l'application
#- `config.py`: Configuration de l'application
#- `data/`: Module pour la récupération et le stockage des données
#- `portfolio/`: Module de gestion du portefeuille
#- `analysis/`: Module d'analyse et d'optimisation
#- `ui/`: Interfaces utilisateur (CLI et GUI)
#- `utils/`: Fonctions utilitaires

# Contribution
# Les contributions sont les bienvenues ! Veuillez consulter le fichier CONTRIBUTING.md pour plus de détails.

# Licence
# Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

import pandas as pd
from config import PORTFOLIO
from data.crypto_data import CryptoData
from portfolio.portfolio import Portfolio
from analysis.calculations import calculate_portfolio_return, calculate_sharpe_ratio, calculate_correlation_matrix
from analysis.optimization import optimize_portfolio
from analysis.visualization import plot_portfolio_allocation, plot_price_history, plot_correlation_heatmap
from ui.cli import run_cli
from ui.gui import run_gui
from utils.helpers import load_csv, save_csv, get_current_timestamp

def main():
    # Initialisation des données
    crypto_data = CryptoData(PORTFOLIO)
    crypto_data.update_prices()
    crypto_data.get_historical_data()
    crypto_data.update_fear_greed_index()

    # Création du portefeuille
    portfolio = Portfolio(crypto_data)

    # Calculs et analyses
    portfolio_return = calculate_portfolio_return(portfolio)
    sharpe_ratio = calculate_sharpe_ratio(portfolio)
    correlation_matrix = calculate_correlation_matrix(portfolio)

    # Optimisation du portefeuille
    optimal_weights = optimize_portfolio(portfolio)

    returns = portfolio.get_returns()
    optimal_weights = optimize_portfolio(returns)
    
    # Affichage des résultats
    print(f"Valeur totale du portefeuille: ${portfolio.get_total_value():.2f}")
    print(f"Rendement du portefeuille: {portfolio_return:.2f}%")
    print(f"Ratio de Sharpe: {sharpe_ratio:.2f}")
    print(f"Fear and Greed Index: {crypto_data.fear_greed_index}")

    # Visualisations
    plot_portfolio_allocation(portfolio)
    plot_price_history(portfolio)
    plot_correlation_heatmap(correlation_matrix)

    # Sauvegarde des données
    df_portfolio = portfolio.to_dataframe()
    save_csv(df_portfolio, f'portfolio_data_{get_current_timestamp()}.csv')

    # Lancement de l'interface utilisateur
    choice = input("Choisissez l'interface (cli/gui): ").lower()
    if choice == 'cli':
        run_cli(portfolio)
    elif choice == 'gui':
        run_gui(portfolio)
    else:
        print("Choix invalide. Fin du programme.")

if __name__ == "__main__":
    main()
