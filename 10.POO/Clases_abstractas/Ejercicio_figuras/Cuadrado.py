from Ejercicio_figuras.fig_geo import Figuras

class Cuadrado(Figuras):

    # Constructor de clase
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)

    # Implementación del  método abstacto de figuras
    def calcular_area(self):
        return self._alto * self._ancho
    
    # Método string
    def __str__(self):
        return f'{Figuras.__str__(self)}'