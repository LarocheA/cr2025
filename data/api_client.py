import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from config import API_KEY_CRYPTOCOMPARE, API_KEY_COINMARKETCAP, BASE_URL_CRYPTOCOMPARE, BASE_URL_COINMARKETCAP, FEAR_GREED_URL

def get_crypto_price(symbol, vs_currency='USD'):
    """
    Récupère le prix actuel d'une cryptomonnaie.
    
    :param symbol: Le symbole de la cryptomonnaie
    :param vs_currency: La devise de référence (par défaut USD)
    :return: Le prix actuel de la cryptomonnaie
    """
    url = f"{BASE_URL_CRYPTOCOMPARE}/price"
    params = {
        "fsym": symbol,
        "tsyms": vs_currency,
        "api_key": API_KEY_CRYPTOCOMPARE
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if vs_currency in data:
            return data[vs_currency]
        else:
            raise KeyError(f"Les données pour {symbol} en {vs_currency} ne sont pas disponibles.")
    except RequestException as e:
        raise Exception(f"Erreur lors de la récupération du prix pour {symbol}: {str(e)}")

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
