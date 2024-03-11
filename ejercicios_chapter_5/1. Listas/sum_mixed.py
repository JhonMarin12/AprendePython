# ****************
# SUMA HETEROGÉNEA
# ****************


def run(items: list) -> int:
    # TU CÓDIGO AQUÍ
    sum_items = sum([int(x) for x in items])

    return sum_items


if __name__ == '__main__':
    run([1, '2', 3, '4', 5])