# *********************
# VOLUMEN DE UNA ESFERA
# *********************


def run(radius: float) -> float:
    constante = 4/3 * 3.14
    volume = constante * radius ** 3

    return volume


if __name__ == '__main__':
    run(5)