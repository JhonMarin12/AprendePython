# ******************
# AGRUPANDO PALABRAS
# ******************


def run(words: list) -> dict:
    # TU CÓDIGO AQUÍ
    group_words = {}

    for i in words:
        letter_intial = i[0]
        if letter_intial not in group_words:
            group_words[letter_intial] = []
        group_words[i[0]].append(i)

    return group_words


if __name__ == '__main__':
    run(['mesa', 'móvil', 'barco', 'coche', 'avión', 'bandeja', 'casa', 'monitor', 'carretera', 'arco'])  # noqa: E501