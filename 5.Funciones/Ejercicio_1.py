#Calculadora Básica
import time

def sumar(a , b):
    Resultado =  a + b
    return Resultado

def restar(a , b):
    Resultado =  a - b
    return Resultado

def multiplicación(a , b):
    Resultado =  a * b
    return Resultado

def División(a , b):

    if b == 0:
        print("Dividir entre cero es imposible")
    else:
        Resultado =  a / b
        return Resultado

def calculadora():
    opción = 0
    while opción != 5:
        print(f'''Calculadora
                1.Sumar
                2.Restar
                3.Multiplicar
                4.Dividir
                5.Cerrar el programa        
    ''')
        opción = int(input())

        if opción == 5:
            break
        
        a = float(input("Ingrese el primer número "))
        b = float(input("Ingrese el segundo número "))
       

        if opción == 1:
            print(sumar(a, b))
            time.sleep(2)
        elif opción == 2:
            print(restar(a, b))
            time.sleep(2)
        elif opción == 3:
            print(multiplicación(a, b))
            time.sleep(2)
        elif opción == 4:
            print(División(a, b))
            time.sleep(2)
        else:
            print("Error en la sintaxis")    

calculadora()