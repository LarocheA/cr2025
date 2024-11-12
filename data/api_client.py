import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from config import API_KEY_CRYPTOCOMPARE, API_KEY_COINMARKETCAP, BASE_URL_CRYPTOCOMPARE, BASE_URL_COINMARKETCAP, FEAR_GREED_URL

def get_crypto_price(symbol, vs_currency='usd'):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies={vs_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if symbol in data and vs_currency in data[symbol]:
            return data[symbol][vs_currency]
    raise Exception(f"Erreur lors de la récupération du prix pour {symbol}")

# 
def get_historical_data(symbol, vs_currency='USD', limit=2000):
    url = f"{BASE_URL_CRYPTOCOMPARE}/histoday"
    params = {
        "fsym": symbol,
        "tsym": vs_currency,
        "limit": limit,
        "api_key": API_KEY_CRYPTOCOMPARE
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['Data']['Data']
    else:
        raise Exception(f"Error fetching historical data for {symbol}: {response.status_code}")

def get_fear_and_greed_index():
    response = requests.get(FEAR_GREED_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        fng_value = soup.find('div', class_='fng-value')
        if fng_value:
            return int(''.join(filter(str.isdigit, fng_value.text)))
    return None
