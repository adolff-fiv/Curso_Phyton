class Celular: # Molde principal
    #Atributos
    pantalla = ""
    forma = "" 
    ram = 0
    almacenamiento = 0
    camara = 0

    def __init__(self, pant, form, rm, alm, cm):
        self.pantalla = pant
        self.forma = form
        self.ram = rm
        self.almacenamiento = alm
        self.camara = cm

samsung = Celular("Oled", "Rectangular", 16, 64, 48)
print(type(samsung))
print(samsung.pantalla)
print(samsung.forma)
print(samsung.ram)
print(samsung.almacenamiento)
print(samsung.camara)