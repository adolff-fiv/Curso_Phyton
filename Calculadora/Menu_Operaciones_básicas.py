
from Operaciones_básicas import *

def op():
    rpta = int(input("Ingrese una operación "))
    if rpta == 1: 
        a = int(input("Ingrese un número "))
        b = int(input("Ingrese otro número "))
        print(f''' {a} + {b} = {sumar(a,b)} ''') 
    elif rpta == 2:
        a = int(input("Ingrese un número "))
        b = int(input("Ingrese otro número "))
        print(f''' {a} - {b} = {restar(a,b)} ''')
    elif rpta == 3:
        a = int(input("Ingrese un número "))
        b = int(input("Ingrese otro número "))
        print(f''' {a} x {b} = {multiplicación(a,b)} ''')
    elif rpta == 4:
        a = int(input("Ingrese un número "))
        b = int(input("Ingrese otro número "))
        print(f''' {a} / {b} = {División(a,b)} ''')
    elif rpta == 5:
        a = int(input("Ingrese un número "))
        b = int(input("Ingrese otro número "))
        print(f''' {a} * {b} = {Potencia(a,b)} ''')
    elif rpta == 6:
        a = int(input("Ingrese un número "))
        b = int(input("Ingrese otro número "))
        print(f''' {a} % {b} = {Modulo(a,b)} ''')
    elif rpta == 7:
        a = int(input("Ingrese un número "))
        print(f''' raíz cuadrada de {a} = {Raiz_cuadrada(a)} ''')
    elif rpta == 8: 
        a = int(input("Ingrese un número "))
        print(f''' raíz cúbica de {a} = {Raiz_cubica(a)} ''')