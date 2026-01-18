class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        return f"Color del vehículo: {self._color} \nTipo de rueda del vehículo: {self._ruedas}"
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()}\n Velocidad(Km/h): {self._velocidad} '

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo

    def __str__(self):
        return super().__str__() + "\n Tipo:" + self._tipo
    
carreta = Vehiculo("Negro", 4)
print(carreta)

nissan = Coche("Blanco", 4, 150)
print(nissan)

trek = Bicicleta("Rojo", 2, "Montaña")
print(trek)
    
    

    