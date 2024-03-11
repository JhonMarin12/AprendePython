# ***************
# CONTANDO LETRAS
# ***************


def run(sentence: str) -> dict:
    # TU CÓDIGO AQUÍ
    counter = {}

    for i in sentence:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1

    return counter


if __name__ == '__main__':
    run('boom')

