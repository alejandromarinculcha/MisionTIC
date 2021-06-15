# Función que solicita al usuario un número hasta que ese número este fuera de las letras mayúsculas en el código ASCII
def conversion():

    valor_entero = 64
    while (valor_entero < 65 or valor_entero > 90):
        valor_entero = int(input("Ingrese valor entero: "))
    return "Se ingresó letra mayúcula"


print(conversion())
