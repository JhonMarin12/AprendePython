# *******************
# APROXIMANDO EL SENO
# *******************


def run(x: float) -> float:
  numerador = 4 * x * (180 - x)
  denominador = 40500 - x * (180 - x)
  sin = numerador/denominador


  return sin


if __name__ == '__main__':
    run(90)