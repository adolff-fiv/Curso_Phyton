""" while 1 == 1:
     print("Hola") """

# Contador = 0
# while Contador < 8:
#     print("El número se encuentra entre 3 y 8")
#     Contador += 1

Número = int(input("Ingrese un número "))
Sumatoria = 0

while Número != 0:
    Sumatoria += Número
    Número = int(input("Ingrese otro número "))
print("La sumatoria es", Sumatoria , "" )
