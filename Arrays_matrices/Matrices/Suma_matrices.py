import numpy as np

filas = int(input("Ingrese la cantidad de filas de las matrices "))
columnas = int(input("Ingrese la cantidad de columnas de las matrices "))

def crear_matrices(filas, columnas):
    f = -1 ; c = -1
    e_fil = []
    for i in range(0, filas):
        e_col = []
        f += 1
        for j in range(0, columnas):
            c += 1
            valor = int(input(f'Ingrese el valor del componente {i} , {j} => '))
            e_col.append(valor)
        e_fil.append(e_col)
    return e_fil

matrizA = np.array(crear_matrices(filas,columnas))
matrizB = np.array(crear_matrices(filas,columnas))

Suma = matrizA + matrizB
Resta = matrizA - matrizB
Multiplicacion = matrizA * matrizB

print(f'Suma de matrices \n{Suma} \n\n Resta de matrices \n{Resta} \n\n Multiplicación de matrices \n{Multiplicacion} ')