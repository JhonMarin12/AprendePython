# ********************
# DESCIFRANDO CIUDADES
# ********************


def run(cinfo: str) -> dict:
    # TU CÓDIGO AQUÍ
    cities = {}
    seeparate_info = cinfo.split(';')
    for i in seeparate_info:
        aux = i.split(':')
        cities[aux[0]] = int(aux[1])

    return cities


if __name__ == '__main__':
    run('Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;Mumbai:21_357_000')


