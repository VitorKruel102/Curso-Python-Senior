"""
Atributo de Classe.

Criado: 03/07/2023 12:08

Autor: Vitor Kruel
"""
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        self.ano_atual = 2022 
        """
        São duas variavel diferentes:
            self.ano_atual != Pessoa.ano_atual
        
        Uma é a variável de instancia e outra da classe;
        """
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

pessoa_01 = Pessoa(nome='Vitor', idade=22)
pessoa_02 = Pessoa(nome='Vitória', idade=22)

print(pessoa_01.get_ano_nascimento())
print(pessoa_02.get_ano_nascimento())