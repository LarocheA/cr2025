import argparse
from portfolio.portfolio import Portfolio
from data.crypto_data import CryptoData
from config import PORTFOLIO
from analysis.visualization import plot_portfolio_allocation, plot_price_history
from utils.helpers import export_to_csv

def run_cli():
    parser = argparse.ArgumentParser(description="Crypto Portfolio Tracker CLI")
    parser.add_argument("-d", "--display", action="store_true", help="Display portfolio")
    parser.add_argument("-u", "--update", action="store_true", help="Update prices")
    parser.add_argument("-a", "--analyze", action="store_true", help="Analyze performance")
    parser.add_argument("-g", "--graph", choices=["allocation", "history"], help="Display graphs")
    parser.add_argument("-e", "--export", action="store_true", help="Export data to CSV")
    
    args = parser.parse_args()
    
    crypto_data = CryptoData()
    portfolio = Portfolio(PORTFOLIO)
    
    if args.update:
        crypto_data.update_prices()
        portfolio.update_prices(crypto_data)
        print("Prix mis à jour avec succès.")
    
    if args.display:
        portfolio.display()
    
    if args.analyze:
        portfolio.analyze_performance()
    
    if args.graph:
        if args.graph == "allocation":
            plot_portfolio_allocation(portfolio)
        elif args.graph == "history":
            plot_price_history(portfolio)
    
    if args.export:
        export_to_csv(portfolio.to_dataframe(), "portfolio_export.csv")
        print("Données exportées avec succès dans 'portfolio_export.csv'")

if __name__ == "__main__":
    run_cli()
