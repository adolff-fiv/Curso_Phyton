a = {1,2,3,4,5,6,7,8,9,10}
b = {1,3,90,67,7,0}
c = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}

# Unión de conjuntos
union = a|b
print(f'La unión de a y b es: {union}')

# Intersección de conjuntos
interseccion = a&b
print(f'La intersección de a y b es: {interseccion}')

# Diferencia de conjuntos
diferencia = a-b
print(f'La diferencia de a b es: {diferencia}')

diferencia2 = b-a
print(f'La diferencia de b a es: {diferencia2}')

# Diferencia simétrica de conjuntos
simetrica = a^b 
print(f'La diferencia simétrica de a b = {simetrica}')

# Si a es subconjunto de b
subconjunto = a.issubset(b)
print(f"¿a es subconjunto de b? = {subconjunto}")

# Si a es superconjunto de b
superconjunto = a.issuperset(b)
print(f"¿a es superconjunto de b? = {superconjunto}")

# Si a y b son disconexos
disconexo = a.isdisjoint(b)
print(f"¿a y b son disconexos? = {disconexo}")