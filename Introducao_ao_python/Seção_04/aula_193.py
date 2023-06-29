"""
Exercício - Lista de tarefas com opções
de desfazer e refazer.

Criado: 29/06/2023 09:55

Autor: Vitor
"""
def listar(tarefas) -> None:
    """Utilizado para listar as tarefas."""
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('TAREFAS:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')


def desfazer(tarefas, tarefas_refazer) -> None:
    """Utilizado para desfazer as tarefas da lista."""
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)


def refazer(tarefas, tarefas_refazer) -> None:
    """Utilizado para refazer as tarefas da lista."""
    print()
    if not tarefas:
        print('Nenhuma tarefa para refazer')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)


def adicionar(tarefa, tarefas) -> None:
    """Utilizado para adicionar tarefas."""
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa')
        return
    
    tarefas.append(tarefa)


tarefas = []
tarefas_refazer = []

while True:
    print()
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite um tarefa ou comando: ').lower()

    if tarefa == 'listar':
        listar(tarefas)
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        

