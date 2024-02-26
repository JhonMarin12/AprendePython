# ******************
# ÁREA DE UN CÍRCULO
# ******************


def run(radius: float) -> float:
  # TU CÓDIGO AQUÍ
  radius_squared = radius**2
  
  area = 3.14 * radius_squared

  return area


if __name__ == '__main__':
  run(4)
