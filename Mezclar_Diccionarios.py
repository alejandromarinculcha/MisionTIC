def buscarClave(cl, dic):  # mira si una clave dada esta en el diccionario
    if cl in dic:
        return True
    else:
        return False

# Une los dos diccionario, si slgun elemento del segundo diccionario ya esta en el primero, se conserva el valor del primero


def mezclar(dic1, dic2):
    for k, v in dic2.items():  # saca la clave y valor de dic2
        if (buscarClave(k, dic1)) == False:
            dic1[k] = v
    return(dic1)


d1 = {'manzana': 430, 'bananas': 312,
      'naranjas': 525, 'peras': 217, 'aguacate': 13}
d2 = {'manzana': 400, "papaya": 500}

print(mezclar(d1, d2))
