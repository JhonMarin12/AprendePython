# ***************
# PALABRA DIVERSA
# ***************


def run(words: list) -> str:
    # TU CÓDIGO AQUÍ
    dword = words[0]
    for i in words:
        if len(set(dword)) <= len(set(i)):
            dword = i


    return dword


if __name__ == '__main__':
    run(['dictionary', 'turtle', 'flexibility', 'humanity'])