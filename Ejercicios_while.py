# Función para ingresar número NO negativas y encontrar su cuadrado.
from os import sep


def cuadrado():
    x = int(input("Ingrese número: "))
    while (x > 0):
        print(x*x)
        x = int(input("Ingrese número: "))


cuadrado()


# Función que debe ingresar un número y realizar una operación según el tipo del número


def parImpar():
    n = int(input("Ingrese un número: "))
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        print(n, end=" ")


parImpar()


# Función que imprime el año en que la población B superará la población A


def crecimiento():
    A = int(input("Ingrese la población de A: "))
    B = int(input("Ingrese la población de B: "))

    año = 2022
    while A >= B:
        A = A + A*0.02
        B = B + B*0.03
        año = año + 1
    print("La poblacón de B superó a la población de A en el año", año)


crecimiento()
