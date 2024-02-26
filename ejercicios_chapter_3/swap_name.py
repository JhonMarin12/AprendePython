# ****************
# NOMBRE VICEVERSA
# ****************


def run(fullname: str) -> str:
  # TU CÓDIGO AQUÍ
  swap = fullname.find(" ")
  
  swapname =  fullname[swap+1:] +" "+ fullname[:swap] 

  return swapname


if __name__ == '__main__':
  print(run('John McClane'))
