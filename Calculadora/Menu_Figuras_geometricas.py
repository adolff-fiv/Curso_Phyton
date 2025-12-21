from Pedir_datos_fig import *
from figuras import *

def menu_fig_geo():
    opcion = 0
    while opcion != 6:
        print("\n------------------------\n"
              "-   Figuras Geometricas   \n"
              "--------------------------\n"    
              "- 1.Cuadrado              \n"
              "- 2.Rectangulo            \n"
              "- 3.Circulo               \n"
              "- 4.Hexagono              \n"        
              "- 5.Triangulo             \n"
              "- 6.Salir                 \n")
        opcion = int(input("ingrese su opcion "))
        if opcion == 1: 
            perimetro, area = op_cuadrado(ped_dat_fig("cuadrado"))
            print(f'El perímetro es igual a {perimetro}, mientras que el area el igual a {area} ')
        elif opcion == 2: 
            base, altura = ped_dat_fig("rectangulo")
            perimetro, area = op_rectangulo(base, altura)
            print(f'El perímetro es igual a {perimetro}, mientras que el area el igual a {area} ')
        elif opcion == 3: 
            radio = ped_dat_fig("circulo")
            perimetro, area = op_circulo(radio)
            print(f'El perímetro es igual a {perimetro}, mientras que el area el igual a {area} ')
        elif opcion == 4: 
            lado, apotema = ped_dat_fig("hexagono")
            perimetro, area = op_hexágono(lado, apotema)
            print(f'El perímetro es igual a {perimetro}, mientras que el area el igual a {area} ')
        elif opcion == 5: 
            ladoA, ladoB, ladoC = ped_dat_fig("triangulo")
            perimetro, area = op_triángulo(ladoA, ladoB, ladoC)
            print(f'El perímetro es igual a {perimetro}, mientras que el area el igual a {area} ')
        elif opcion == 6:
            print("")
        else:
            print("Opción inválida")