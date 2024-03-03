# ******************
# TODO EN ALFABÉTICO
# ******************

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def run(text: str) -> bool:
    # TU CÓDIGO AQUÍ
    isalpha = True

    for i in text.lower():
      if i not in ALPHABET:
        isalpha = False
        break

    return isalpha


if __name__ == '__main__':
    run('hello-world')