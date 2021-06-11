# La función me indica en qué cuadrante del plano cartesiano se encuentran las coordenadas X y Y dadas.

def cuadrante(x, y):
    if (x > 0 and y > 0):
        return ("Las coordenadas: " + str(x) + " , " + str(y) + " son del cuadrante 1 del plano cartesiano")
    elif (x < 0 and y > 0):
        return ("Las coordenadas: " + str(x) + " , " + str(y) + "  son del cuadrante 2 del plano cartesiano")
    elif (x < 0 and y < 0):
        return ("Las coordenadas: " + str(x) + " , " + str(y) + "  son del cuadrante 3 del plano cartesiano")
    elif (x > 0 and y < 0):
        return ("Las coordenadas: " + str(x) + " , " + str(y) + "  son del cuadrante 4 del plano cartesiano")
    else:
        return ("Las coordenadas: " + str(x) + " , " + str(y) + " estan en el origen")


X = float(input("Ingrese la coordenada X: "))
Y = float(input("Ingrese la coordenada Y: "))
print(cuadrante(X, Y))
