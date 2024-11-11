from .transaction import Transaction

class Portfolio:
    def __init__(self):
        self.holdings = {}
        self.transactions = []

    def add_transaction(self, crypto_id, amount, price, date):
        transaction = Transaction(crypto_id, amount, price, date)
        self.transactions.append(transaction)
        if crypto_id in self.holdings:
            self.holdings[crypto_id] += amount
        else:
            self.holdings[crypto_id] = amount

    def get_holdings(self):
        return self.holdings

    def get_total_value(self, crypto_data):
        total = 0
        for crypto_id, amount in self.holdings.items():
            price = crypto_data.get_price(crypto_id)
            total += amount * price
        return total
