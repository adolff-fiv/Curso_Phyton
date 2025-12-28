print("Ingrese el orden de la matriz A")
filaA, columnaA = int(input()), int(input())

print("Ingrese el orden de la matriz B")
filaB, columnaB = int(input()), int(input())

if columnaA == filaB:
    matrizA = []
    for i in range(filaA):
        matrizA.append([0] * columnaA)

    matrizB = []
    for j in range(filaB):
        matrizB.append([0] * columnaB)
    
    print("Ingrese la matriz A")
    for fil in range(filaA):
        for col in range(columnaA):
            matrizA[fil][col] = float(input(f'Ingresa la posición número {fil},{col} de la matriz A '))

    print("Ingrese la matriz B")
    for fil in range(filaB):
        for col in range(columnaB):
            matrizB[fil][col] = float(input(f'Ingresa la posición número {fil},{col} de la matriz B '))

    matrizC = []
    for l in range(filaA):
        matrizC.append([0] * columnaB)

    for i in range(filaA):
        for j in range(columnaB):
            for l in range(filaB):  
                matrizC[i][j] += matrizA[i][l] * matrizB[l][j]

    print('\nLa matriz resultante es:')
    for i in matrizC:
        print(i)
else:
    print("No es posible efectuar la multiplicación")