# ************
# VALOR MÁXIMO
# ************


def run(values: list) -> int:
    # TU CÓDIGO AQUÍ
    max_value = values[0]
    for i in values:
        if i > max_value:
            max_value = i
    return max_value


if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])