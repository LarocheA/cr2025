import pandas as pd
import requests
from tqdm import tqdm

# Création d'une structure de données pour le portefeuille
portfolio = [
    {"symbol": "BTC", "quantity": 0.00043331},
    {"symbol": "BTC.b", "quantity": 0.0113417},
    {"symbol": "ETH", "quantity": 0.22375339},
    {"symbol": "WETH", "quantity": 0.0002109},
    {"symbol": "WETH.e", "quantity": 0.111998},
    {"symbol": "wstETH", "quantity": 0.0187779},
    {"symbol": "DOT", "quantity": 252.0325},
    {"symbol": "KSM", "quantity": 2.19},
    {"symbol": "AVAX", "quantity": 12.9},
    {"symbol": "WAVAX", "quantity": 0.0024956},
    {"symbol": "sAVAX", "quantity": 3.82},
    {"symbol": "LINK", "quantity": 22},
    {"symbol": "LINK.e", "quantity": 18.9},
    {"symbol": "GRT", "quantity": 1366.1},
    {"symbol": "CAPS", "quantity": 19217.1121},
    {"symbol": "SOL", "quantity": 0.07633722},
    {"symbol": "TIA", "quantity": 1.7},
    {"symbol": "OMI", "quantity": 94000},
    {"symbol": "USDT", "quantity": 0.53771299},
    {"symbol": "USDC", "quantity": 0},
    {"symbol": "DAI", "quantity": 0}
]

# Création d'une DataFrame à partir de la structure
df_portfolio = pd.DataFrame(portfolio)

def get_current_prices(symbols, vs_currency='USD'):
    base_url = "https://min-api.cryptocompare.com/data/pricemulti"
    api_key = "02f11b8b9dec16c0149bae39ee0b3f4ea8cf7528552e71622d8b887ff3f149a0"
    
    # Convertir la liste de symboles en une chaîne séparée par des virgules
    fsyms = ','.join(symbols)
    
    params = {
        "fsyms": fsyms,
        "tsyms": vs_currency
    }
    
    headers = {
        "authorization": f"Apikey {api_key}"
    }
    
    response = requests.get(base_url, params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        prices = {}
        for symbol in symbols:
            if symbol in data and vs_currency in data[symbol]:
                prices[symbol] = data[symbol][vs_currency]
            else:
                prices[symbol] = None
        return prices
    else:
        print(f"Erreur lors de la récupération des prix : {response.status_code}")
        return None

# Récupération des prix actuels
prices = get_current_prices(df_portfolio['symbol'].tolist())

# Ajout des prix actuels au DataFrame
df_portfolio['current_price'] = df_portfolio['symbol'].map(prices)

# Calcul de la valeur totale de chaque position
df_portfolio['total_value'] = df_portfolio['quantity'] * df_portfolio['current_price']

# Calcul de la valeur totale du portefeuille
total_portfolio_value = df_portfolio['total_value'].sum()

# Calcul du pourcentage de chaque crypto dans le portefeuille
df_portfolio['portfolio_percentage'] = df_portfolio['total_value'] / total_portfolio_value * 100

# Affichage du résultat
print(df_portfolio)
print(f"\nValeur totale du portefeuille : ${total_portfolio_value:.2f}")
