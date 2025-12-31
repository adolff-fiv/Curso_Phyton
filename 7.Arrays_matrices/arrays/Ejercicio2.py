#Quitar el menor número de un arreglo y calcular su promedio

array = []
tamaño = int(input("Ingrese el tamaño del arreglo "))

for i in range(tamaño):
    array.append(int(input("Ingrese un número ")))

minimo = min(array)
array.remove(minimo)

print(f'El dato menor del arreglo es {minimo}')

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

print(f'El promedio del arreglo sin la nota más baja es {suma/len(array)}')