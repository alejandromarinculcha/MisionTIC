# Funcion para terminar si con los datos A, B y C se puede formar un triangulo

def si_forma_triangulo(a, b, c):
    if (a+b > c and a+c > b and b+c > a):
        return ("Los valores: "+str(a)+" , "+str(b)+" , "+str(c)+" Si forma un triángulo")
    else:
        return ("Los valores: "+str(a)+" , "+str(b)+" , "+str(c)+" No forma un triángulo")


A = float(input("Ingrese el primer valor: "))
B = float(input("Ingrese el segundo valor: "))
C = float(input("Ingrese el tercer valor: "))
print(si_forma_triangulo(A, B, C))
