__all__ = [
    'variavel',
    'soma',
] 
"""Quando chamado todo o modulo (*), só o que tiver dentro
do __all__ será permitido o acesso.
"""


variavel = 'Nome'

def soma(x, y):
    return x + y