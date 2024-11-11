# data/api_client.py

import requests
from config import API_KEY, BASE_URL

def get_crypto_price(symbol, vs_currency='USD'):
    url = f"{BASE_URL}/price"
    params = {
        "fsym": symbol,
        "tsyms": vs_currency,
        "api_key": API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['Data'][vs_currency]
    else:
        raise Exception(f"Error fetching price for {symbol}: {response.status_code}")
