def mayor_edad(edad):
    if edad >= 18:
        print("ES MAYOR DE EDAD")
    else:
        print("NO ES MAYOR DE EDAD")


Edad_persona = int(input("Ingrese su edad: "))
mayor_edad(Edad_persona)

print("Y la edad es: " + str(Edad_persona) + " años" + ", recién cumplidos.")
print("Y la edad es:", Edad_persona, "años, recien cumplidos.")
