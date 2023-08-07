"""
Criando Exceptions em Python Orientado a Objetos

Criado: 07/08/2023 13:15

Author: Vitor Kruel.
"""


class MeuError(Exception):


    pass


def levantar():
    exception_ = MeuError('a', 'd', 'c') 
    exception_.add_note('Você errou isso')
    raise exception_

try:
    levantar()
except MeuError as error:
    print(error)
    raise