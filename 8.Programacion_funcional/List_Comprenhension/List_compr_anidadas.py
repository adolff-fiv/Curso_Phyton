# Una list comprehension anidada es una lista de listas

matriz = [[1,2,3],[4,5,6],[7,8,9]]

lista = [valor for sublista in matriz for valor in sublista]
print(f'Lista anidada: {lista}')

lista_pares = [valor for sublista in matriz for valor in sublista if valor % 2 == 0]
print(f'Lista de números pares: {lista_pares}')