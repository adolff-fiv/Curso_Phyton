import numpy as np

print("Ingresa el orden de la matriz a calcular")
filas, columnas = int(input()), int(input())

matrizA = []
for i in range(filas):
    matrizA.append([0] * columnas)

print("Ingrese la matriz")
for fil in range(filas):
    for col in range(columnas):
        matrizA[fil][col] = float(input(f'Ingresa la posición número {fil},{col} de la matriz '))

determinante = np.linalg.det(matrizA)
print(determinante)