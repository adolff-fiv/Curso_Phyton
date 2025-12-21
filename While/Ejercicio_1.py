#Suma dígitos de un número

Numerin  = int(input("Ingrese un número entero positivo por favor "))
Numero = Numerin
Suma = 0

if Numero < 0:
     Numero = Numero * -1

while Numero != 0:
     Digito = Numero % 10
     Suma += Digito
     Numero = Numero // 10

print("La suma de las cifras de", Numerin ,"es", Suma ,"")