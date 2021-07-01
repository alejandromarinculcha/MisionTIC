# ¡AQUI SE REPITE DE MANERA INFINITA!
"""
while True:
    pastrana = int(input("Ingrese los años del colegio pastrana: "))
    sanmiguel = 2*pastrana+4
    esperanza = (pastrana+sanmiguel)//5

    def categoria():

        if 0 < esperanza <= 20:
            return "UNO"
        else:
            if 20 < esperanza <= 30:
                return "DOS"
            else:
                if 30 < esperanza <= 50:
                    return "TRES"
                else:
                    return "CUATRO"
    print(pastrana, sanmiguel, esperanza, "\n", categoria())
"""

# MANERA 1 (ESTE FUE EL QUE ENTREGUÉ)
"""
if 0 < esperanza <= 20:
    print(pastrana, sanmiguel, esperanza, "\nuno")
else:
    if 20 < esperanza <= 30:
        print(pastrana, sanmiguel, esperanza, "\ndos")
    else:
        if 30 < esperanza <= 50:
            print(pastrana, sanmiguel, esperanza, "\ntres")
        else:
            print(pastrana, sanmiguel, esperanza, "\ncuatro")
"""

# MANERA 2
"""
def categoria():

    if 0 < esperanza <= 20:
        return "UNO"
    else:
        if 20 < esperanza <= 30:
            return "DOS"
        else:
            if 30 < esperanza <= 50:
                return "TRES"
            else:
                return "CUATRO"

print(pastrana, sanmiguel, esperanza, "\n", categoria())
"""

# MANERA 3
"""
pastrana = int(input("Ingrese los años del colegio pastrana: "))
sanmiguel = 2*pastrana+4


def categoria(e):

    if 0 < e <= 20:
        return "UNO"
    else:
        if 20 < e <= 30:
            return "DOS"
        else:
            if 30 < e <= 50:
                return "TRES"
            else:
                return "CUATRO"


esperanza = (pastrana+sanmiguel)//5

print(pastrana, sanmiguel, esperanza, "\n", categoria(esperanza))
"""

# MANERA 4, ELIGE ALEATORIAMENTE NÚMEROS DADOS

import random
pastrana = ("30", "20", "36", "32", "12", "214", "12", "5",
            "2", "100", "73", "62", "20")

pastrana2 = int(random.choice(pastrana))
sanmiguel = 2*pastrana2+4


def categoria(e):

    if 0 < e <= 20:
        return "UNO"
    else:
        if 20 < e <= 30:
            return "DOS"
        else:
            if 30 < e <= 50:
                return "TRES"
            else:
                return "CUATRO"


esperanza = (pastrana2+sanmiguel)//5

print(pastrana2, sanmiguel, esperanza, "\n", categoria(esperanza))
