# Empacotamento e Desempacotamento de dicionários.
a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenoma': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa} #Desempacotamento
print(pessoas_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    """."""
    print('NÃO NOMEADOS: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(1, 2, nome='Vitor', idade=28)
