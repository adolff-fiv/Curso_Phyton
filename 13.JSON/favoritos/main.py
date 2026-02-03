from Crud.agregar_favoritos import add_favoritos
from Crud.actualizar_favoritos import update_favorito
from Crud.eliminar_favoritos import delete_favorito
from Crud.mostrar_favoritos import view_favoritos
opcion = 0
URL = "13.JSON/favoritos/favoritos.json"

if __name__ == "__main__":
    while opcion != 5:
        print(f" \n--------------------\n"
            "- 1.Agregar favoritos   \n"
            "- 2.Actualizar favoritos   \n"
            "- 3.Eliminar favortios   \n"
            "- 4.Consultar favoritos    \n"
            "- 5.Salir del programa   \n"
            "-----------------------\n")
        opcion = int(input("Ingresa tu opción "))
        
        if opcion == 1:
            add_favoritos(URL)
        elif opcion == 2:
            update_favorito(URL)
        elif opcion == 3:
            delete_favorito(URL)
        elif opcion == 4:
            view_favoritos(URL)
        elif opcion == 5:
            print("Deteniendo programa")
            exit()
        else:
            print("Opción inválida")

    
    
