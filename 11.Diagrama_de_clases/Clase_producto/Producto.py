class Producto:
    contador_productos = 0

    # Constructor de clase
    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    # Propiedades
    def get_precio(self):
        return(self._precio)
    
    # Método string
    def __str__(self):
        return f"\nID: {self._id} \nNombre del producto: {self._nombre} \nPrecio: {self._precio}"
    
if __name__ == "__main__":
    producto1 = Producto("Hollow Night", 20)
    print(producto1)
    producto2 = Producto("pvz", 15)
    print(producto2)


