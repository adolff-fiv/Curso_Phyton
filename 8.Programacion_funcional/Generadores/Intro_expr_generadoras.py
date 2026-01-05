#Introducción a las expresiones generadoras

rango = int(input("Ingrese un número "))

generador = (numero * numero for numero in range(rango))

print(type(generador))
for i in generador:
    print(f'Numero elevado al cuadrado -> {i}')
