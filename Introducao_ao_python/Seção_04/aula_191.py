"""
Problema dos parâmetros mutáveis em funções
em Python

Criado: 29/06/2023 09:21

Autor: Vitor Kruel
"""
# É recomendado não utilizar parâmetros mutáveis como padrão
# das funções;

def adiciona_clientes(nome, lista=[]): #Forma errada
    """."""
    lista.append(nome)
    return lista

clientes1 = adiciona_clientes('Luiz')
adiciona_clientes('Joana', clientes1)
print(clientes1)

clientes2 = adiciona_clientes('Maria')
adiciona_clientes('Helena', clientes2)
print(clientes2)

print('=' * 40)

def adiciona_clientes(nome, lista=None): #Forma Correta
    """."""
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

clientes1 = adiciona_clientes('Luiz')
adiciona_clientes('Joana', clientes1)
print(clientes1)

clientes2 = adiciona_clientes('Maria')
adiciona_clientes('Helena', clientes2)
print(clientes2)
