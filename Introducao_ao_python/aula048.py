# Listas
string = 'ABCDE'

lista = ['Vitória', 123, True, 1.2, []]
lista[-5] = 'Vitória Dias'

conjunto_numerico = [10, 20, 30, 40]
conjunto_numerico[2] = 300 # Update

numero = conjunto_numerico[2]
print(conjunto_numerico, f'{numero=}', sep=' --> ')

del conjunto_numerico[0] # Delete
print(conjunto_numerico)