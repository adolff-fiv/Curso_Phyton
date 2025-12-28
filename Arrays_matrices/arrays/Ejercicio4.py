# Analizar si un número del arreglo es igual a la suma de los demás

array = []
tamaño = int(input("Ingrese el tamaño del arreglo "))
suma = 0
n = -1

for i in range(tamaño):
    dato = int(input("Ingrese un número "))
    array.append(dato)
    suma += array[i]
    
    if array[i] == suma:    
        n = suma

if n != -1:
    print(f'El número {n} es igual a la suma del resto de números')
else:
    print("Ningún numero cumple con las condiciones requeridas")
