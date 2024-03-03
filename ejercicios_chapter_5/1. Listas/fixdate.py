# ********************
# REORGANIZANDO FECHAS
# ********************


def run(input_date: str, base_year: int) -> str:
    # TU CÓDIGO AQUÍ
    date = input_date.split('/')
    output_date = f"{int(date[1]):02}-{int(date[0]):02}-{int(date[2]) + base_year}"

    return output_date


if __name__ == '__main__':
    run('12/31/23', 2000)
