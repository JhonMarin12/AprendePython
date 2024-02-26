# *************************
# DÍGITO DE CONTROL DEL NIF
# *************************


def run(nif: str) -> str:
  # TU CÓDIGO AQUÍ
  letters = 'TRWAGMYFPDXBNJZSQVHLCKE'
  resto = int(nif) % 23
  wnif = nif + letters[resto]

  return wnif


if __name__ == '__main__':
  run('78654355')
