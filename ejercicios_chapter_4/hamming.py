# *****************
# DISTANCIA HAMMING
# *****************


def run(text1: str, text2: str) -> int:
  dhamming = 0

  for i in range(len(text1)):
    are_equasl = text1[i] == text2[i]
    if are_equasl:
      continue
    else:
      dhamming += 1

  return dhamming


if __name__ == '__main__':
  run('0001010011101', '0000110010001')
