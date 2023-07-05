"""
@property + @setter - Getter e Setter no modo pythônico

Criado 04/07/2023 19:35

Author: Vitor Kruel
"""


class Caneta:
    def __init__(self, cor) -> None:
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor.')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


"""
Atributos que começam com um ou dois underlines 
não devem ser usados fora da classe:
Ex.:
    _cor
    __cor
"""

caneta = Caneta('Vermelha')
# setter -> Mandar o valor
caneta.cor = 'Pink'
caneta.cor_tampa = 'Azul'
# getter -> Obter valor
print(caneta.cor)
print(caneta.cor_tampa)

"""
Utilizamos o setter para conseguir restringir 
valores que o usuário mandar ou ajustar valores
para o formato desejado.

Propety: utilizado para não quebrar o código em
         possíveis alterações futuras.

Setter: Utilizado para modificar ou restringir o
        formato que o usuário enviou.

"""
