try:
    archivo = open("prueba.txt", "w", encoding= "utf 8")
    archivo.write("Agregamos una línea de texto desde python \n")
    archivo.write("Hola")
except Exception as e:
    print(e)
finally:
    archivo.close()
