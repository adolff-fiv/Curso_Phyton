#Sistema básico de encriptación "La cifra del Cesar"

Alfabeto = "abcdefghijklmnñopqrstuvwxyz"
Corrimiento = int(input("Ingrese el corrimiento "))

for i in range(5):
    Mensajes = str(input("Ingrese los mensajes a encriptar "))
    Encriptado = ""
    for caracter in Mensajes:
        if caracter.lower() in Alfabeto:
            variable = caracter.lower()
            Indice = Alfabeto.find(variable)
            Indice = (Indice + Corrimiento) % 27
            Encriptado = Encriptado + Alfabeto[Indice]
        else:
            Encriptado = Encriptado + caracter
    print(Encriptado)

