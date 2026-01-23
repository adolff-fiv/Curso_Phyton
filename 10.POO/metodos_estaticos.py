class Persona:

    variable_clase = "Esta es una variable de clase"

    def __init__(self, varianble_instancia):
        self._variable_instancia = varianble_instancia
    
    def get_variable_instancia(self):
        return self._variable_instancia
    
    def metodo_normal(self):
        return "Retornando método normal"
    
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    @staticmethod
    def metodo_estatico():
        print(Persona.variable_clase)

Persona.metodo_estatico()
Persona.metodo_clase()