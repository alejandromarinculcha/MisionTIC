# Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

x = 1
while (x <= 100):
    print(x, (x**2))
    x += 1


# Imprimir un listado con los números del 100 al 1 cada uno con su respectivo cuadrado.

x = 100
while (x >= 1):
    print(x, (x**2))
    x -= 1


# Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n>= 2 dado.

x = int(input("Ingrese número: "))
if (x % 2 == 0):
    while x >= 2:
        print(x)
        x -= 2
else:
    print("NO INGRESÓ NÚMERo PAR")
