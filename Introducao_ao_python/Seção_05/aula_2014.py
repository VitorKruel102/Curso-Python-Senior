"""
Encapsulamento - Modificadores de Acesso (public, _protected, __private)

Criado: 05/07/2023 18:21

Author: Vitor Kruel
"""


class Foo:
    def __init__(self) -> None:
        self.public = 'É público!'
        self._protected = 'Isso é protegido!'
        self.__private = 'É privado!'

    def metodo_publico(self):
        print(self.__private)
        return 'metodo-publico'

    def _metodo_protected(self):
        return 'metodo-protegido'

    def __metodo_private(self):
        return 'metodo-privado'


"""
Public -> Pode ser usado dentro e fora da classe;
Protected -> Só deve ser usada na classe ou na subclass dela;
Private -> É só deve ser usada na classe.
"""

f = Foo()
print(f.public)
