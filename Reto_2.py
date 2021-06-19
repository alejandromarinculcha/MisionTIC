"""" Dos universidades están compitiendo por una beca para enviar a sus estudiantes a un intercambio universitario a otro país, para lo cual se realiza un concurso donde cada universidad postula a un grupo de n estudiantes. El primer grupo corresponde a los estudiantes de la universidad de San Vicente  y el segundo grupo de la universidad  Manizales.
Para la decisión de quienes serán los ganadores de la beca, el comité organizador hace un concurso que consiste en ir sacando letras de una balota. Si la letra sacada es igual a la letra inicial del nombre de algunos de los estudiantes del grupo, estos se anotan un punto.
Después de asignar las puntuaciones, estas se comparan, y si el primer grupo lleva más puntos que el segundo se escribe una S en un tablero. Si el segundo grupo lleva más puntos, entonces se anota una M, pero si hay empate se anotan una E.
Realizar un programa que reciba una cadena con las letras iniciales de los nombres de los estudiantes del primer grupo, otra cadena con  las letras iniciales de los nombres del segundo grupo, y una tercera cadena con el registro de todas las letras sacadas de la balota. El programa debe devolver la cadena de texto que se anotó en el tablero."""

estudiante_U_SanVIcente = input(
    "Ingrese las iniciales de los estudiantes de la U. San Vicente: ")
estudiante_U_Manizales = input(
    "Ingrese las iniciales de los estudiantes de la U. Manizales: ")
balotas = input("Ingrese las letras de las balotas: ")


def grupos(grupo1, grupo2):
    puntos_SV = 0
    puntos_M = 0
    for i in range(0, len(balotas)):
        if balotas[i] in grupo1:
            puntos_SV += 1
        if balotas[i] in grupo2:
            puntos_M += 1
        if (puntos_SV > puntos_M):
            categoria = ("S")
        elif (puntos_SV < puntos_M):
            categoria = ("M")
        elif(puntos_SV == puntos_M):
            categoria = ("E")
        print(categoria, end="")


grupos(estudiante_U_SanVIcente, estudiante_U_Manizales)
