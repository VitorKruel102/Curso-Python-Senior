"""Exercicio:"""
carrinho_de_compras = []

while True:    
    modifica_carrinho = input(
        'Você deseka inserir[i], apagar[a],'
        'listar[l] suas compras ou finalizar compra[f]? '
    ).lower()

    if modifica_carrinho == 'i':
        produto = input('Informe o nome do produto: ').lower()
        carrinho_de_compras.append(produto)
        print(
            f'Este é a suas lista de compras: {carrinho_de_compras}'
        )
    elif modifica_carrinho == 'a':
        print(
            f'Este é a suas lista de compras: {carrinho_de_compras}'
        )
        produto = input('Informe o nome do produto que deseja apagar: ').lower()

        if not produto in carrinho_de_compras:
            print(
                'Não temos esse produto na lista, tente novamente mais tarde.'
            )
            continue

        for index, item in enumerate(carrinho_de_compras):
            if item == produto:
                carrinho_de_compras.pop(index)
    elif modifica_carrinho == 'l':
        print(
            f'Este é a suas lista de compras: {carrinho_de_compras}'
        )
    elif modifica_carrinho == 'f':
        print(
            f'Este é a suas lista de compras: {carrinho_de_compras}\n'
            'Suas compras estão finalizadas. Obrigado pela preferência.'
        )
        break
    else:
        print('Dígite uma solicitação valida!')
    