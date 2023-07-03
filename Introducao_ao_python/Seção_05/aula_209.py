"""
Métodos de classe(@classmethod) + factories(fábricas).

Criado: 03/07/2023 12:58

Autor: Vitor Kruel
"""
class Pessoa:
    ano = 2023 # Atributo de classe

    def __init__(self, nome, idade) -> None: # Método
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey!')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def cria_sem_nome(cls, idade):
        return cls('Anônima', idade)


pessoa_01 = Pessoa(nome='Vitor', idade=23)
pessoa_02 = Pessoa.criar_com_50_anos('Glaci')
pessoa_03 = Pessoa.cria_sem_nome(25)

print(pessoa_01.nome)
print(pessoa_02.nome)
print(pessoa_03.nome)
