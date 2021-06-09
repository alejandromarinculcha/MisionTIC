pastrana = int(input("Ingrese los años del colegio pastrana "))
sanmiguel = 2*pastrana+4
esperanza = (pastrana+sanmiguel)//5

if 0 < esperanza <= 20:
    print(pastrana, sanmiguel, esperanza, "\n uno")
else:
    if 20 < esperanza <= 30:
        print(pastrana, sanmiguel, esperanza, "\n dos")
    else:
        if 30 < esperanza <= 50:
            print(pastrana, sanmiguel, esperanza, "\n tres")
        else:
            print(pastrana, sanmiguel, esperanza, "\n cuatro")
