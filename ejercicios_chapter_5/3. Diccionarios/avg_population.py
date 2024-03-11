# ******************
# POBLACIÓN PROMEDIO
# ******************


def run(pdata: dict) -> dict:
    # TU CÓDIGO AQUÍ
    avg_data = {}
    total_population = sum(pdata.values())

    for city in pdata:
        avg_data[city] = round((pdata[city]/total_population) * 100,3)
    return avg_data


if __name__ == '__main__':
    run({'Tokyo': 38140000, 'Delhi': 26454000, 'Shanghai': 24484000, 'Mumbai': 21357000})