import json
import os


BASE_DIR = os.path.dirname(__file__)
PATH_ARQUIVO = os.path.join(BASE_DIR, 'arquivo-pessoa.json')

class Pessoa:
    def __init__(self, nome, sobrenome, idade, sexo, cidade, estado) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.sexo = sexo
        self.cidade = cidade
        self.estado = estado
    

pessoa_01 = Pessoa(
    nome='Vitor',
    sobrenome='Kruel',
    idade=23,
    sexo='Masculino',
    cidade='São Leopoldo',
    estado='RS'
)    

def fazer_dump():
    with open(PATH_ARQUIVO, 'w+', encoding='utf-8') as arquivo:
        json.dump(vars(pessoa_01), arquivo, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    fazer_dump()