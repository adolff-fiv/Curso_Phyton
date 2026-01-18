from Animales.Animal import Animal

class Conejo(Animal):
    # Constructor heredado
    def __init__(self, peso, altura, alimentos, diente):
        super().__init__(peso, altura, alimentos)
        self.__diente = diente
    # Método get
    def get_diente(self):
        return self.__diente