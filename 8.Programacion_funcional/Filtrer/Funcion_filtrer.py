# filter(funcion o filtro, iterable a filtrar)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
def funcion(x):
    if x % 2 == 0:
        return True
    else:
        return False
"""

resultado = filter(lambda x: x % 2 == 0, num)
print(list(resultado))