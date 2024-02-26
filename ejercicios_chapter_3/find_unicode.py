# ********************
# ENCUENTRE EL UNICODE
# ********************


def run(source_char: str, offset: int) -> str:
    # TU CÓDIGO AQUÍ
    target_char = chr(ord(source_char) + offset)

    return target_char


if __name__ == '__main__':
    run('δ', -2)