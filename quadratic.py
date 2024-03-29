# *************************
# ECUACIÓN DE SEGUNDO GRADO
# *************************


def run(a: int, b: int, c: int) -> tuple:
  # TU CÓDIGO AQUÍ
  x1 = x2 = 'output'
  discriminate = b**2 - 4 * a * c

  x1 = (-b + discriminate**0.5) / (2 * a)
  x2 = (-b - discriminate**0.5) / (2 * a)

  return x1, x2


if __name__ == '__main__':
  run(4, -6, 2)
