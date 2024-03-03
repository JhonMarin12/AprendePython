# ***************
# UN SET AL TENIS
# ***************


def run(points: str) -> tuple:
  games_player1 = 0
  games_player2 = 0
  points_player1 = 0
  points_player2 = 0
  for i in points:
    if i == 'A':
      points_player1 += 1
    else:
      points_player2 += 1

    if (points_player1 >= 6 or points_player2 >= 6):
      if points_player1 > points_player2:
        if points_player1 - points_player2 >= 2:
          
        games_player1 += 1
        points_player1 = points_player2 = 0
      else:
        games_player2 += 1
        points_player1 = points_player2 = 0

  return games_player1, games_player2

#REVISAR TEORIA JUEGOS DE TENNIS

if __name__ == '__main__':
  run('AABBAABABBBABABABBBAAABBBABAABBABBAABBBABABBAAAABBBBABBBAB')
