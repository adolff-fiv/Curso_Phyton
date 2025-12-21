# Tienda de descuentos

Pago = int(input("\n------------------------------------------------------------------\n"
                 "- Seleccione el medio de pago con el cual desea realizar su compra -\n"
                 "--------------------------------------------------------------------\n"
                 "-    1. En Efectivo                                                -\n"
                 "-    2. En Tarjeta de Crédito                                      -\n"))

if Pago != 1 and Pago != 2:
    print("Medio de pago no válido")

Compra = float(input("Ingrese el costo de su compra "))

if Compra <= 0:
    print("El valor de la compra ingresado es inválido, por favor intente de nuevo")

# PAGO EN EFECTIVO

if Pago == 1:
    Descuento1 = Compra * 0.2
    Descuento2 = Compra * 0.3
    Descuento3 = Compra * 0.4
    
    if Compra > 0 and  Compra <= 10000:
        print("Su descuento es del 20%")
        print(f'Su monto a pagar es: { Compra - Descuento1}')
    elif Compra > 10000 and Compra <= 20000:
        print("Su descuento es del 30%")
        print(f'Su monto a pagar es: { Compra - Descuento2}')
    else:
        print("Su descuento es del 40%")
        print(f'Su monto a pagar es: { Compra - Descuento3}')

# PAGO CON TARJETA DE CRÉDITO

if Pago == 2:
    Descuento4 = Compra * 0.1
    Descuento5 = Compra * 0.15
    Descuento6 = Compra * 0.2
    
    if Compra > 0 and  Compra <= 10000:
        print("Su descuento es del 10%")
        print(f'Su monto a pagar es: { Compra - Descuento4}')
    elif Compra > 10000 and Compra <= 20000:
        print("Su descuento es del 15%")
        print(f'Su monto a pagar es: { Compra - Descuento5}')
    else:
        print("Su descuento es del 20%")
        print(f'Su monto a pagar es: { Compra - Descuento6}')