"""
Herança simples.

Criado 12/07/2023 10:14

Autor: Vitor Kruel
"""

"""
Classe Principal (Pessoa)
   -> SuperClasse, BaseClass, ParentClasse

Classe Filha (Cliente)
   -> SubClass, ChildClass, DerivedClass

 |  Method resolution order:
 |      Cliente
 |      Pessoa
 |      builtins.object

"""

class Pessoa:
   def __init__(self, nome, sobrenome) -> None:
      self.nome = nome
      self.sobrenome = sobrenome

   def falar_nome_classe(self):
      print('CHEGUEI NA CLASSE PESSOA')
      print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
   def falar_nome_classe(self):
      print('CHEGUEI NA CLASSE CLIENTE')
      print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
   pass



cliente1 = Aluno('Vitória', 'Dias')
cliente1.falar_nome_classe()

cliente2 = Cliente('Vitor', 'Kruel')
cliente2.falar_nome_classe()

# help(Cliente)