# Nodo de árbol rojo_negro
class RBN(object):
    def __init__(self, data):
        self.data = data # Campo de datos
        self.color = 0
        self.left = None
        self.right = None
        self.parent = None

# Árbol rojo negro
class RBT(object):
    def __init__(self):
        self.root = None
    
    # Recorrido de orden medio
    def midTraverse(self, x):
        if x == None:
            return
        self.midTraverse(x.left)
        colorStr = "negro" if x.color == 1 else "rojo"
        parentStr = "Padre =" + ("No tiene" if  x.parent == None else str(x.parent.data))
        print(x.data, colorStr, parentStr)
        self.midTraverse(x.right)

    # Agregar un nodo
    def add(self, x):
        # Si no hhay un nodo raíz como raíz
        if self.root == None:
            self.root = x
            x.color = 1 # El nodo raíz es negro
            return
            
        # Encontrar una posicón de inserción adecuada
        p = self.root
        while p != None:
            if x.data < p.data:
                if p.left == None:
                    p.left = x
                    x.parent = p
                    self.addFix(x)
                    break
                p = p.left
            else:
                if p.right == None:
                    p.right = x
                    x.parent = p
                    self.addFix(x)
                    break
                p = p.right
    
    # Ajustar el arbol rojo-negro
    def addFix(self, x):
        while True:
            if x == self.root: # Si se procesa el nodo raíz, el color es negro
                x.color = 1
                return
            p = x.parent #padre
            if p.color == 1 or x.color == 1: #Mientras el hijo o el padre sea ngero, no puede ser doblemente rojo
                return
            # Analizar al padre rojo
            g = p.parent # El abuelo del padre rojo debe tener un padre, porque la raíz no puede ser roja
            # El tío puede ser un nodo vacío
            u = g.left if p == g.right else g.right
            if u != None and u.color == 0:
                u.color = p.color = 1 #El tío y el padre se ponen negros
                g.color = 0 # El abuelo se vuelve rojo
                x = g # x apunta al abuelo y continúa el ciclo
                continue
            if p == g.left and x == p.left: # izquierda izquierda
                self.rotateRight(p)
            elif p == g.left and x == p.right: # izquierda derecha
                self.rotateLeft(x)
                self.rotateRight(x)
            elif p == g.right and x == p.right: # derecha derecha
                self.rotateLeft(p)
            elif p == g.right and x == p.left: # derecha izquierda
                self.rotateRight(x)
                self.rotateLeft(x)

    def rotateLeft(self, p):
        g = p.parent 
        if g == self.root:
            self.root = p
            p.parent = None
        else:
            gp = g.parent
            p.parent = gp
            if g == gp.left:
                gp.left = p
            else:
                gp.right = p
        g.right = p.left
        if p.left != None:
            p.left.parent = g
        p.left = g
        g.parent = p
        # g y p intercambio de color
        p.color, g.color = g.color, p.color

    def rotateRight(self, p):
        g = p.parent 
        if g == self.root:
            self.root = p
            p.parent = None
        else:
            gp = g.parent
            p.parent = gp
            if g == gp.left:
                gp.left = p
            else:
                gp.right = p
        g.left = p.right
        if p.right != None:
            p.right.parent = g
        p.right = g
        g.parent = p
        # g y p intercambio de color
        p.color, g.color = g.color, p.color

if __name__ == "__main__":
    rbt = RBT()

    datas = [10, 20, 30, 15, 12, 11, 55]

    for dato in datas:
        rbt.add(RBN(dato))

    rbt.midTraverse(rbt.root)
    




    

 