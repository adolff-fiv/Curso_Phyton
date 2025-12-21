#Edad de n asistentes a evento

n = int(input("Ingrese el número de asistentes "))

if n < 1:
    print("Número ingresado inválido")

mayor = -1
menor = 999

for i in range(n):
    edades = int(input(f"Escriba la edad del asistente N.{i + 1} "))
    if edades > mayor:
        mayor = edades
    elif edades < menor:
        menor = edades

if 0 > mayor or mayor > 125 or 0 > menor or menor > 125:
    print("Edad de los asistentes inválida")
else:
    print("\n El asistente con mayor edad tiene ", mayor ," años"
      "\n El asistente con menor edad tiene ", menor ,"  años") 
    


    

