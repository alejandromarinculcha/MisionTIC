# Determina si todas las claves se encuentran en otro diccionario

def buscarClave(cl, dic):  # mira si una clave dada esta en el diccionario
    if cl in dic:
        return True
    else:
        return False


def buscarTodas(dic1, dic2):
    for key in dic1:
        if (buscarClave(key, dic2)) == True:
            print(key+" si esta")
            print()
        else:
            print(key + " No esta")
            print()


d1 = {'manzana': 430, 'bananas': 312,
      'naranjas': 525, 'peras': 217, 'aguacate': 13}
d2 = {'manzana': 400, 'bananas': 312,
      'naranjas': 525, 'mango': 217, 'peras': 217}
buscarTodas(d1, d2)
