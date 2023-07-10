"""
Composição é uma especialização da agregação.

Criado: 10/07/2023 10:59

Autor: Vitor Kruel.
"""

# Composição: Nela, quando o objeto "pai" for apagado, 
# todas as referências do objeto filho também são apagador

class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.enderecos = []

    def insetir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero)) # Composição: criando a instância dentro de outra classe.

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print(f'APAGANDO {self.nome, self.enderecos}')


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print(f'APAGANDO {self.rua, self.numero}')

cliente1 = Cliente('Maria')
cliente1.insetir_endereco('AV Brasil', 54)
cliente1.insetir_endereco('Rua B', 554)
cliente1.listar_enderecos()

del cliente1

print('******************** TERMINOU MEU CODIGO ********************')