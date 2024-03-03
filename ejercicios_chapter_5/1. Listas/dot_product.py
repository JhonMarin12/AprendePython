# ****************
# PRODUCTO ESCALAR
# ****************


def run(vector1: list, vector2: list) -> float:
    # TU CÓDIGO AQUÍ
    dprod = 0

    if len(vector1) != len(vector2):
        return None
    for i, j in zip(vector1, vector2):
        dprod += i * j
        
    return dprod


if __name__ == '__main__':
    run([4, 3, 8, 1], [9, 2, 7, 3])