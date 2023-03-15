# While:
condicao = True

while condicao:
    nome = input('Qual é o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou!') 
