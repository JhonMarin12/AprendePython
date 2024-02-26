# ***************
# ÁREA DEL ANILLO
# ***************


def run(z: float) -> float:
    # TU CÓDIGO AQUÍ
    white_area = 3.14 * (((z+z/2) **2 ) - (z/2)**2)

    return round(white_area,2)


if __name__ == '__main__':
    print(run(6))