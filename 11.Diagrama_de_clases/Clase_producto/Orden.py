from Producto import Producto

class Orden:
    contador = 0
    
    # Constructor de clase
    def __init__(self, productos):
        Orden.contador += 1
        self._contador = Orden.contador
        self._productos = list(productos)

    # Método para agregar los productos a la lista
    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_orden(self):
        total = 0
        for producto in self._productos:
            total += producto.get_precio
        return total
    
    def __str__(self):
        producto_str = " "
        for producto in self._productos:
            producto_str += producto.__str__() + "\n"
        return f"Orden: {self._contador} \n Productos: {producto_str}"  

if __name__ == "__main__":
    producto1 = Producto("Rocket League", 1)
    producto2 = Producto("FIFA", 70)
    productos_lista = [producto1, producto2]
    orden1 = Orden(productos_lista)
    orden1.agregar_producto(Producto("Ghost", 80))
    print(orden1)
    print(f"El monto total es: {orden1.calcular_orden()}") 

    
        