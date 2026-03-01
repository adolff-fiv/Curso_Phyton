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

    
        
