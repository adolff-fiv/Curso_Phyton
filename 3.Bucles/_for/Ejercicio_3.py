#Suma de n pares e impares

N = int(input("Ingrese la cantidad de números que desee operar "))

Par = 0
Impar = 0
ContadorPar = 0
ContadorImpar = 0

for iterador in range(N):
    Números = int(input(f"Escriba el dato N.{iterador + 1} "))
    if Números % 2 == 0:
        Par += Números
        ContadorPar += 1
    else:
        Impar += Números
        ContadorImpar +=1

print("\n La suma de los números pares es", Par ,""
          "\n El cantidad de números pares es", ContadorPar ,""
          "\n La suma de los números impares es", Impar ,"" 
          "\n El cantidad de números impares es", ContadorImpar ,"")
          


