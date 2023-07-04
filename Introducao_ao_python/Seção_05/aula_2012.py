"""
@property - um getter no modo pythonico;

Criado: 04/07/2023 19:16

Author: Vitor Kruel
"""

# Código Cliente: Código que usa seu código


class Caneta:
    def __init__(self, cor) -> None:
        self.cor_tinta = cor

    def get_cor(self):
        print('GET COR')
        return self.cor_tinta


caneta = Caneta('Azul')

print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())

#########################################


class Caneta:
    def __init__(self, cor) -> None:
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 'QUALQUER COISA'

"""
É a forma pythonica de fazer:

    Quando precisamos alterar o nome de um atributo
    em uma aplicação, utilizamos o @property para
    conseguir alterar o nome do atributo mas não
    quebrar o código do cliente que ainda utiliza 
    o nome antigo do atributo.
"""
caneta = Caneta('Vermelho')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)