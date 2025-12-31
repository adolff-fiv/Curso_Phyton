# Calcular IMC

Edad = int(input("Ingrese su edad "))
Peso = float(input("Ingrese su peso en kilogramos "))
Estatura = float(input("Ingrese su estatura en metros "))
Imc = Peso / Estatura ** 2

if Estatura > 3 or Estatura < 1.20:
    print("Estatura ingresada inválida")

if Peso < 30 or Peso > 180:
    print("Peso ingresado inválido")

if Edad >= 20 and Edad < 105:
    if Imc >= 0 and Imc < 18.5:
        print("Bajo peso")
    elif Imc >= 18.5 and Imc < 25:
        print("Peso saludable ")
    elif Imc >= 25 and Imc < 30:
        print("Sobrepeso")
    elif Imc >= 30:
        print("Obesidad")
    else:
        print("Valores digitados incorrectos")
else:
    print("Edad ingresada erronea, tu edad debe ser real y mayor a 20 años para poder hallar el IMC")

