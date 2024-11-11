# portfolio/portfolio.py

class Portfolio:
    def __init__(self, crypto_list):
        self.crypto_list = crypto_list

    def get_total_value(self):
        return sum(crypto['quantity'] * crypto['price'] for crypto in self.crypto_list)

    def get_crypto_values(self):
        return {crypto['symbol']: crypto['quantity'] * crypto['price'] for crypto in self.crypto_list}

    def get_crypto_percentages(self):
        total_value = self.get_total_value()
        return {crypto['symbol']: (crypto['quantity'] * crypto['price'] / total_value) * 100 for crypto in self.crypto_list}
