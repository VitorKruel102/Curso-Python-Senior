# isistance() - Analisa o tipo de um dado

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'}
]

for item in lista:
    if isinstance(item, set): # Ver se o tipo do item é set()
        print(item)
    if isinstance(item, str): # Ver se o tipo do item é str()
        print(item.upper())
    if isinstance(item, (int, float)): # Ver se o tipo do item é int() or float()
        print(item * 2)