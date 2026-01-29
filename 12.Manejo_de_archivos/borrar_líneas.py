archivo = open("prueba.txt", "r")
lineas = archivo.readlines()
archivo.close()

del lineas[3 - 1]

archivo = open("prueba.txt", "w")
archivo.writelines(lineas)
archivo.close()

