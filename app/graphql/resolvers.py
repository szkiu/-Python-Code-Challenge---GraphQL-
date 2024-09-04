from ..utils.csv_loader import load_csv_data


def resolve_get_data(_, info):
    data = load_csv_data()

    mapped_data = []
    for item in data:
        mapped_data.append(
            {
                "desc_ga_sku_producto": item.get("desc_ga_sku_producto"),
                "desc_ga_marca_producto": item.get("desc_ga_marca_producto"),
            }
        )

    return mapped_data
