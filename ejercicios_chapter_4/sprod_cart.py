# ***************************************
# PRODUCTO CARTESIANO EN CADENAS DE TEXTO
# ***************************************


def run(text1: str, text2: str) -> str:
  # TU CÓDIGO AQUÍ
  cartesian = ''

  for i in text1:
    for j in text2:
      cartesian = cartesian + i + j

  return cartesian


if __name__ == '__main__':
  run('xy', '$#')
