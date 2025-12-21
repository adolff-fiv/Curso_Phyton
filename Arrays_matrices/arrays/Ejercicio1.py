n = int(input("Ingrese cuantos nombres desea colocar "))

array1 = []
array2 = []

for i in range(n):
     nombre = str(input("Ingresa un nombre "))
     array1.append(nombre)

print(array1)

for i in range(n):
     array2.append(i)

print(array2)
     