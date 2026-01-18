class Padre:

    # Constructor de clase
    def __init__(self, nombre, apellido, carro):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carro = carro
    
    def jugar_futbol(self):
        return "Jugando fútbol"
    
    def cocinar(self):
        return "Cocinando"

    def __str__(self):
        return f'Datos básicos Padre: \nNombre: {self.__nombre} \nApellido: {self.__apellido} \nCarro: {self.__carro}'
    
class Hijo(Padre):

    # Constructor de clase
    def __init__(self, nombre, apellido, carro, moto):
        super().__init__(nombre, apellido, carro)
        self.__moto = moto

    def correr(self):
        return "Corriendo"
    
padre = Padre("Ricardo", "Paredes", "Si")
print(padre.__str__())
print(padre.jugar_futbol())
print(padre.cocinar())
print(f'\n ---------------------------- \n')

hijo = Hijo("Adolfo", "Paredes", "Si", "Si")
print(hijo.jugar_futbol())
print(hijo.cocinar())
print(hijo.correr())
