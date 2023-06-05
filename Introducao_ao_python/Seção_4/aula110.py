from itertools import groupby

alunos = [
    {'Nome': 'Vitoria', 'Nota': 'A'},
    {'Nome': 'Luiz', 'Nota': 'B'},
    {'Nome': 'Vitor', 'Nota': 'B'},
    {'Nome': 'Mateus', 'Nota': 'C'},
    {'Nome': 'Vania', 'Nota': 'A'},
    {'Nome': 'Raquel', 'Nota': 'A'},
    {'Nome': 'Pedro', 'Nota': 'C'},
    {'Nome': 'Fernando', 'Nota': 'B'},
    {'Nome': 'Maria', 'Nota': 'C'},
    {'Nome': 'João', 'Nota': 'A'},
]


def ordena_dicionario(dicionario):
    return dicionario['Nota']


alunos_agrupados = sorted(alunos, key=ordena_dicionario)
grupos = groupby(alunos_agrupados, key=ordena_dicionario)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
