# **************
# POTENCIAS DE 2
# **************


def run(num_powers: int) -> list:
    # TU CÓDIGO AQUÍ
    powers2 = [2**x for x in range(num_powers+1)]

    return powers2


if __name__ == '__main__':
    run(0)