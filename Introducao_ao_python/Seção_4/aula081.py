# Funções lambda:

lista = [
    {'nome': 'Vitor', 'sobrenome': 'Kruel'},
    {'nome': 'Pedro', 'sobrenome': 'Silva'},
    {'nome': 'Maria', 'sobrenome': 'Manoel'},
    {'nome': 'Joao', 'sobrenome': 'Hiaj'},
    {'nome': 'Carlos', 'sobrenome': 'Fonseca'},
]

lista_alterada = sorted(lista, key=(lambda item: item['nome']))

print(lista)
print(lista_alterada)
