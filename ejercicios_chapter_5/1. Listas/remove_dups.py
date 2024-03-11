# *********************
# ELIMINANDO DUPLICADOS
# *********************


def run(nums_dups: list) -> list:
    # TU CÓDIGO AQUÍ
    nums_unique = []

    for i in nums_dups:
        if i not in nums_unique:
            nums_unique.append(i)

    return nums_unique


if __name__ == '__main__':
    run([2, 3, 2, 2, 1, 5, 4, 2, 4, 9])