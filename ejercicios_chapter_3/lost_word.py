# ******************
# LA PALABRA PERDIDA
# ******************


def run(text: str, target_word: str, replace_word: str) -> str:
  # TU CÓDIGO AQUÍ
  index_found = text.index(target_word)
  len_word = len(target_word)
  first = text[:index_found]
  second = text[index_found + len_word:]

  mtext = first + replace_word +second

  return mtext


if __name__ == '__main__':
  run('This is a beautiful night on the Atlantic', 'beautiful', 'terrible')
