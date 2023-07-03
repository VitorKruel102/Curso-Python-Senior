"""
@staticmethod (métodos estátios)

Criado: 03/07/2023 13:29

Autor: Vitor Kruel
"""
class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)


def funcao(*args, **kwargs):
    print('Oi', args, kwargs)   


Classe.funcao_que_esta_na_classe(1, 2, 3)
funcao(1, 2, 3)

Classe.funcao_que_esta_na_classe(nomeado=1)
funcao(nomeado=1)