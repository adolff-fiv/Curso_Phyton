#Generador de números parea

cant = int(input("Ingrese cuantos números desea generar "))

def generador(cant):
    for i in range( 1, cant + 1):
        yield i

for valor in generador(cant):
    if valor % 2 == 0:
        print(valor)
        
        