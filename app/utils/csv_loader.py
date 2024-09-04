import pandas as pd


def load_csv_data():
    try:
        df = pd.read_csv("/app/data/Data_example.csv")

        df.replace("", pd.NA, inplace=True)
        df.fillna("Unknown", inplace=True)

        data = df.to_dict(orient="records")

        return data
    except Exception as e:
        print(f"Error loading CSV data: {e}")
        return []
