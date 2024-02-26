# *************************
# LA MULTIPLICACIÓN DE JACK
# *************************


def run(n: int) -> int:
  # TU CÓDIGO AQUÍ
  number_digits = len(str(n).lstrip("-"))
  result = n * 5**number_digits

  return result


if __name__ == '__main__':
  run(3)
