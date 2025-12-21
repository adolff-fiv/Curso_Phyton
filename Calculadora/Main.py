# Menu

from Menu_Operaciones_básicas import *
from Menu_Sistemas_numericos import *
from Menu_Figuras_geometricas import menu_fig_geo 

opcion = 0


print(" \n---------------------------\n"
          "-       CALCULADORA       \n"
          "--------------------------\n"
          "- 1.Operaciones básicas   \n"
          "- 2.Conversión de bases   \n"
          "- 3.Figuras geométricas   \n"
          "- 4.Salir del programa    \n"
          "--------------------------\n")
opcion = int(input("Ingrese una opción "))
if opcion == 1:
    print    ("\n-Digite la operación que desea ejecutar-\n"
              "\n-1= Suma                                \n"
              "\n-2= Resta                               \n"
              "\n-3= Multiplicación                      \n"
              "\n-4 = División                           \n"
              "\n-5 = Potencia                           \n"
              "\n-6 = Módulo                             \n"
              "\n-7 = Raíz cuadrada                      \n"
              "\n-8 = Raíz cúbica                        \n")
    op()
elif opcion ==2:
    sistmn()
elif opcion == 3:
    menu_fig_geo()
elif opcion == 4:
    print("\n--- Adios ---")
    exit
else:
    print("Respuesta invalida")
    

