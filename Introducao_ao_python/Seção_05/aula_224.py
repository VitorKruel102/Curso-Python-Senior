"""
Herança Múltipla.

Criado: 14/07/2023 09:42

Autho: Vitor Kruel
"""
class A:
    ...
    def quem_sou(self):
        """."""
        print('A')


class B(A):
    ...
    # def quem_sou(self):
    #     """."""
    #     print('B')


class C(A):
    ...
    def quem_sou(self):
        """."""
        print('C')


class D(B, C):
    ...
    # def quem_sou(self):
    #     """."""
    #     print('D')


d = D()
d.quem_sou()
# print(D.__mro__)
print(D.mro())

"""
Quando temos mais de uma herança, ele vai seguir a 
order colocada. Buscará primeiro na Classe D, depois 
na Classe B, depois na Classe C e por fim na Classe A.

Seguindo a heranças de todas as classe tando das classe
que o D herda(B, C) quanto as classes que B e C herdam(A) 
"""