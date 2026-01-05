rango = int(input("Ingrese un número "))
suma = sum(numero * numero for numero in range(rango))
print(f'La suma total de los numeros al cuadrado es {suma}')