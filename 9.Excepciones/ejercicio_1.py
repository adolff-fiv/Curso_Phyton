# Localizar el error en un código

try:
    colores = {'red':'rojo', 'green':'verde', 'negro':'black',}
    colores['blanco']
except KeyError as key:
    print("Ha ocurrido un error del tipo Keyerror, Blanco no se encuentra dentro del diccionario a utilizar.")
    print("La solución es crear la llave o acceder a una llave válida.")