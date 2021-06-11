# Función para determinar si un número es positivo, negativo o neutro.

def positivoOnegativo(numero):

    if (numero > 0):
        return ("El número " + str(numero) + ", es POSITIVO")
    elif (numero < 0):
        return ("El número " + str(numero) + ", es NEGATIVO")
    else:
        return ("El número: " + str(numero) + ", es el NEUTRO PARA LA SUMA")


numerofinal = float(input("Ingrese el número a evaluar: "))
print(positivoOnegativo(numerofinal))
