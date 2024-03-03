# *********************************
# COMPROBANDO IGUALDAD DE POTENCIAS
# *********************************


def run(n: int) -> tuple:
  # TU CÓDIGO AQUÍ
  left_side = right_side = 0

  for i in range(1, n + 1):
    left_side += i
    right_side += i**3
  return left_side**2, right_side


if __name__ == '__main__':
  run(1)
