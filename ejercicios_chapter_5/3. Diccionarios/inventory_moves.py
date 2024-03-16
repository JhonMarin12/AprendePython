# *************************
# MOVIMIENTOS DE INVENTARIO
# *************************


def run(imoves: str) -> dict:
    # TU CÓDIGO AQUÍ
    inventory = {}

    for i in imoves.split(','):
        if i[0] not in inventory:
            inventory[i[0]] = 0
        inventory[i[0]] += int(i[1:])

    return inventory


if __name__ == '__main__':
    run('A1,B4,A-2,A7,B1,C4')