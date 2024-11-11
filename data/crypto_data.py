from .api_client import CryptoAPIClient

class CryptoData:
    def __init__(self):
        self.api_client = CryptoAPIClient()
        self.prices = {}
        self.history = {}

    def update_price(self, crypto_id):
        self.prices[crypto_id] = self.api_client.get_crypto_price(crypto_id)

    def get_price(self, crypto_id):
        if crypto_id not in self.prices:
            self.update_price(crypto_id)
        return self.prices[crypto_id]

    def get_history(self, crypto_id, days=30):
        if crypto_id not in self.history:
            self.history[crypto_id] = self.api_client.get_crypto_history(crypto_id, days=days)
        return self.history[crypto_id]
