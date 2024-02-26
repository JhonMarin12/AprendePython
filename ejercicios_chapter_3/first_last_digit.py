# ****************************************
# ENCONTRANDO EL PRIMER Y EL ÚLTIMO DÍGITO
# ****************************************


def run(text: str) -> tuple:
  # TU CÓDIGO AQUÍ
  numbers = list(filter(str.isdigit, text))
  #Revisar se supone no se deberian usar conceptos
  #Avanzados como las listas o filtros, solo la
  #Manipulacion de cadenas de texto
  first_digit = int(numbers[0])
  last_digit = int(numbers[-1])

  return first_digit, last_digit


if __name__ == '__main__':
  print(run('1abc2'))
