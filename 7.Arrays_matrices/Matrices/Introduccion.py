matriz3X3 = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

punto = matriz3X3[1][2]
print(punto)

print(matriz3X3[2][0])

#Suma de los elementos de la matriz
Suma = 0
for i in range(len(matriz3X3)):
    for j in range(len(matriz3X3)):
        Suma += matriz3X3[i][j]

print(Suma)
