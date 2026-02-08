""" Pedir números al usuario y devolver el mes del año del número mediante tuplas"""

meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre"
         , "noviembre", "diciembre")



def funcion():
    respuesta = None
    try:
        while respuesta != 0:
            num =int((input("Ingrese el número del mes que desea ver o 0 si desea cerrar el programa ")))
            if 1 <= num <= 12:
                print(f"{num} = {meses[num - 1]}")
            elif num == 0:
                print("Cerrando programa".center(50, "-"))
                respuesta = 0
            else:
                print("ERROR - El número digitado no es un mes existente")
                funcion()   
    except Exception as e:
        print(e)
        print("Ha ocurrido un error inesperado, por favor intente de nuevo\n")
        funcion()
funcion()
        

    



