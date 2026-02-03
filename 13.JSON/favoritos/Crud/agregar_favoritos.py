import json

# --- Estableciendo variables ---
def add_favoritos(URL):
    lista = []
    diccionario = {}

    # --- Pidiéndole los datos al usuario ---
    titulo, url, comentario = input("Ingrese el título "), input("Ingrese la URL "), input("Ingrese un comentario ")

    # --- Agregando la URL y el comentario a la lista ---
    lista.append(url)
    lista.append(comentario)

    # --- Agregando el favorito al diccionario ---
    diccionario[titulo] = lista

    escribir_json(URL, diccionario)

def escribir_json(url,datos):
    archivo = open(url, "w")
    json.dump(datos, archivo)
    archivo.close()     


