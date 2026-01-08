# map(funcion, iterable)

"""Sin utilizar lambda"""

def letra_A(x):
    return x[0] == "A"

frutas = ["Platano","Arándano","Piña","Manzana","Pera"]
objeto = map(letra_A, frutas)
print(list(objeto))

"Utilizando lambda"

frutas = ["Platano","Arándano","Piña","Manzana","Pera"]
objeto_map = map(lambda x: x[0] == "A", frutas)
print(list(objeto_map))