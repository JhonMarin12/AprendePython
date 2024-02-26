# *********************
# ENCUENTRA LA INTEGRAL
# *********************


def run(symbol: str) -> str:
  # TU CÓDIGO AQUÍ
  coma = symbol.find(",")
  exponente = int(symbol[coma+1:])+1
  coeficiente = int(symbol[:coma])/exponente
  integral = f"{coeficiente:.0f}x^{exponente}"

  return integral


if __name__ == '__main__':
  run('3,2')
