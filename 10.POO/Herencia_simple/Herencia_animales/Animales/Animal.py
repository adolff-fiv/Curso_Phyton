class Animal:
    # Método constructor
    def __init__(self, peso, altura, alimentos):
        self._peso = peso
        self._altura = altura
        self._alimentos = alimentos

    #Métodos Get 
    def get_peso(self):
        return self._peso
    
    def get_altura(self):
        return self._altura

    def get_alimentos(self):
        return self._alimentos
    
    # Funcion calculadora del IMC
    def get_IMC(self):
        return self._peso / (self._altura * self._altura)