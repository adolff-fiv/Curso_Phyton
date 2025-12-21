#Tabla de multiplicar

Número = int(input("Ingrese su número entero por favor "))

if Número < 0:
    print("Número ingresado inválido")
else:
    for i in range(10):
        print(Número,"x", i + 1 ,"=", (i +1) * Número)
    



    