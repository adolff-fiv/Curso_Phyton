class Cola:
        # Constructor de clase
    def __init__(self, ):
        self.cola = []
        self.size = 0

    # Si hay elementos en la cola
    def empty(self):
        return len(self.cola) == 0
        
    # Agregar datos a la cola
    def push(self, dato):
            self.cola += [dato]
            self.size += 1

    # Eliminar un elemento de la cola
    def pop(self):
        if self.empty():
            print("La cola está vacía")
        else:
            self.cola = [self.cola[i] for i in range(1, self.size)]
            self.size -= 1

    # Mostrar cola
    def show(self):
        i = self.size - 1
        while i > -1:
            print(f'[{i}] => {self.cola[i]}')
            i -= 1
    
    # Mostrar el primer dato de la cola
    def front(self):
        print("Cola vacía") if self.empty() else print(f'Primer dato: {self.cola[0]}')

try:   
    if __name__ == "__main__":
        opcion = 0
        cola = Cola()
        while opcion != 6:
            print(f"\n-----------COLA------------\n"
                "- 1.Agregar dato   \n"
                "- 2.Eliminar dato   \n"
                "- 3.¿Está vacía la cola?   \n"
                "- 4.Mostrar cola    \n"
                "- 5.Mostrar el primer dato   \n"
                "- 6.Salir del programa   \n"
                "-----------------------------\n")
            opcion = int(input("Ingresa tu opción "))
            
            if opcion == 1:
                dato = input("Ingresa el dato a añadir a la cola ")
                cola.push(dato)
            elif opcion == 2:
                cola.pop()
            elif opcion == 3:
                print("Sí" if cola.empty() else "No")
            elif opcion == 4:
                cola.show()
            elif opcion == 5:
                print(cola.front())
            elif opcion == 6:
                print("Deteniendo programa")
                exit()
            else:
                print("Opción inválida")
except Exception as e:
    print(e)