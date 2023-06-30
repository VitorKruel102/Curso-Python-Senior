"""
Métodos em instâncias de classe Python

Criado: 30/06/2023 15:55

Autor: Vitor Kruel
"""
class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome

    def acelerar(self):
        """."""
        print(f'{self.nome} está acelerando...')     


fusca = Carro(nome='Fusca')
celta = Carro(nome='Celta')

print(fusca.nome)
fusca.acelerar()

print(celta.nome)
celta.acelerar()
