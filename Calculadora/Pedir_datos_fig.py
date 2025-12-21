def ped_dat_fig(figura):
    if figura == "cuadrado":
        lado = int(input("Ingrese el lado del cuadrado" ))
        return lado
    elif figura == "rectangulo":
        base = int(input("Ingrese la base del rectángulo "))
        altura = int(input("Ingrese la altura del rectángulo "))
        return base, altura
    elif figura == "circulo":
        radio = int(input("Ingrese el radio del círculo "))
        return radio
    elif figura == "hexagono":
        hexágono = int(input("Ingrese el lado del hexágono "))
        apotema = int(input("Ingrese el apotema del hexágono "))
        return hexágono, apotema
    elif figura == "triangulo":
        ladoa = int(input("Ingrese el lado a del triángulo "))
        ladob = int(input("Ingrese el lado b del triángulo "))
        ladoc = int(input("Ingrese el lado c del triángulo "))
        return ladoa, ladob, ladoc