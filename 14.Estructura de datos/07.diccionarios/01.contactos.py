"""Diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono"""

diccionario = {}
opcion = 1

try:
    while opcion == 1:
        nombre = input("Ingrese el nombre del contacto ")
        numero = int(input("Ingrese el número del contacto "))
        diccionario[nombre] = numero
        opcion = int(input("Ingrese 1 para seguir añadiendo contactos o cualquier otro " \
        "número para salir "))
    print(diccionario)
except Exception as e:
    print("\nOcurrió un error inesperado")
    print(e)


