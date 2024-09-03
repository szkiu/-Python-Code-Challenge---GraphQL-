import pandas as pd


def load_csv_data(file_path: str = "./data/Data_example.csv"):
    """Carga el archivo CSV y devuelve un DataFrame de pandas."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise Exception(f"Archivo no encontrado en la ruta especificada: {file_path}")
