class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircularSimplementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacio(self):
        return self.primero == None
    
    def agregar_inicio(self, dato):
        if self.vacio():
            self.primero = self.ultimo = Nodo(dato  )
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero

    def agregar_final(self, dato):
        if self.vacio():
            self.primero = self.ultimo = Nodo(dato)
            self.primero.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero
    
    def recorrido(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break
    
    def eliminar_inicio(self):
        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero

    def eliminar_final(self):
        if self.vacio():
            print("La lista está vacía")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            aux = self.primero
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente
            aux.siguiente = self.primero
            self.ultimo = aux

try:   
    if __name__ == "__main__":
        opcion = 0
        lista = ListaCircularSimplementeEnlazada()
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
                lista.agregar_final(dato)
            elif opcion == 2:
                lista.eliminar_final()
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