"""
def mi_decorador(funcion):
    def nueva_funcion (a,b):
        print("Se va a llamar")
        c = funcion(a,b)
        print("Se ha llamado")
        return c
    return nueva_funcion

@mi_decorador
def suma(a,b):
    print("Entra en función suma")
    return a + b

@mi_decorador
def resta(a,b):
    print("Entra en función resta")
    return a - b

print(suma(1,2))
print(resta(5,3))
"""
def mi_decorador(arg):
    def decorador_real(funcion):
        def nueva_funcion(a, b):
            print(arg)
            c = funcion(a, b)
            print(arg)
            return c
        return nueva_funcion
    return decorador_real

@mi_decorador("Imprime esto antes y después")
def suma(a, b):
    print("Entra en función suma")
    return a + b

print(suma(7, 4))
