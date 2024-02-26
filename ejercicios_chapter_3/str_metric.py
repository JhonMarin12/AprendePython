# ********************************
# UNA MÉTRICA PARA CADENA DE TEXTO
# ********************************


def run(text: str) -> int:
  # TU CÓDIGO AQUÍ
  metric = len(text) * (text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u'))

  return metric


if __name__ == '__main__':
  run('ordenador')
