import math

class Persona:
    def __init__(self, nombre, apellido, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.altura = altura
        self.peso = peso
    
    def calcular_imc(self):
        return self.peso / math.pow(self.altura, 2)
    
class Trabajador(Persona):
    def __init__(self, nombre, apellido, altura, peso):
        Persona.nombre = nombre
        Persona.apellido = apellido 
        Persona.altura = altura 
        Persona.peso = peso 
    def trabajar():
        return "Trabajando"
    
class Insituto:
    def __init__(self, nombre_ins):
        self.nombre_ins = nombre_ins    

    def estudiando(self):
        return f"Estudiando en {self.nombre_ins}"
    
class Estudiante(Trabajador, Insituto):
    def __init__(self, nombre, apellido, altura, peso, nombre_ins):
        Trabajador.nombre = nombre
        Trabajador.apellido = apellido
        Trabajador.altura = altura
        Trabajador.peso = peso
        Insituto.nombre_ins = nombre_ins

    def estudiar(self):
        return "Me gusta estudiar"
    
estudiante = Estudiante("Adolfo", "Paredes", 1.78, 57, "Cato")
print(estudiante.calcular_imc())
print(estudiante.estudiando())
print(estudiante.estudiar())