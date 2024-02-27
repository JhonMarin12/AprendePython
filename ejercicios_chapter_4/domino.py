i = 0
j = 0
aux = 7
while i < 7:
  j = 0
  while j<aux:
    print(f"{j}|{i}", end=" ")
    j +=1
  print("\n")
  i += 1
  aux -=1