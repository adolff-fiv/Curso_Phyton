# Almacenar artículos y su precio, mostrar solo los artículos que superen 100 S/

def menu():
    opc = 0
    diccionario = {}
    try:
        while opc != 4:
            print("LISTA DE ARTÍCULOS\n" 
                  +"\n\t1.Agregar artículo" 
                  +"\n\t2.Mostar listado de artículos"
                  +"\n\t3.Mostrar artículos mayores a 100 S/"
                  +"\n\t4.Salir")
            opc = int(input("Ingrese una opción "))
        
            if opc == 1:
                ingresar_artículo(diccionario)
            elif opc == 2:
                print(diccionario)
            elif opc == 3:
                precios_mayores_100(diccionario)
            elif opc == 4:
                print("Deteniendo programa")
                exit()
            else:
                print("La opción digitada no es válida")
    except Exception as e:
        print("Ha ocurrido un error inesperado, solo son válidos las caracteres numéricos")
        print(e)
        

def ingresar_artículo(diccionario):
    nombre = input("Ingrese el nombre del artículo ")
    precio = float(input("Ingrese el precio del artículo "))
    diccionario[nombre] = precio

def precios_mayores_100(diccionario):
    for i in diccionario:
        if diccionario[i] > 100:
            print(diccionario[i])

if __name__ == "__main__":
    menu() 

