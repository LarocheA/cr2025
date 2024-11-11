from datetime import datetime

class Transaction:
    def __init__(self, crypto_id, amount, price, date=None):
        self.crypto_id = crypto_id
        self.amount = amount
        self.price = price
        self.date = date or datetime.now()

    def __str__(self):
        return f"Transaction: {self.crypto_id}, Amount: {self.amount}, Price: {self.price}, Date: {self.date}"
