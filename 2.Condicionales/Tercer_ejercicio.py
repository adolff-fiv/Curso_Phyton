# Encontrar y calcular el Domingo de Pascua

Year = int(input("Ingrese un año por favor "))

#Algoritmo de Gauss

A = Year % 19
B = Year % 4
C = Year % 7
D = (19 * A + 24) % 30
E = (2 * B + 4 * C  + 6 * D + 5) % 7
N = (22 + D + E)

# 

print("El domingo de Pascua cae el ", N, " de marzo") if N <= 31 else print("El domingo de Pascua cae el ", N - 31, " de Abril")