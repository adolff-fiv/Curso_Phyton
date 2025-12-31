#Máquina registradora

# Contador_500 = 0
# Contador_500 = 0
# Contador_500 = 0
# Contador_500 = 0

Total_Pago = float(input("Ingrese el monto total a pagar "))
Pago_Cliente = float(input("Ingrese la cantidad en efectivo con la cual va a pagar "))
Vuelto = Pago_Cliente - Total_Pago

if Pago_Cliente < Total_Pago:
    print("Dinero insuficiente")
else:
    contador_quinientos = int(Vuelto / 500)
    aux_1 = Vuelto - (contador_quinientos * 500)
    contador_cien = int(aux_1 /100 )
    aux2 = aux_1 - (contador_cien * 100)
    contador_cincuenta = int(aux2 /50 )
    aux3 = aux2 - (contador_cincuenta * 50)
    contador_diez = int(aux3 /10 )
    aux4 = aux3 - (contador_diez * 10)
    contador_uno = int(aux4 /1 )
    
print(f'Su vuelto es de {Vuelto} y recibirá {contador_quinientos} billetes de 500, {contador_cien} billetes de 100, {contador_cincuenta} billetes de 50, {contador_diez} billetes de 10 y {contador_uno} billetes de 1 '  ) 