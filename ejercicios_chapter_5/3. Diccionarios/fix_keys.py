# ********************
# LA CLAVE ES LA CLAVE
# ********************


def run(items: dict) -> dict:
    # TU CÓDIGO AQUÍ
    fitems = {clave.replace(' ', '') : valor for clave, valor in items.items()}
    

    
    return fitems


if __name__ == '__main__':
    run({'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']})