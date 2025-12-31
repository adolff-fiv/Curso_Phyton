# Jubilación

Edad = int(input("Ingrese su edad: "))
Sexo = str(input("Ingrese du sexo: "))

if Edad >= 60 and Edad < 105 and Sexo == "Masculino" or  Edad >= 54 and Edad < 105 and Sexo == "Femenino":
    print("Usted ya puede jubilarse")
elif Edad > 105 or Edad < 0:
    print("Edad ingresada inválida")
elif Sexo != "Masculino" or "Femenino":
    print("Sexo ingresado inválido")

else:
    print("Aún no puedes jubilarte")

# print("Usted ya puede jubilarse") if Edad >= 60 and Sexo == "Masculino" or Edad >= 54 and Sexo == "Femenino" else print("Aún no puedes jubilarte")
    