# Criando um range em uma lista:
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

# List Comprehension:
lista = [x for x in range(10)]
print(lista)

# Mapeamento de dados em List Comprehension:
lista = [numero * 2 for numero in lista]
print(lista)

produtos = [
    {'nome': 'p1', 'preco': 10,},
    {'nome': 'p2', 'preco': 20,},
    {'nome': 'p3', 'preco': 30,},
]

novos_produtos = [ {**produto, 'preco': produto['preco'] * 1.05} for produto in produtos]
print(novos_produtos)