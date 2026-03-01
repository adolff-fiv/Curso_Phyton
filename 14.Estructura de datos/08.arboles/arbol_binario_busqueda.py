class Nodo:

    # Constructor de clase
    def __init__(self, valor=None, padre=None, es_raiz=False, 
                 es_izquierda=False, es_derecha=False):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.padre = padre
        self.es_raiz = es_raiz
        self.es_izquierda = es_izquierda
        self.es_derecha = es_derecha

class ArbolBinarioBusqueda:
    # Constructor de clase 
    def __init__(self):
        self.raiz = None
    # Saber si está vacío
    def vacio(self):
        return self.raiz == None

    # Obtener lugar
    def obtener_lugar(self, valor):
        aux = self.raiz
        while aux != None:
            temp = aux
            if valor <= aux.valor:
                aux = aux.izquierda
            else:
                aux = aux.derecha
        return temp 

    # Agregar Dato
    def agregar_dato(self,valor):
        if self.vacio():
            self.raiz = Nodo(valor=valor, es_raiz=True)
        else:
            nodo = self.obtener_lugar(valor)
            if valor <= nodo.valor:
                nodo.izquierda = Nodo(valor=valor, padre=nodo, es_izquierda=True)
            else:
                nodo.derecha = Nodo(valor=valor, padre=nodo, es_derecha=True)
    
    # Realizar recorrido en orden
    def reccorido_in_order(self, node):
        if node:
            self.reccorido_in_order(node.izquierda)
            print(node.valor)
            self.reccorido_in_order(node.derecha)

    # Realizar recorrido en pre-orden
    def reccorido_pre_order(self, node):
        if node:
            print(node.valor)
            self.reccorido_pre_order(node.izquierda)
            self.reccorido_pre_order(node.derecha)

    # Realizar recorrido en pos-orden
    def reccorido_pos_order(self, node):
        if node:
            self.reccorido_pos_order(node.izquierda)
            self.reccorido_pos_order(node.derecha)
            print(node.valor)           

    # Buscar un dato
    def buscar(self, nodo, valor):
        if nodo == None:
            return None
        else:
            if nodo.valor == valor:
                print(nodo)
            elif valor <= nodo.valor:
                return self.buscar(nodo.izquierda, valor)
            else:
                return self.buscar(nodo.derecha, valor)

if __name__ == "__main__":
    def menu():
        opc = 0
        arbol = ArbolBinarioBusqueda()
        try:
            while opc != 7:
                print("Arbol binario de Búsqueda\n" 
                    +"\n\t1.Agregar dato" 
                    +"\n\t2.¿Está vacío el arbol?"
                    +"\n\t3.Recorrer en orden"
                    +"\n\t4.Recorrer en pre-orden"
                    +"\n\t5.Recorrer en post-orden"
                    +"\n\t6.Buscar un dato"
                    +"\n\t7.Salir")
                opc = int(input("Ingrese una opción "))
            
                if opc == 1:
                    dato = int(input("Ingrese el dato a añadir al arbol "))
                    arbol.agregar_dato(dato)
                elif opc == 2:
                    print("Si" if arbol.vacio() else print("No"))
                elif opc == 3:
                    arbol.reccorido_in_order(arbol.raiz)
                elif opc == 4:
                    arbol.reccorido_pre_order(arbol.raiz)
                elif opc == 5:
                    arbol.reccorido_pos_order(arbol.raiz)
                elif opc == 6:
                    dato = int(input("Ingrese el dato a buscar al arbol "))
                    print(arbol.buscar(arbol.raiz, dato))
                elif opc == 7:
                    print("Deteniendo programa")
                    exit()
                else:
                    print("La opción digitada no es válida")
        except Exception as e:
            print("Ha ocurrido un error inesperado, solo son válidos las caracteres numéricos")
            print(e)

menu()
    
        
