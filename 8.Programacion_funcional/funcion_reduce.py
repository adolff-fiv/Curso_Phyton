# Reduce hace todos los posibles valores en uno solo y solo ese lo retorna

from functools import reduce

"Ejercicio sin usar lambda"

def add(a, b):
    return a + b

numeros = [2, 4, 7, 3]
print(reduce(add, numeros))

"Ejercicio usando lambda"

numeros = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, numeros ))
print("Con valor inicial:" + str(reduce(lambda x, y: x + y, numeros, 10)))