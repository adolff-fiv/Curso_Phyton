def decimal():
    num = int(input("Ingrese un número decimal (Base 10) "))
    alt = int(input("\n-Ingrese la base a la que desea convertirlo\n"
                    "--------------------------                   \n"
                    "- 1.Base binaria                             \n"
                    "- 2.Base octal                               \n"
                    "- 3.Base hexadecimal                         \n"))
    if alt == 1:
        return bin(num)
    elif alt == 2:
        return oct(num)
    elif alt == 3:
        return hex(num)
    else:
        print("Opción invalida")


def Binario():
    num = (input("Ingrese un número decimal (Base 2) "))
    alt = int(input("\n-Ingrese la base a la que desea convertirlo\n"
                    "--------------------------                   \n"
                    "- 1.Base decimal                             \n"
                    "- 2.Base octal                               \n"
                    "- 3.Base hexadecimal                         \n"))
    if alt == 1:
        return int(num, base=2) 
    elif alt == 2:
        num = int(num, base=2)
        return oct(num)
    elif alt == 3:
        num = int(num, base=2)
        return hex(num)
    else:
        print("Opción invalida")


def Octal():
    num = (input("Ingrese un número decimal (Base 8) "))
    alt = int(input("\n-Ingrese la base a la que desea convertirlo\n"
                    "--------------------------                   \n"
                    "- 1.Base decimal                             \n"
                    "- 2.Base binario                             \n"
                    "- 3.Base hexadecimal                         \n"))
    if alt == 1:
        return int(num, base=8)
    elif alt == 2:
        f = int(num, base=8)
        return bin(f)
    elif alt == 3:
        f = int(num, base=8)
        return f''' {hex(f)} '''
    else:
        print("Opción invalida")

def Hexa():
    num = (input("Ingrese un número decimal (Base 16) "))
    alt = (input("\n-Ingrese la base a la que desea convertirlo\n"
                    "--------------------------                   \n"
                    "- 1.Base decimal                             \n"
                    "- 2.Base binario                             \n"
                    "- 3.Base octal                               \n"))
    if alt == 1:
        return int(num, base=16)
    elif alt == 2:
        num = int(num, base=16)
        return bin(num)
    elif alt == 3:
        num = int(num, base=16)
        return oct(num)
    else:
        print("Opción invalida")

