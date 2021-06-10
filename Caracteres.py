# EJERCICIO 1
def conversion1(x):

    y = chr(x)

    if (y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u'):
        return("El número " + str(x) + " si corresponde al ascii de una vocal mínuscula que es " + y)
    else:
        return("El número " + str(x) + " No corresponde al ascii de una vocal mínuscula " + "corresponde a " + y)

x = int(input("Ingrese un número: "))

print(conversion1(x))


# EJERCICIO 2
def converison2():

    x = (input("Ingrese un carácter de longitud 1: "))

    y = ord(x)

    if (y % 2 == 0):
        print("El número:", y, "ES PAR")
    else:
        print("El número:", y, "ES IMPAR")

converison2()


# EJERCICIO 3
def conversion3(x):

    if (str.isdigit(x)):
        print("La cadena: " + x + " es un digito.")
    else:
        print("La cadena: " + x + " no es un digito.")


x = (input("Ingrese una cadena: "))

conversion3(x)


# EJERCICIO 4
def conversion4(a):
    if (str.isdigit(a) == True):
        print("USTED INGRESÓ NÚMEROS Y FUERON: " + a)
    else:
        print("USTED INGRESÓ ALGUNA PALABRA AQUÍ: " + a)

ingresar = input("Ingrese una cadena: ")
conversion4(ingresar)
