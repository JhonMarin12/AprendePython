# ***********
# MITAD FUERA
# ***********


def run(values: set) -> set:
    # TU CÓDIGO AQUÍ
    
    half_out_values = set()

    for i in values:
        valor = i // 2
        if valor not in values:
            half_out_values.add(valor)

    return half_out_values


if __name__ == '__main__':
    run({50, 100, 4, 6, 12})