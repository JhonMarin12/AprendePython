# *****************
# UN JUEGO AL TENIS
# *****************


def run(points: str) -> str:

  winner = 'output'
  a_score = 0
  b_score = 0
  for i in points:
    if i == 'A':
      a_score += 1
    else:
      b_score += 1

  winner = 'A' if a_score > b_score else 'B'
  
  return winner


if __name__ == '__main__':
  run('ABAABA')
