# Lista de numeros divisibles entre 2 y 6

print("Ingrese el rango de los números, mínimo y máximo")
a, b = int(input()), int(input())
lista = []
lista = [num for num in range(a, b + 1) if num % 2 == 0 and num % 6 == 0]
print(f'La lista de números divisibles entre 2 y 6: {lista}')