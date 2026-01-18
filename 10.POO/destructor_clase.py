class Celular: # Molde principal
    #Atributos
    def __init__(self):
        self.__pantalla = ""
        self.__forma = ""
        self.__ram = 0
        self.__almacenamiento = 0
        self.__camara = 0
        self.__password = "12345"

    def get_pantalla(self):
        return self.__pantalla
    
    def set_pantalla(self, pantalla):
        self.__pantalla = pantalla
        
    def get_forma(self):
        return self.__forma

    def set_forma(self, forma):
        self.__forma = forma
    
    def get_ram(self):
        return self.__ram
    
    def set_ram(self, ram):
        self.__ram = ram
    
    def get_almacenamiento(self):
        return self.__almacenamiento

    def set_almacenamiento(self, almacenamiento):
        self.__almacenamiento = almacenamiento
    
    def get_camara(self):
        return self.__camara
    
    def set_camara(self, camara):
        self.__camara = camara

    def __del__(self):
        print(f'Celular: {self.__almacenamiento} {self.__camara}')

print("Creando un objeto de tipo Celular")
Celu = Celular()
Celu.set_pantalla("IPC"), Celu.set_forma("Curva"), Celu.set_ram(8)
Celu.set_almacenamiento(256), Celu.set_camara(64)
print(Celu) #Celular nuevo que apunta a una dirección de memoria
del Celu # Eliminando celular en la dirección: 0x0000029808C26A50
Celular2 = Celular()
Celular2.set_pantalla("OLED"), Celular2.set_forma("Rectangular"), Celular2.set_ram(16)
Celular2.set_almacenamiento(128), Celular2.set_camara(32)
print(Celular2)  #Creando celular2 en la dirección: 0x0000029808C26A50