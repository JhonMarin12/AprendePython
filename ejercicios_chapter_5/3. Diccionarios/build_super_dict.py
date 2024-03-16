# ***************************
# DICCIONARIO EN CONSTRUCCIÓN
# ***************************


def run(items: list) -> dict:
    # TU CÓDIGO AQUÍ
    
    
    unpack_items = {}
    for i in items:
        first_element = i[0]
        rest_of_list = i[1:]
        unpack_items[first_element] = rest_of_list
        

    return unpack_items


if __name__ == '__main__':
    run([['Episode IV - A New Hope', 'May 25', 1977, 'George Lucas'], ['Episode V - The Empire Strikes Back', 'May 21', 1980], ['Episode VI - Return of the Jedi', 'May 25', 1983]])