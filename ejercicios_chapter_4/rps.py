# **********************
# PIEDRA, PAPEL O TIJERA
# **********************


def run(choice1: str, choice2: str) -> int:
  # TU CÓDIGO AQUÍ
  choice1 = choice1.lower()
  choice2 = choice2.lower()

  if choice1 == choice2:
    winner = 0
  elif (choice1 == 'piedra' and choice2 == 'tijera') or (choice1 == 'tijera' and choice2 == 'papel') or (choice1 == 'papel' and choice2 == 'piedra'):
    winner = 1
  else:
    winner = 2

  return winner


if __name__ == '__main__':
  run('piedra', 'PAPEL')
