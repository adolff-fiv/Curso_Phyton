from Ejercicio_figuras.Cuadrado import Cuadrado 
from Ejercicio_figuras.Triangulo import Triangulo 

cuadrado = Cuadrado(5, 5) 
cuadrado.set_alto(7) 
cuadrado.set_ancho(7) 
print("Creando un cuadrado".center(50,"-")) 
print(f"El area del cuadrado es: {cuadrado.calcular_area()} ") 
print(cuadrado) 

print("--------------------------------------------------")
triangulo = Triangulo(5, 5)
triangulo.set_alto(7)
triangulo.set_ancho(7)
print("Creando un cuadrado".center(50,"-"))
print(f"El area del cuadrado es: {triangulo.calcular_area()} ")
print(triangulo)

