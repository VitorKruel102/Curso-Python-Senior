# Reatribuir valor
"""Nesse exemplo abaixo, o valor do outra_variavel,
se manteria 'Vitor', mesmo alterando reatribuindo
outro valor dentro da variavel nome.
"""
nome = 'Vitor'
outra_variavel = nome
nome = 'Vitoria'

print(nome)
print(outra_variavel)

"""Porém, nesse caso abaixo, a lista_a e lista_b estão
apontando para o mesmo espaço da memória, ou seja, se
a variavel lista_a for reatribuida em outros nomes, a
lista_b também será modificada.
"""
lista_a = ['Vitor', 'Vitoria']
lista_b = lista_a
lista_a[0] = 'Joao'
print(lista_a)
print(lista_b)