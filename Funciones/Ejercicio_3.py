#Factorial de un número

def factorial(X):
    f = 1
    if X != 0:
        for i in range (1, X + 1):
            f = f * i
    return f

numero = 0

Dato =  int(input("Ingrese un número porfavor o 0 si desea parar "))
while Dato != 0:
    print(f'El factorial de {Dato} = {factorial(Dato)}')
    Dato =  int(input("Ingrese un número porfavor o 0 si desea parar "))
    numero += 1
    if Dato == 0:
        break
print(f'La cantidad de números digitados es {numero}')

