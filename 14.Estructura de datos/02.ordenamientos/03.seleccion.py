lista = [4, 2, 5, 1, 8, 7]

for i in range(len(lista)):
    minimo = i
    for x in range(i, len(lista)):
        if lista[x] < lista[minimo]:
            minimo = x
    aux = lista[i]
    lista[i] = lista[minimo]
    lista[minimo] = aux
