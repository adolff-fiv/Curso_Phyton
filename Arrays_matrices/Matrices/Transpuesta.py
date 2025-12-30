print("Ingresa el orden de la matriz a calcular")
filas, columnas = int(input()), int(input())

matrizA = []
for i in range(filas):
    matrizA.append([0] * columnas)

print("Ingrese la matriz A")
for fil in range(filas):
    for col in range(columnas):
        matrizA[fil][col] = float(input(f'Ingresa la posición número {fil},{col} de la matriz '))

print('\nMatriz inicial')
for i in matrizA:
    print(i)

matrizB = []
for i in range(columnas):
    matrizB.append([0] * filas)

for fil in range(columnas):
    for col in range(filas):
        matrizB[fil][col] = matrizA[col][fil]

print('\nMatriz inversa')
for i in matrizB:
    print(i)
