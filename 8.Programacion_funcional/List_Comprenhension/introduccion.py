# Crear un array que almacene los valores pares multiplicados entre si en un rango determinado

rango = range(10)
lista = []

for num in rango:
    if num % 2 == 0:
        lista.append(num * num)

print(f'La lista de pares al cuadrado: {lista}')

lista = []
lista = [num * num for num in rango if num % 2 == 0]
print(f'La lista de pares usando list comprehension: {lista}')