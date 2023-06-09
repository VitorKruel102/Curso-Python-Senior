from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 4', 'preco': 15.00},
    {'nome': 'Produto 3', 'preco': 12.00},
    {'nome': 'Produto 2', 'preco': 13.00},
    {'nome': 'Produto 1', 'preco': 14.00},
]

def funcao_do_reduce(acumulador, produto):
    """."""
    return acumulador + produto['preco']

total = reduce(
    funcao_do_reduce,
    produtos,
    0 # Valor Inicial
)

print(total)