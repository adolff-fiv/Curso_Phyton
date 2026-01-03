import time

def generador(funcion):
    def dividir(*arg, **kwargs):
        tiempo1 = time.time()
        print("Efectuando la división")
        resultado = funcion(*arg, **kwargs)
        tiempo2 = time.time()
        print("La funcion tardó {0} segundos en efectuarse".format(tiempo2 - tiempo1) )
        return resultado
    return dividir 

@generador
def division(a, b):
    return a / b

print(division(5, 2))