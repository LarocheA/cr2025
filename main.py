from data.crypto_data import CryptoData
from portfolio.portfolio import Portfolio

def main():
    crypto_data = CryptoData()
    portfolio = Portfolio()

    # Ajout de quelques transactions
    portfolio.add_transaction("bitcoin", 0.1, 50000, "2023-01-01")
    portfolio.add_transaction("ethereum", 1, 3000, "2023-02-01")

    # Affichage des holdings
    print("Holdings:")
    for crypto, amount in portfolio.get_holdings().items():
        print(f"{crypto}: {amount}")

    # Affichage de la valeur totale du portefeuille
    total_value = portfolio.get_total_value(crypto_data)
    print(f"\nValeur totale du portefeuille: ${total_value:.2f}")

if __name__ == "__main__":
    main()
