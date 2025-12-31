"""
edad = int(input("Ingrese su edad "))
if (edad >= 18):
    print("Puedes entrar a la disco")
else:
    print("No puedes entrar a la disco")
"""
Edad = int(input("Ingrese su edad "))
if 18 <= Edad < 60:
    print("Eres mayor de edad")
elif 60 <= Edad <= 100:
    print("Perteneces a la tercera edad, eres un abuelito")
elif 0 <= Edad < 18:
    print("No eres mayor de edad")
else:
    print("La edad ingresada es inválida")