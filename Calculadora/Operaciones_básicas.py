import math

def sumar(x , v):
    return x + v

def restar(x , v):
    return x - v

def multiplicación(x , v):
    return x * v

def División(x , v):

    if v == 0:
        print("Dividir entre cero es imposible")
    else:
        return x / v

def Potencia(x , v):
    return math.pow(x,v)

def Raiz_cuadrada(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        x * -1
        return math.sqrt(x), "i"
    
def Modulo(x , v):
    if v != 0:
        return x % v
    else:
        print("Es imposible dividir entre 0")

def Raiz_cubica(num1):
    return math.pow(num1, 1/3)

        
