"""
Exercicio com classes.

Criado: 10/07/2023 11:20

Autor: Vitor Kruel.
"""
class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, nome):
        self._motor = nome

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, nome):
        self._fabricante = nome


class Motor:
    def __init__(self, nome) -> None:
        self.nome = nome


class Fabricante:
    def __init__(self, nome) -> None:
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')

fusca.fabricante = volkswagen
fusca.motor = motor_1_0

print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)