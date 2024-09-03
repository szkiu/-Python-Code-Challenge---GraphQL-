import pandas as pd


def load_csv_data(file_path: str = "./data/Data_example.csv"):
    """Carga el archivo CSV y devuelve un DataFrame de pandas."""
    return pd.read_csv(file_path)
