import json
import os

from aula_206_a import Pessoa, PATH_ARQUIVO


with open(PATH_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

pessoa_01 = Pessoa(**dados)
print(vars(pessoa_01))
