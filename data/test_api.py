# test_api.py

from data.api_client import get_crypto_price

def test_get_crypto_price():
    try:
        price = get_crypto_price('BTC')
        print(f"Le prix actuel du BTC est : ${price:.2f}")
    except Exception as e:
        print(f"Erreur: {e}")

if __name__ == "__main__":
    test_get_crypto_price()
