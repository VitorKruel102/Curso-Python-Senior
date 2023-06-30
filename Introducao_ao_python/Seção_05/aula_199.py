"""
Introdução ao método __init__(Inicializador de atributos)

Criado: 30/06/2023 15:35

Autor: Vitor Kruel
"""


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    

    def nome_completo(self):
        """."""
        return f'{self.nome} {self.sobrenome}'


pessoa_01 = Pessoa('Vitor', 'Kruel') # Criando uma instância
pessoa_02 = Pessoa('Vitória', 'Dias')

print(pessoa_01.nome_completo())  # Acessando os atributos
print(pessoa_02.nome_completo())  # Acessando os atributos

