""" Reemplazar el texto erróneo en un archivo """

# Creando archivo de texto con la conversación
try:
    archivo = open("prueba.txt", "wt",  encoding= "utf 8")
    archivo.write("Hola\nHola, ¿Cómo estas?\nNo muy bien y ¿tú?\nPerro\nOk, hablamos mañana\nAdiós")
except Exception as e:
    print(e)
finally:
    archivo.close()

# Reemplazando la frase erronea
try:
    archivo = open("prueba.txt", "rt",  encoding= "utf 8")
    reemplazo = ""
    for linea in archivo:
        linea.strip()
        cambio = linea.replace("Perro", "Podría estar mejor")
        reemplazo = reemplazo + cambio 
except Exception as ex:
    print(ex)
finally:
    archivo = open("prueba.txt", "wt",  encoding= "utf 8")
    archivo.write(reemplazo)
    archivo.close()