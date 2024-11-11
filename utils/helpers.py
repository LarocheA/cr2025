import pandas as pd
from datetime import datetime

def load_csv(file_path):
    """
    Charge un fichier CSV et retourne un DataFrame pandas.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'a pas été trouvé.")
        return None

def save_csv(df, file_path):
    """
    Sauvegarde un DataFrame pandas en fichier CSV.
    """
    df.to_csv(file_path, index=False)
    print(f"Données sauvegardées dans {file_path}")

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
