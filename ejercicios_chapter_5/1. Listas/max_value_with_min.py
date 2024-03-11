# ************
# VALOR MÁXIMO
# ************


def run(values: list) -> int:
    # TU CÓDIGO AQUÍ
    valores_inveridos = [-x for x in values]
    max_value = min(valores_inveridos) * -1

    return max_value


if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])