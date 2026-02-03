import json

def delete_favorito(URL):

    # --- Solicitando el título ---
    titulo_eliminar = input("Ingrese el título del favorito a eliminar ")

    datos = cargar_json(URL)

    if titulo_eliminar in datos:
        del datos[titulo_eliminar]
        print("Favorito eliminado")
    else:
        print("No existe el favorito en el archivo")
    
    escribir_json(URL, datos)

def escribir_json(url,datos):
    archivo = open(url, "w")
    json.dump(datos, archivo)
    archivo.close()

def cargar_json(url):
    archivo = open(url, "r")
    datos = json.load(archivo)
    archivo.close()
    return datos