# Filtro de la primera letra de nombres

lista = input("Ingresa los nombres separados por comas y sin espacios ")
lista_sin_repetidos = list(set(lista.split(',')))
delimitador = input("Ingresa la primera letra que deben tener los nombres ")
resultado = filter(lambda x: str(x).startswith(delimitador), lista_sin_repetidos)
print(sorted(list(resultado)))
