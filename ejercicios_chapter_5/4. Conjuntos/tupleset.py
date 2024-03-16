# ******************
# TUPLAS Y CONJUNTOS
# ******************


def run(input: tuple) -> tuple:
    # TU CÓDIGO AQUÍ
    
    primer_conjunto = set()
    segundo_conjunto = set()

    for i in input:
        primer_conjunto.add(i[0])
        segundo_conjunto.add(i[1])  

    output = (primer_conjunto, segundo_conjunto)  
    return output


if __name__ == '__main__':
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))