# Exercício - Sistema de perguntas e respostas;

perguntas = [
    {
        'Questão': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Questão': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Questão': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

quantidade_acertos = 0
for pergunta in perguntas:
    questao = pergunta['Questão']
    opcao = pergunta['Opções']
    resposta_certa = pergunta['Resposta']

    print(f'''
Pergunda: {questao}\n
Opção: 
0){opcao[0]}
1){opcao[1]}
2){opcao[2]}
3){opcao[3]}
    ''')

    resposta_user = input('Escolha a opção: ')
    try:
        if opcao[int(resposta_user)] == resposta_certa:
            print('Acertou')
            quantidade_acertos += 1
        else:
            print('Errou')
    except ValueError:
        print('Errou')

print(f"""
Você acertou {quantidade_acertos}
de {len(perguntas)} perguntas.
""")

    
    