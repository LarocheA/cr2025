import uuid

class Transaction:
    def __init__(self, symbol, quantity, price, transaction_type, date=None):
        self.id = str(uuid.uuid4())
        self.symbol = symbol
        self.quantity = float(quantity)
        self.price = float(price)
        self.transaction_type = transaction_type
        self.date = date or datetime.now()

        if self.quantity <= 0 or self.price <= 0:
            raise ValueError("La quantité et le prix doivent être positifs")

    def get_total_value(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.transaction_type.capitalize()} {self.quantity} {self.symbol} at {self.price} on {self.date} (Total: {self.get_total_value():.2f})"

def add_transaction(portfolio, transaction):
    if transaction.transaction_type == 'buy':
        portfolio.add_crypto(transaction.symbol, transaction.quantity)
    elif transaction.transaction_type == 'sell':
        if portfolio.get_crypto_quantity(transaction.symbol) < transaction.quantity:
            raise ValueError("Quantité insuffisante pour la vente")
        portfolio.remove_crypto(transaction.symbol, transaction.quantity)
    else:
        raise ValueError("Type de transaction non valide")

    portfolio.transactions.append(transaction)
    portfolio.update_values()
