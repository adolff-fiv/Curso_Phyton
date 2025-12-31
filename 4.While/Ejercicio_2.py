#Suma de los dígitos de varios números

Numerin  = int(input("Ingrese un número entero positivo por favor (-1 para detener el programa) "))
Numero = Numerin
Pares = 0

while Numerin != -1:
     Numero = Numerin
     if Numero % 2 == 0:
        Pares += 1
     
     Suma = 0
     if Numero < 0:
            Numero = Numero * -1

     while Numero != 0:
            Digito = Numero % 10
            Suma += Digito
            Numero = Numero // 10

     print("La suma de las cifras de", Numerin ,"es", Suma ,"")
     Numerin  = int(input("Ingrese un número entero positivo por favor (-1 para detener el programa) ")) 

print("Existen", Pares, "numeros pares")

