# Conversión de entero a Romano

Número = int(input("Ingrese un número menor a 4000 "))

if Número >= 4000 or Número < 1:
    print("Número ingresado inválido")

"""
Descomposición numérica
"""

Millar = (int(Número / 1000)) * 1000
Centena = int((Número - Millar)/100)*100
Decena = (int((Número - Millar - Centena) / 10)) * 10
Unidad = int((Número - Millar - Centena - Decena / 1)) * 1

Romano = str()

"""
Validaciónes de los millares
"""

if Millar == 3000:
    Romano += "MMM"
elif Millar == 2000:
    Romano += "MM"
elif Millar == 1000:
    Romano += "M"
if Centena == 900:
    Romano += "CM"
elif Centena == 800:
    Romano += "DCCC"
elif Centena == 700:
    Romano += "DCC"
elif Centena == 600:
    Romano += "DC"
elif Centena == 500:
    Romano += "D"
elif Centena == 400:
    Romano += "CD"
elif Centena == 300:
    Romano += "CCC"
elif Centena == 200:
    Romano += "CC"
elif Centena == 100:
    Romano += "C"
if Decena == 90:
    Romano += "XC"
elif Decena == 80:
    Romano += "LXXX"
elif Decena == 70:
    Romano += "LXX"
elif Decena == 60:
    Romano += "LX"
elif Decena == 50:
    Romano += "L"
elif Decena == 40:
    Romano += "XL"
elif Decena == 30:
    Romano += "XXX"
elif Decena == 20:
    Romano += "XX"
elif Decena == 10:
    Romano += "X"
if Unidad == 9:
    Romano += "IX"
elif Unidad == 8:
    Romano += "VIII"
elif Unidad == 7:
    Romano += "VII"
elif Unidad == 6:
    Romano += "VI"
elif Unidad == 5:
    Romano += "V"
elif Unidad == 4:
    Romano += "IV"
elif Unidad == 3:
    Romano += "III"
elif Unidad == 2:
    Romano += "II"
elif Unidad == 1:
    Romano += "I"

print(Romano)