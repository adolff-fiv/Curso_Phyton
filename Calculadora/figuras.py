import math

def op_cuadrado(lado):
    perimetro = lado * 4
    area = lado * lado
    return perimetro, area

def op_rectangulo(base, altura):
    perimetro = (base + altura) * 2 
    area = altura * base
    return perimetro, area

def op_circulo(radio):
    perimetro = math.pi * (2 * radio)
    area = (radio * radio) * math.pi
    return perimetro, area


def op_hexágono(lado, apotema):
    perimetro = lado * 6
    area = (perimetro * apotema) / 2
    return perimetro, area

def op_triángulo(ladoa, ladob, ladoc):
    perimetro = ladoa + ladob + ladoc
    semp = perimetro / 2
    area = math.sqrt(semp * (semp - ladoa) * (semp - ladob) * (semp - ladoc) )
    return perimetro, area