print("Antes del error")
def x(a, b):
    yield a + b
    yield a - b
xd = x(7, 4)
try:
    print(7/ 0)
    print(next(xd))
    print(next(xd))
    print(next(xd))
except:
    print("Ha ocurrido un error")
finally:
    print("Imprimiendo algo")

print("Después del error")

