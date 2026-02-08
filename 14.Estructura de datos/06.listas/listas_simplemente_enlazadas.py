class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista_Simplemente_Enlazada    :
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacio(self):
        return self.primero == None
    
    def agregar_ultimo(self, dato):
        if self.vacio():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
    
    def recorrido(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente

    def eliminar_ultimo(self):
        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux = aux.siguiente
        aux.siguiente = None
        self.ultimo = aux

    def agregar_inicio(self, dato):
        if self.vacio():
            self.primero = self.ultimo = Nodo(dato  )
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux

    def eliminar_inicio(self):
        self.primero = self.primero.siguiente

try:   
    if __name__ == "__main__":
        opcion = 0
        lista = Lista_Simplemente_Enlazada()
        while opcion != 7:
            print(f"\n--------LISTA SIMPLEMENTE ENLAZADA------------\n"
                "- 1.Agregar último   \n"
                "- 2.Eliminar último   \n"
                "- 3.¿Está vacía la lista?   \n"
                "- 4.Mostrar lista    \n"
                "- 5.Agregar al inicio   \n"
                "- 6.Eliminar al inicio   \n"
                "- 7.Salir   \n"
                "-----------------------------\n")
            opcion = int(input("Ingresa tu opción "))
            
            if opcion == 1:
                dato = input("Ingresa el dato a añadir a la lista ")
                lista.agregar_ultimo(dato)
            elif opcion == 2:
                lista.eliminar_ultimo()
            elif opcion == 3:
                print("Sí" if lista.vacio() else "No")
            elif opcion == 4:
                lista.recorrido()
            elif opcion == 5:
                dato = input("Ingresa el dato a añadir a la lista ")
                print(lista.agregar_inicio(dato))
            elif opcion == 6:
                lista.eliminar_inicio()
            elif opcion == 7:
                print("Deteniendo programa")
                exit()
            else:
                print("Opción inválida")
except Exception as e:
    print(e)