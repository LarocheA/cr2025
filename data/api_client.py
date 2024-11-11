import requests

class CryptoAPIClient:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"

    def get_crypto_price(self, crypto_id, vs_currency="usd"):
        endpoint = f"/simple/price?ids={crypto_id}&vs_currencies={vs_currency}"
        response = requests.get(self.base_url + endpoint)
        if response.status_code == 200:
            data = response.json()
            return data[crypto_id][vs_currency]
        else:
            raise Exception(f"Erreur lors de la récupération du prix: {response.status_code}")

    def get_crypto_history(self, crypto_id, vs_currency="usd", days=30):
        endpoint = f"/coins/{crypto_id}/market_chart?vs_currency={vs_currency}&days={days}"
        response = requests.get(self.base_url + endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Erreur lors de la récupération de l'historique: {response.status_code}")
