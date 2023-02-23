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

conjunto_numerico.append(50) # Add itens ao final
ultimo_valor = conjunto_numerico.pop() # Remove e retorna o último item 
primeiro_valor = conjunto_numerico.pop(0) # Remove e retorna o primeiro item
print(conjunto_numerico, f'{ultimo_valor=}', f'{primeiro_valor=}', sep=' --> ')