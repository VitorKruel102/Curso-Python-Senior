"""
Salvando e lendo dados Python em Json

Criado: 28/06/2023 09:49

Autor: Vitor Kruel
"""
import json
import os


from pprint import pprint


BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')

pessoas = [
    {
        "Nome:": "Vitor",
        "Sobrenome": "Kruel da Silva",
        "Estado": "RS",
        "Cidade": "São Leopoldo",
        "Idade": 22,
        "Telefone": {
            "Residencial": "00 0000-0000",
            "Pessoal": "00 0 0000-0000"
        }
    },
    {
        "Nome:": "Vitória Carolina",
        "Sobrenome": "Dias da Silva",
        "Estado": "RS",
        "Cidade": "Guaíba",
        "Idade": 22,
        "Telefone": {
            "Residencial": "00 0000-0000",
            "Pessoal": "00 0 0000-0000"
        }
    },
    {
        "Nome:": "Vânia",
        "Sobrenome": "Renner Kruel",
        "Estado": "RS",
        "Cidade": "São Leopoldo",
        "Idade": 49,
        "Telefone": {
            "Residencial": "00 0000-0000",
            "Pessoal": "00 0 0000-0000"
        }
    }
]

with open(SAVE_TO, 'w', encoding='utf-8') as arquivo:
    json.dump(pessoas, arquivo, indent=2, ensure_ascii=False)
    # indent -> Coloca espaços de separação do arquivo
    # ensure_ascii -> Aceita acentuação

with open(SAVE_TO, 'r', encoding='utf-8') as arquivo:
    pessoas = json.load(arquivo)
    pprint(pessoas)
