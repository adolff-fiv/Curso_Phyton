from abc import ABC, abstractmethod

# Clase abstracta modelo para todas las figuras geométricas
class Figuras(ABC):
    def __init__(self, ancho, alto):
        if self._validar_positivo(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print("Error, el ancho no puede ser menor a uno")
        if self._validar_positivo(alto):
            self._alto = alto
        else:
            self._alto = 0
            print("Error, el alto no puede ser menor a uno")
            
    # --- Métodos get and set ---
    def get_ancho(self):
        return self._ancho
    
    def get_alto(self):
        return self._alto

    def set_ancho(self, ancho):
        self._ancho = ancho

    def set_alto(self, alto):
        self._alto = alto

    # --- Fin métodos get and set ---

    # Método para validar elementos positivos    
    def _validar_positivo(valor, value):
        return True if valor and value > 0 else False

    
    @abstractmethod
    def calcular_area(self):
        pass
    
    # Método string
    def __str__(self):
        return f'Figura geométrica \n[Ancho: {self._ancho}] \n[Alto: {self._alto}]'
