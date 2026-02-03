import json

def view_favoritos(URL):

    datos = cargar_json(URL)

    print("\n--- Lista de favoritos ---")
    for favoritos in datos:
        print(f'{favoritos} = {datos[favoritos]}')

def cargar_json(url):
    archivo = open(url, "r")
    datos = json.load(archivo)
    archivo.close()
    return datos