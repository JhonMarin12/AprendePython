# *********************
# ENCONTRANDO ISOGRAMAS
# *********************
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def run(text: str) -> bool:
    # TU CÓDIGO AQUÍ

    is_isogram = True
    
    for i in list(ALPHABET):
      count = 0
      for j in list(text):
        if i == j:
          count += 1
        if count > 1:
          is_isogram = False
          break
          
    return is_isogram


if __name__ == '__main__':
    run('lumberjacks')