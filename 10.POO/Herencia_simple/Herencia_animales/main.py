
from Animales.Conejo import Conejo
from Animales.Gorila import Gorila

conejo = Conejo(3, 0.3, ["Pastizal", "Agua"], "Molar")
print(conejo.get_peso())
print(conejo.get_altura())
print(conejo.get_alimentos())
print(conejo.get_diente())
print(conejo.get_IMC())

gorila = Gorila(90, 1.3, ["Banana", "Peras"])
print(gorila.get_peso())
print(gorila.get_altura())
print(gorila.get_alimentos())
print(gorila.comer())
print(gorila.get_IMC())




    
    



    

    
