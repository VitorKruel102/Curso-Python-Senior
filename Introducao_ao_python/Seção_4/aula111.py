def print_iter(iterator):
    """."""
    print(*list(iterator), sep='\n')
    print()


def aumentar_porcentagem(valor, porcentagem):
    """."""
    return round(valor * porcentagem, 2)


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 4', 'preco': 15.00},
    {'nome': 'Produto 3', 'preco': 12.00},
    {'nome': 'Produto 2', 'preco': 13.00},
    {'nome': 'Produto 1', 'preco': 14.00},
]

novos_produtos = [
    {
        **produto, 
        'preco': aumentar_porcentagem(produto['preco'], 1.1)
    }
    for produto in produtos
]


print_iter(produtos)
print_iter(novos_produtos)

print(*produtos)