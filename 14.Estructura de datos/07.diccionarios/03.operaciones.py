from pprint import pprint as pp
diccionario = {"Nombre": "Adolf"}

# Método get recupera una llave y en caso de que no exista no lanza excepciones
# Además, podemos regresar un mensaje o un valor en caso de que no exista la llave
print(diccionario.get("Nombre", "No se encontró la llave"))

# SetDefault modifica el diccionarios, además un valor por defecto
apellido = diccionario.setdefault("Apellido", "Paredes")
print(apellido)
print(diccionario)

# Imprimiendo con pprint
pp(diccionario, sort_dicts=False)

# Imprimiendo con for 
for valor in diccionario.values():
    print(valor)

for key in diccionario.keys():
    print(key)

for key, valor in diccionario.items():
    print(key, valor)

print("\n\n".center(50, "-"))

d = {"uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5}
print(d)

# Eliminar valor del diccionario
d.pop("dos")
print(d)

# Eliminar elementos con PopItem() (Elimina el último elemento)
d.popitem()
print(d)

# Eliminar con del
del d["tres"]
print(d)

# Consultar la longitud del diccionario
print(len(d))

# Eliminar el diccionario
d.clear()
print(d)