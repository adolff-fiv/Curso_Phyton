from Sistemas_numéricos import *

def sistmn():
    print(" \n------------------------\n"
          "-¿Qué base desea convertir?\n"
          "---------------------------\n"
          "- 1.Decimal               -\n"
          "- 2.Binario               -\n"
          "- 3.Octal                 -\n"
          "- 4.Hexadecimal           -\n"
          "---------------------------\n")
    opc = int(input())
    if opc == 1:
        print(decimal())
    elif opc == 2:
        print(Binario())
    elif opc == 3:
        print(Octal())
    elif opc == 4:
        print(Hexa())