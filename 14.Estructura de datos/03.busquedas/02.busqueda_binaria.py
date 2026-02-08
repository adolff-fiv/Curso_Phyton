"""
    Búsqueda binaria

    Precondición lista ordenada
    Devuelve -1 si x no está en la lista
    Devuelve p tal que lista[p] ==  x, si x está en la lista
"""
def busqueda_binaria(lista, datos):
    izq = 0  # Guarda el índice del segmento
    der = len(lista)- 1 # Guarda el índice final del segmento

    # Un segmento es igual a vacío cuando izq > der:
    while izq <= der:
        medio = int((izq + der) / 2)

        if lista[medio] == datos:
            return medio
        
        # Si el valor del punto medio es mayor que el dato, sigue buscando en el segmento de la izquierda;
        # [izq, medio -i], descartando la derecha
        elif lista[medio] > datos:
            der = medio - 1

        # Si no, sigue buscando en el segmento de la derecha: [medio + 1, der], descartando la izquierda
        else:
            izq = medio + 1

    return None

def buscar(dato, lista):
    if busqueda_binaria(lista, dato) == None:
        return("El dato %d no se encontró en el arreglo" % (dato))
    else:
        return(f"El dato {dato} está en la posición {busqueda_binaria(lista, dato)}")
    
lista = [1, 3, 4, 6, 7, 8, 9, 13, 15, 16, 19]
    
print(buscar(13, lista))  