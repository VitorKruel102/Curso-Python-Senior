"""
Relações entre classes: Associação, agregação e composição.

Criado: 05/07/2023 19:30

Author: Vitor Kruel.
"""


class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome) -> None:
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')

escritor.ferramenta = maquina_de_escrever

print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())