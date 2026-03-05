import re

# Con expresiones regulares, podemos buscar todo tipo de patrones
# por ejemplo, podemos filtrar las palabras con acentos

patron = ('w*[ñáéíóúÑÁÉÍÓÚ]w*')
palabras = re.compile(patron)
print(palabras.findall("Niño, Acciónn, Perro, Lobo, Expresión, Español"))
