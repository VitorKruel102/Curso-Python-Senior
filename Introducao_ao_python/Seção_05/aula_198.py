"""
Como funciona uma classe?

Criado: 30/06/2023 15:35

Autor: Vitor Kruel
"""

# Objetos ou Instancias == Class
class Pessoa: # Convenção usamos PastalCase 
    ... # Dados dentro de Class são Atributos
    


pessoa_01 = Pessoa() # Criando uma instância
pessoa_02 = Pessoa()

pessoa_01.nome = 'Vitor'
pessoa_01.sobrenome = 'Kruel'
print(pessoa_01.nome)  # Acessando os atributos
print(pessoa_01.sobrenome)