primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(
        f'{primeiro_valor=} é maior'
        f'que o {segundo_valor=}'
    )
elif primeiro_valor == segundo_valor:
    print(
        f'{primeiro_valor=} é igual'
        f'ao {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'que o {primeiro_valor=}'
    )
