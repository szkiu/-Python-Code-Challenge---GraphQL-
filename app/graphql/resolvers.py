import pandas as pd
from ..utils.csv_loader import load_csv_data

# Cargar los datos CSV utilizando una función de utilidad
data = load_csv_data()


def resolve_get_data(_, info):
    # Convertir los datos a una lista de diccionarios
    return data.to_dict(orient="records")
