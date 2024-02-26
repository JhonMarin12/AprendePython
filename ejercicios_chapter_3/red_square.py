# ****************
# EL CUADRADO ROJO
# ****************


def run(arc_A: float) -> float:
    # TU CÓDIGO AQUÍ
    radius = (arc_A * 2) / (3.14)
    area = radius ** 2

    return round(area, 10)


if __name__ == '__main__':
    run(1)