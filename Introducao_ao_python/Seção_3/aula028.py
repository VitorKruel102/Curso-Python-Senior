while True:
    try:
        nome = input('Dígite o seu nome: ')
        valida_nome = int(nome)
        print('Nome inválido')
    except ValueError:
        while True:
            try:
                idade = input('Dígite sua idade: ')
                valida_idade = int(idade)
                break
            except ValueError:
                print('Idade incorreta')
        break

if nome:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')  
else:
    print('Desculpe, você deixou campos vazios.')

