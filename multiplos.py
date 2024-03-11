limite = int(input("Ingrese valor: "))
x = 0
while x <= limite:
    if x % 5 == 0:
        print(x, end=', ')
    x += 1
