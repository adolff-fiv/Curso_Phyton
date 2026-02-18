class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class Lista_Doblemente_Enlazada    :
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacio(self):
        return self.primero == None
    
    def agregar_final(self, dato):
        if self.vacio():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.size += 1

    def agregar_primero(self, dato):
        if self.vacio():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = None
            self.primero = aux
        self.size += 1
    
    def recorrer_inicio(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente
    
    def recorrer_final(self):
        aux = self.ultimo
        while aux  != None:
            print(aux.dato)
            aux = aux.anterior
    
    def tamaño(self):
        print(self.size)
    
    def eliminar_primero(self):
        if self.vacio():
            print("La lista está vacía") 
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0  
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size -= 1

    def eliminar_final(self):
        if self.vacio():
            print("La lista está vacía") 
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0  
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -= 1

try:   
    if __name__ == "__main__":
        opcion = 0
        lista = Lista_Doblemente_Enlazada()
        while opcion != 9:
            print(f"\n--------LISTA DOBLEMENTE ENLAZADA------------\n"
                "- 1.Agregar al final  \n"
                "- 2.Eliminar al final   \n"
                "- 3.¿Está vacía la lista?   \n"
                "- 4.Mostrar en orden ascendente    \n"
                "- 5.Agregar al inicio   \n"
                "- 6.Eliminar al inicio   \n"
                "- 7.Motrar en orden descendente   \n"
                "- 8.Motrar tamaño de la llista   \n"
                "- 9.Salir   \n"
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
                lista.recorrer_inicio()
            elif opcion == 5:
                dato = input("Ingresa el dato a añadir a la lista ")
                print(lista.agregar_primero(dato))
            elif opcion == 6:
                lista.eliminar_primero()
            elif opcion == 7:
                lista.recorrer_final()
            elif opcion == 8:
                lista.tamaño()
            elif opcion == 9:
                print("Deteniendo programa")
                exit()
            else:
                print("Opción inválida")
except Exception as e:
    print(e)