class Madre:
    # Constructor de clase
    def __init__(self, nombre, apellido, lote):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__lote = lote

    def get_lote(self):
        return "Lote:", self.__lote

    def jugar_voley(self):
        return "Jugando voley"
    
    def limpiar(self):
        return "Limpiando"

    def __str__(self):
        return f'Datos básicos Madre: \nNombre: {self.__nombre} \nApellido: {self.__apellido} \nLote: {self.__lote}'

class Padre:

    # Constructor de clase
    def __init__(self, nombre, apellido, carro):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carro = carro

    def get_carro(self):
        return "Carro:", self.__carro
    
    def jugar_futbol(self):
        return "Jugando fútbol"
    
    def cocinar(self):
        return "Cocinando"

    def __str__(self):
        return f'Datos básicos Padre: \nNombre: {self.__nombre} \nApellido: {self.__apellido} \nCarro: {self.__carro}'
    
class Hijo(Padre, Madre):

    # Constructor de clase
    def __init__(self, nombre, apellido, carro, lote):
        Madre.__init__(self, nombre, apellido, lote)
        Padre.__init__(self, nombre, apellido, carro)

    def correr(self):
        return "Corriendo"
    
class Nieto(Hijo):
    # Constructor de clase
    def __init__(self, nombre, apellido, carro, lote):
        super().__init__(nombre, apellido, carro, lote)

    def nadar(self):
        return "Nadando"

madre = Madre("María", "Chicata", "Si")
print(madre.__str__()), print(madre.jugar_voley()), print(madre.limpiar())
print(f'\n ---------------------------- \n')

padre = Padre("Ricardo", "Paredes", "Si")
print(padre.__str__()), print(padre.jugar_futbol()), print(padre.cocinar())
print(f'\n ---------------------------- \n')

hijo = Hijo("Adolfo", "Paredes", "Si", "Si")
print(hijo.jugar_futbol()), print(hijo.cocinar()),print(hijo.correr())
print(hijo.jugar_voley()), print(hijo.limpiar()), print(hijo.get_carro())
print(hijo.get_lote())
print(f'\n ---------------------------- \n')

nieto = Nieto("Rafael", "Paredes", "Si", "Si")
print(nieto.jugar_futbol()), print(nieto.cocinar()),print(nieto.correr())
print(nieto.jugar_voley()), print(nieto.limpiar()), print(nieto.get_carro())
print(nieto.get_lote()), print(nieto.nadar())

