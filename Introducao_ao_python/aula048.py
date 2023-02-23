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

conjunto_numerico.clear() # Limpar lista
print(conjunto_numerico)

conjunto_numerico = [10, 20, 30, 40]
conjunto_numerico.insert(0, 5) # Adicionar um item em determinado indice
print(conjunto_numerico)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) # Adiciona a Lista_b na lista_a

print(lista_c, f'{lista_a=}', sep=' --> ')