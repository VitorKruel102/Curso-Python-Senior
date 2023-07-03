"""
__dict__ e vars para atributos de instância.

Criado: 03/07/2023 12:18

Autor: Vitor Kruel
"""
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
dados = {'nome': 'Vitor', 'idade': 22}
pessoa_01 = Pessoa(**dados)

print(pessoa_01.__dict__)
print(vars(pessoa_01))