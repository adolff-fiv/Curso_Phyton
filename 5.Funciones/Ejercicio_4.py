#Secuencia de Collatz

def collartz():
    pasos = 1

    num = int(input("Digite un número mayor que uno "))

    if num > 1:
        while num != 1:
            if num % 2 == 0:
                num = num / 2
            else:
                num = 3 * num + 1
            print(f'paso {pasos} = {num}')
            pasos += 1
    else:
        print("El número tiene que ser mayor a uno")


