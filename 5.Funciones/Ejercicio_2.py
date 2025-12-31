#Sumando números primos
def primo(numero):
    n = int(2)
    band = True

    while band and (n < numero):
        if numero % n == 0:
            band == False
        else:
            n += 1
            
    return band 
    
acumulador = 0

while True:
    numero = int(input("Ingrese un número primo o 0 para salir "))
    if numero == 0:
        break
    if primo(numero):
        acumulador += numero

print(f'La sumatoria de números primos es  {acumulador}') 



