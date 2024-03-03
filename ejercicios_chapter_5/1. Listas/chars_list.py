# **********************
# DESPLEGANDO CARACTERES
# **********************


def run(texts: list) -> list:
    # TU CÓDIGO AQUÍ
    chars = []

    for i in texts:
        chars += list(i)

    return chars


if __name__ == '__main__':
    run(['uno', 'dos', 'tres'])