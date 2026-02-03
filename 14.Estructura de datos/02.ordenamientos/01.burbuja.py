lista = [100, 50, 20, 10, 8, 4, 2] 

for i in range(len(lista)): # Evalúa las pasadas
    for x in range(len(lista) - 1): # Evalúa los elementos en cada pasada
        if lista[x] > lista[x + 1]:
            aux = lista[x]
            lista[x] = lista[x + 1]
            lista[x + 1] = aux
    print(lista)