"""
Escopo de classe e de métodos de clases

Criado: 01/07/2023 18:01

Autor: Vitor Kruel
"""
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        """."""
        return f'{self.nome} está comendo {alimento}...'

    def executar(self, *args, **kwargs):
        """."""
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('Carne'))