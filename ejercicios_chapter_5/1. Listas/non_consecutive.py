# *******************
# NO ERES CONSECUTIVO
# *******************


def run(values: list) -> int:
    # TU CÓDIGO AQUÍ
    
    if len(values) == 0 or len(values) == 1:
        target = None
    else:
        first = values[0]
        for i in values:
            if i == first:
                continue
            else:
                target = i
                break
            first+=1

    return target


if __name__ == '__main__':
    run([1, 2, 3, 4, 6, 7, 8])