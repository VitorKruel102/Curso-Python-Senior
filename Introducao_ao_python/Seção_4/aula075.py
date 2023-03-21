"""Exercício:
Crie funções que duplicam, triplicam e quadriplicam o número
recebido como parâmetro.
"""
def criar_multiplicador(multiplicador):
    """Cria multiplicadores."""
    def multiplicar(numero):
        """Mostra resultado da multiplicação."""
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))

