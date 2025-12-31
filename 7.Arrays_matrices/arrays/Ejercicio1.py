n = int(input("Ingrese cuantos nombres desea colocar "))

array1 = []
array2 = []

for i in range(n):
     array1.append(str(input("Ingresa un nombre ")))

print(array1)

for i in range(n):
     array2.append(len(array1[i]))

print(array2)
     