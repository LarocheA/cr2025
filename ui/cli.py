from portfolio.portfolio import Portfolio
from data.crypto_data import CryptoData
from config import PORTFOLIO

def display_menu():
    print("\n--- Menu Principal ---")
    print("1. Afficher le portefeuille")
    print("2. Mettre à jour les prix")
    print("3. Analyser les performances")
    print("4. Quitter")

def run_cli():
    crypto_data = CryptoData()
    portfolio = Portfolio(PORTFOLIO)

    while True:
        display_menu()
        choice = input("Choisissez une option : ")

        if choice == '1':
            portfolio.display()
        elif choice == '2':
            crypto_data.update_prices()
            portfolio.update_prices(crypto_data)
            print("Prix mis à jour avec succès.")
        elif choice == '3':
            portfolio.analyze_performance()
        elif choice == '4':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    run_cli()
