import json
import os

from aula_206_a import Pessoa


CAMINHO_ARQUIVO = r'C:\Users\vkrue\OneDrive\Área de Trabalho\GitHub\Curso-Python-Senior\Introducao_ao_python\Seção_05\arquivo-pessoa.json'


with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

pessoa_01 = Pessoa(**dados)
print(vars(pessoa_01))
