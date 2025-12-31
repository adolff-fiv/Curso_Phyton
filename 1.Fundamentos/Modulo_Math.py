"""
Ingresamos modulo matemático para las operaciones
"""
import math

numero = int(input("ingresa un número entero por favor "))
print(f"Raíz cuadrada de {numero} = {math.sqrt(numero)}")
print(f"Seno de {numero} = {math.sin(numero)}")
# Exponencial de x es elevar la contante matemática(2.71828) a x, es decir e elevado a x.
print(f"Exponencial de {numero} = {math.exp(numero)}")

print(f"Redondear resultado de {numero} = {round(numero)}")
print(f"logaritmo de {numero} = {math.log(numero)}")
# El logaritmo y la exponencial son operaciones opuestas y al usarlas ambas deberían dar el mismo número.

print(f"El mismo número de {numero} = {math.log(math.exp(numero))}")

"""
Página del Módulo Math: https://docs.python.org/es/3.10/library/math.html
"""