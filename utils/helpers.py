import pandas as pd
from datetime import datetime
import re

def load_csv(file_path):
    """
    Charge un fichier CSV et retourne un DataFrame pandas.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'a pas été trouvé.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Le fichier {file_path} est vide.")
        return None
    except pd.errors.ParserError:
        print(f"Erreur lors de l'analyse du fichier {file_path}.")
        return None

def save_csv(df, file_path):
    """
    Sauvegarde un DataFrame pandas en fichier CSV.
    """
    try:
        df.to_csv(file_path, index=False)
        print(f"Données sauvegardées dans {file_path}")
    except PermissionError:
        print(f"Erreur de permission lors de l'écriture dans {file_path}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des données : {str(e)}")

def format_currency(value):
    """
    Formate une valeur en devise avec deux décimales.
    """
    return f"${value:.2f}"

def calculate_percentage_change(old_value, new_value):
    """
    Calcule le pourcentage de changement entre deux valeurs.
    """
    if old_value == 0:
        return 0
    return ((new_value - old_value) / old_value) * 100

def get_current_timestamp():
    """
    Retourne le timestamp actuel au format YYYY-MM-DD HH:MM:SS.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_crypto_symbol(symbol):
    """
    Valide le format du symbole d'une cryptomonnaie.
    """
    pattern = r'^[A-Z0-9]{2,10}$'
    return bool(re.match(pattern, symbol))

def handle_api_error(response):
    """
    Gère les erreurs d'API courantes.
    """
    if response.status_code == 400:
        print("Erreur 400: Mauvaise requête")
    elif response.status_code == 401:
        print("Erreur 401: Non autorisé - Vérifiez votre clé API")
    elif response.status_code == 403:
        print("Erreur 403: Accès interdit")
    elif response.status_code == 404:
        print("Erreur 404: Ressource non trouvée")
    elif response.status_code == 429:
        print("Erreur 429: Trop de requêtes - Attendez avant de réessayer")
    elif response.status_code >= 500:
        print(f"Erreur {response.status_code}: Erreur serveur")
    else:
        print(f"Erreur inattendue: {response.status_code}")

def export_to_csv(df, filename):
    """
    Exporte un DataFrame pandas vers un fichier CSV.
    
    :param df: Le DataFrame à exporter
    :param filename: Le nom du fichier CSV de sortie
    """
    try:
        df.to_csv(filename, index=False)
        print(f"Données exportées avec succès dans '{filename}'")
    except Exception as e:
        print(f"Erreur lors de l'exportation des données : {str(e)}")
