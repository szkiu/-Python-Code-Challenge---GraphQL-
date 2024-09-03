import pandas as pd
from ..utils.csv_loader import load_csv_data

# Cargar los datos CSV utilizando la ruta correcta
data = (
    load_csv_data()
)  # Asegúrate de que no esté especificando una ruta incorrecta aquí


def resolve_get_data(_, info):
    return data.to_dict(orient="records")
