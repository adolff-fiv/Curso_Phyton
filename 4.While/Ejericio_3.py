# Número secreto

import random

N = int(input("Ingrese un número entre 1 y 10 "))
NumeroSecreto = random.randint(1 , 10)
intentos = 0

if 0 <= N <= 10:
    while N != NumeroSecreto:
        print("¡Ja, ja! ¡Estás atrapado en mi ciclo ")
        intentos += 1
        N = int(input("Ingrese un número entre 1 y 10 "))
    print(NumeroSecreto)
    print("¡Bien hecho, muggle! eres libre ahora -> intentos:", intentos , "")  
else:
    print("El número debe estar entre 1 y 10.")
        
    




    