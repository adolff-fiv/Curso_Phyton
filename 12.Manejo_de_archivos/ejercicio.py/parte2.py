# Eliminar el archivo si el text coincide con "abadacadabra"
import os

try:
    archivo = open("prueba2.txt", "wt",  encoding= "utf 8")
    frase = input("Ingrese una frase ")
    archivo.write(frase + "\n")
    if frase == "abadacadabra":
        archivo.close()
        os.remove("prueba2.txt")
    else:
        print("No es la frase adecuada")
except Exception as e:
    print(e)
finally:    
    archivo.close()

