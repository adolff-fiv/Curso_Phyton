#Sucesión de Fibonacci

numero = 10
n0 = 0
n1 = 1

print(n0 , end=" ; ")
print(n1 , end=" ; ")


for i in range( numero -2):
    n3 = n0 + n1
    print(n3, end=" ; ")
    n0 = n1 
    n1 = n3
