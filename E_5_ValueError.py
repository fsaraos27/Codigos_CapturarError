# Captura de error de la funcion con elemento existente.

def agregar_una_vez(lista, elemento):
    if elemento in lista:
        try:
	        raise ValueError('ya existe')
        except ValueError:
            print('Se encuentra en la lista')
    else: 
	    lista.append(elemento)
    return lista

lista = [1,2,3,4]
ele = 7

print(agregar_una_vez(lista, ele))