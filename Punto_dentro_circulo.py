# Función para determinar si un punto esta dentro del circulo con cento a,b

def estaEnCirculo(a, b, x, y, r):
    if (x > (a-r) and x < (a+r) and y > (b-r) and y < (b+r)):
        return ("Si esta dentro del circulo")
    else:
        return ("No esta dentro del circulo")


print(estaEnCirculo(2, 3, 2, 1, 2))
print(estaEnCirculo(2, 3, 2.5, 3.1, 2))
