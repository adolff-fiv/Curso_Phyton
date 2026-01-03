"""
def funcion():
    arry = [1,2,3]
    return arry

arr2 = funcion()
print(arr2[0])
"""
def generador():
    yield 1
    print("Reanundando la ejecución")
    yield 2
    valor1 = 5
    valor2 = 7
    suma = valor1 + valor2
    yield suma


gen = generador()
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))

for valor in generador():
    print(f'Valor devuelto {valor}')
"""gen2 = generador()

print(next(gen2))"""
