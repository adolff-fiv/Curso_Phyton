""" Programa de dos listas y la relación entre sí  """

# Primer lista
lista1 = []
respuesta = str(input("¿Desea agregar elementos a la lista 1? (s/n) "))

while respuesta == "S" or respuesta == "s":
    lista1.append(str(input("Ingrese una palabra a la lista ")))
    respuesta = str(input("¿Desea agregar elementos a la lista 1? (s/n) "))
print("Los elementos que ha ingresado a la lista 1 son", lista1)

# Segunda lista
lista2 = []
respuesta = str(input("¿Desea agregar elementos a la lista 2? (s/n) "))

while respuesta == "S" or respuesta == "s":
    lista2.append(str(input("Ingrese una palabra a la lista ")))
    respuesta = str(input("¿Desea agregar elementos a la lista 2? (s/n) "))
print("Los elementos que ha ingresado a la lista 2 son", lista2)

# Unión
union = list(sorted(set(lista1) | set(lista2)))
print("Los elementos de ambas listas son:", union)

# Solo A
soloA = list(sorted(set(lista1) - set(lista2)))
print("Los elementos que solo aparecen en la primera lista son:", soloA)

# Solo B
soloB= list(sorted(set(lista2) - set(lista1)))
print("Los elementos que solo aparecen en la segunda lista son:", soloB)

# Intersección
interseccion = list(sorted(set(lista1) & set(lista2)))
print("Los elementos que solo aparecen en ambas listas son:", interseccion, "\n")