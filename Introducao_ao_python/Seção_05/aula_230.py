"""
abstractmethod para qualquer método já decorado.

Criado: 17/07/2023 17:08

Author: Vitor Kruel
"""

"""
Podemos utilizar com @property, @property.setter, 
@classmethod, @staticmethod ou métodos normais.

Foo ou Bar - É utilizado como Placeholder, ou seja, 
você pode colocar qualquer palavra que quiser.
"""
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, nome):
        self._nome = None
        self.nome = nome
        

    @property
    def nome(self): 
        return self._nome

    @nome.setter
    @abstractmethod
    def nome(self, nome): ...


class Foo(AbstractFoo):
    def __init__(self, nome):
        super().__init__(nome)

    @AbstractFoo.nome.setter
    def nome(self, nome):
        self._nome = nome


foo = Foo('Bar')
print(foo.nome)    