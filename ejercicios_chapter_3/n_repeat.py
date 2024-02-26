# *************
# SUMA REPETIDA
# *************


def run(n: int) -> int:
  # TU CÓDIGO AQUÍ
  aux = str(n)
  result = int(aux) + int(aux*2) + int(aux*3)

  return result


if __name__ == '__main__':
  run(3)
