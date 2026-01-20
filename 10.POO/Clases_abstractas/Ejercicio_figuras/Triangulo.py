from Ejercicio_figuras.fig_geo import Figuras

class Triangulo(Figuras):

    # Constructor de clase
    def __init__(self, ancho, alto):
        Figuras.__init__(self,ancho, alto)

    # Implementación del  método abstacto de figuras
    def calcular_area(self):
        return (self._alto * self._ancho) / 2 
    
    # Método string
    def __str__(self):
        return f'{Figuras.__str__(self)}'