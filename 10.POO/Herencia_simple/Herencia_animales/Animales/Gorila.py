from Animales.Animal import Animal

class Gorila(Animal):
    # Constructor heredado
    def __init__(self, peso, altura, alimentos):
        super().__init__(peso, altura, alimentos)

    def comer(self):
        lista = []
        for i in self._alimentos:
            lista.append(f'Comiendo: {i}')
        return lista