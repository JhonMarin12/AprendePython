# ************************************
# FORMATEANDO A COLORES EN HEXADECIMAL
# ************************************


def run(intcolor: int) -> str:
  # TU CÓDIGO AQUÍ
  hexcolor = str(hex(intcolor)).upper()
  hexcolor = hexcolor[2:]
  return f"{hexcolor:0>6s}"


if __name__ == '__main__':
  print(run(4098423))
