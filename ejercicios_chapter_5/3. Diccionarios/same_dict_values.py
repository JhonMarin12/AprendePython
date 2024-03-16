# ******************************
# VALORES IGUALES EN DICCIONARIO
# ******************************


def run(items: dict) -> bool:
    # TU CÓDIGO AQUÍ
    values = list(items.values())
    all_same = all(i == values[0] for i in values)

    return all_same


if __name__ == '__main__':
    run({'a': 1, 'b': 1, 'c': 1, 'd': 1})