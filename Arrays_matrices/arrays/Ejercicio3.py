#Múltiplo de un número

cant = int(input("Ingrese cuantos múltiplos desea "))
array = []
num = int(input("Ingrese el numero del cual desea su multiplo "))

for i in range(cant):
    array.append((i + 1) * num)

print(array)