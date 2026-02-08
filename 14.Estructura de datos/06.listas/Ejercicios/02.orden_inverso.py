""" Números naturales y ordenarlos de manera inversa """

n = int(input("Ingrese cuántos números desee que contenga su lista "))
lista = []

for i in range(n):
    num = int(input("Ingrese un número a la lista "))
    lista.append(num)

lista.sort(reverse=True)
print(lista)



