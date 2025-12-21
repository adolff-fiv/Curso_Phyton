array = [20, 15, 12, 11, 8, 4, 1]

max = 20
min = max

for i in array:
    if i < min:
        min = i

print(f'el número menor del arreglo es {min} ')

array.remove(min)

"""Mi método"""
#contador = 0
#suma = 0
#for j in array:
#    suma += j
#    contador += 1
#    if contador == 6:
#        suma = suma / 6

"""Método más eficiente"""

suma = 0
for j in array:
    suma += j


print(f'El promedio del arreglo es {suma/len(array)}')