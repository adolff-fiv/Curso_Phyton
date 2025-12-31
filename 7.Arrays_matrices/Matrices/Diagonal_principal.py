print("Ingresa el orden de la matriz a calcular")
filas, columnas = int(input()), int(input())

diagonal = 0

if filas == columnas:
    matriz = []
    for i in range(filas):
        matriz.append([0] * columnas)

    print("Ingrese la matriz A")
    for fil in range(filas):
        for col in range(columnas):
            matriz[fil][col] = float(input(f'Ingresa la posición número {fil},{col} de la matriz '))
    
    for fil in range(filas):
        for col in range(columnas):
            if fil == col:
                diagonal += matriz[fil][col] 
    
    print(f'El valor de la diagonal principal es: {diagonal} ')
else:
    print("No es posible efectuar la multiplicación")
