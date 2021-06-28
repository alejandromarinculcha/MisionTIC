# Desarrollar un programa que dada una listas de personas, imprima los nombres y apellidos de las personas que están en un rango de edades.
while True:
    Nombre = {}
    Nombre["Nombre"] = input("Ingrese nombre: ")

    Apellido = {}
    Apellido["Apellido"] = input("Ingrese apellidos: ")

    Edad = {}
    Edad["Edad"] = input("Ingrese edad: ")

    Completo = {}
    Edad.update(Completo)
    Apellido.update(Edad)
    Nombre.update(Apellido)

    print(Nombre)
