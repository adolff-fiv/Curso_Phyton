class Node:
    # Constructor de clase
    def __init__(self, label):
        self.label = label
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0
    
class AVL:
    # Constructor de clase
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):        
        node = Node(value)

        if self.root is None:
            self.root = node
            self.root.height = 0
            self.size = 1
        
        else:
            dad_node = None
            curr_node = self.root

            while True:
                if curr_node is not None:
                    dad_node = curr_node

                    if node.label  < curr_node.label:
                        curr_node = curr_node.left
                    else:
                        curr_node = curr_node.right
                
                else:
                    node.height = dad_node.height
                    dad_node.height += 1
                    if node.label < dad_node.label:
                        dad_node.left = node
                    else:
                        dad_node.right = node   
                    self.rebalance(node)
                    self.size += 1
                    break

    # Operación de rotación
    def rebalance(self, node):
        n = node

        while n is not None:
            height_right = n.height
            height_left = n.height

            if n.right is not None:
                height_right = n.right.height      

            
            if n.left is not None:      
                height_left = n.left.height    

            if abs(height_left - height_right) > 1:
                if height_left > height_right:
                    left_child = n.left
                    if left_child is not None:
                        h_right = (left_child.right.height if (left_child.right is not None) else 0)
                    
                        h_left = (left_child.left.height if (left_child.left is not None) else 0)
                    if (h_left > h_right):
                        self.rotate_left(n)
                        break
                    else:
                        self.double_rotate_right(n)
                        break
                    
                else:
                    right_child = n.right 

                    if right_child is not None:
                            h_right = (right_child.right.height if (right_child.right is not None) else 0)
                        
                            h_left = (right_child.left.height if (right_child.left is not None) else 0)
                    if (h_left > h_right):
                            self.double_rotate_left(n)          
                            break
                    else:
                            self.rotate_right(n)
                            break
            n = n.parent
    
    def rotate_left(self, node):
        aux = node.parent.label
        node.parent.label = node.label
        node.parent.right = Node(aux)
        node.parent.right.height = node.parent.height + 1
        node.parent.left = node.right

    def rotate_right(self, node):
        aux = node.parent.label
        node.parent.label = node.label
        node.parent.left = Node(aux)
        node.parent.left.height = node.parent.height + 1
        node.parent.right = node.right

    def double_rotate_left(self,node):
        self.rotate_right(node.getRight().getRight())
        self.rotate_left(node)      
 
    def double_rotate_right(self,node):
        self.rotate_left(node.getLeft().getLeft())
        self.rotate_right(node)

    # Saber si está vacío
    def empty(self):
        return self.root == None
    
    # Realizar recorrido en orden
    def reccorido_in_order(self, node):
        if node:
            self.reccorido_in_order(node.left)
            print(node.label, end=" ")
            self.reccorido_in_order(node.right)

    # Realizar recorrido en pre-orden
    def reccorido_pre_order(self, node):
        if node:
            print(node.label, end=" ")
            self.reccorido_in_order(node.left)
            self.reccorido_in_order(node.right)

    # Realizar recorrido en pos-orden
    def reccorido_pos_order(self, node):
        if node:
            self.reccorido_in_order(node.left)
            self.reccorido_in_order(node.right)
            print(node.label, end=" ")   

    def get_root(self):
        return self.root
    
if __name__ == "__main__":
    def menu():
        opc = 0
        arbol_avl = AVL()
        try:
            while opc != 7:
                print("\nArbol AVL\n" 
                    +"\n\t1.Agregar dato" 
                    +"\n\t2.¿Está vacío el arbol?"
                    +"\n\t3.Recorrer en orden"
                    +"\n\t4.Recorrer en pre-orden"
                    +"\n\t5.Recorrer en post-orden"
                    +"\n\t6.Buscar la raiz del arbol"
                    +"\n\t7.Salir")
                opc = int(input("Ingrese una opción "))
            
                if opc == 1:
                    dato = int(input("Ingrese el dato a añadir al arbol "))
                    arbol_avl.insert(dato)
                elif opc == 2:
                    print("Si" if arbol_avl.empty() else print("No"))
                elif opc == 3:
                    arbol_avl.reccorido_in_order(arbol_avl.root)
                elif opc == 4:
                    arbol_avl.reccorido_pre_order(arbol_avl.root)
                elif opc == 5:
                    arbol_avl.reccorido_pos_order(arbol_avl.root)
                elif opc == 6:
                    print(arbol_avl.get_root().label)
                elif opc == 7:
                    print("Deteniendo programa")
                    exit()
                else:
                    print("La opción digitada no es válida")
        except Exception as e:
            print("Ha ocurrido un error inesperado, solo son válidos las caracteres numéricos")
            print(e)

menu()
    
    

    




        