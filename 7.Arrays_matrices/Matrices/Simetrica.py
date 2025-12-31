print("Ingresa el orden de la matriz a calcular")
filas, columnas = int(input()), int(input())

contador = 0

if filas == columnas:
    matrizA = []
    for i in range(filas):
        matrizA.append([0] * columnas)

    print("Ingrese la matriz ")
    for fil in range(filas):
        for col in range(columnas):
            matrizA[fil][col] = float(input(f'Ingresa la posición número {fil},{col} de la matriz '))

    for fil in range(filas):
        for col in range(columnas):
            normal = matrizA[fil][col]
            transpuesta = matrizA[col][fil]
            if normal == transpuesta:
                contador += 1
    if contador == (filas * columnas):
        print("La matriz sí es simétrica")
    else:
        print("La matriz no es simétrica")
else:
    print("La matriz no es simétrica")