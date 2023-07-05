"""
Agregação de classes

Criado: 05/07/2023 19:51

Author: Vitor Kruel
"""


class Carrinho:
    def __init__(self) -> None:
        self._produtos = []
    
    def preco_total(self):
        return sum([produto.preco for produto in self._produtos])

    def inserir_produtos(self, *produtos):
        self._produtos += produtos
            
    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()

p1, p2 = Produto('Caneta', 1.2), Produto('Camiseta', 20)

carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.preco_total())