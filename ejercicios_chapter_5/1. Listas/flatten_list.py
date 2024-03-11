# ***************
# APLANA LA LISTA
# ***************


def run(elements: list) -> list:
    # TU CÓDIGO AQUÍ
    flatten_elements = []

    for i in elements:
        if isinstance(i, list):
            for j in i:
                flatten_elements.append(j)
        else:
            flatten_elements.append(i)

    return flatten_elements


if __name__ == '__main__':
    run([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])