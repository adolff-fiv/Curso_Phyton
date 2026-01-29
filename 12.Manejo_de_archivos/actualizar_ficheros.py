try:
    archivo = open('prueba.txt',"a", encoding="utf 8")
    archivo.write("\nEsta es una prueba de la tercera línea del texto")    
except Exception as e:
    print(e)
finally:
    archivo.close

    