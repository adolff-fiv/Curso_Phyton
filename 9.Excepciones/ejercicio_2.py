# Excepción en una lista 

lista = [1, 2, 3, 4, 5, 6, 7, 8]

def agregar_una_vez(lista, el):
    try:
        lista.append(el)
        return(set(lista))
    except:
        raise(ValueError)
    
try:
    lista_2 = agregar_una_vez(lista, 9)
except ValueError as Ve:
    print(f'Ha ocurrido un error del tipo {Ve}')
finally:
    print(lista_2)