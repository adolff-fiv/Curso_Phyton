# Conseguir los pares e impares de un rango

pares , impares = [], []

for num in range(1, 10):
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    
print(f'Pares: {pares} \n Impares: {impares}')

# Método con list comprenension

pares , impares = [], []
[pares.append(num) if num % 2 == 0 else impares.append(num) for num in range(1, 10)]
print(f'Pares: {pares} \n Impares: {impares}')
