from datetime import datetime

class Transaction:
    def __init__(self, symbol, quantity, price, transaction_type, date=None):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.transaction_type = transaction_type
        self.date = date or datetime.now()

    def __str__(self):
        return f"{self.transaction_type.capitalize()} {self.quantity} {self.symbol} at {self.price} on {self.date}"

def add_transaction(portfolio, transaction):
    """
    Ajoute une transaction au portefeuille et met à jour les quantités.
    """
    if transaction.transaction_type == 'buy':
        portfolio.add_crypto(transaction.symbol, transaction.quantity)
    elif transaction.transaction_type == 'sell':
        portfolio.remove_crypto(transaction.symbol, transaction.quantity)
    else:
        raise ValueError("Type de transaction non valide")

    portfolio.transactions.append(transaction)
