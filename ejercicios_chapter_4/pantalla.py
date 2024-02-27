tamaño = int(input("Entrada: "))

for i in range(tamaño):
  for j in range(tamaño):
    if i == j:
      print("X",end=" ")
    elif i < j:
      print("U", end=" ")
    else:
      print("D", end=" ")
  print("\n")