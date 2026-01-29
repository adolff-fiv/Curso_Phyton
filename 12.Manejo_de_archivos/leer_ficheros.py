try:
    archivo = open("prueba.txt", "rt", encoding="utf 8")

    # --- Imprimiendo todo el archivo
    print(archivo.read())

    # --- Imprimiendo solo algunos caracteres
    print(archivo.read(7))

    # --- Imprimiendo de línea en línea
    print(archivo.readline())

    # --- Imprimiendo todas las líneas una por una
    for linea in archivo:
        print(linea, end="")
except Exception as e:
    print(e)
finally:
    archivo.close()