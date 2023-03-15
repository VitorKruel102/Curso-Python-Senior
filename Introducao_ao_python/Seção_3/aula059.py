# Desempacotamento em chamadas
string = 'ABCD'
lista = ['Maria', 'Helena', 'Eduarda', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

a, b, *_, u = lista
print(u)

for nome in lista:
    print(nome)

print(*string) # Desempacotamento
print(*lista) # Desempacotamento
print(*tupla) # Desempacotamento