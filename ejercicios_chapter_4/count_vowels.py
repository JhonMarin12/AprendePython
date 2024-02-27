# ****************
# CONTANDO VOCALES
# ****************


def run(text: str) -> int:
  num_vowels = 0  
  for i in text.lower():
    if i in "aeiouáéíóú":
      num_vowels +=1
    else:
      continue
  return num_vowels


if __name__ == '__main__':
    run('El camión chocó contra el árbol')