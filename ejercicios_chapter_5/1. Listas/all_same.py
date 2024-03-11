# *****************************
# SOMOS IGUALES, PERO DISTINTOS
# *****************************


def run(items: list) -> bool:
    # TU CÓDIGO AQUÍ
    all_same = False
    # first_item = items[0]
    # for i in items:
    #     if i != first_item:
    #         all_same = False
    #         break

    all_same = all(item == items[0] for item in items)
    return all_same

    # all

if __name__ == '__main__':
    run([1, 1, 1, 1, 1, 1])