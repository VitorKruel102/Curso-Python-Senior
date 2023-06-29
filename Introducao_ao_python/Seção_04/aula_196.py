"""
Positional-Only Parameters(/) e Keyword-Only Arguments(*)

Criado: 29/06/2023 11:39

Autor: Vitor
"""
def soma(x, y, /, a, b): 
    """
    Os parametros antes da barra não podem ser nomeados, 
    precisam ser posicional e os parametros após a barra
    podem ser posicional ou nomeados.
        soma(1, 2, a=2. b=3)
        soma(1, 2, 2, b=3)
        soma(1, 2, 2, 3)
    """
    print(x + y, a + b)


def soma(x, y, *, a): 
    """
    Os parametros antes da * podem ser nomeados ou 
    ser posicional e os parametros após a * devem 
    ser nomeados.
        soma(1, 2, 2) # Errado
        soma(1, 2, a=2)
    """
    print(x + y + a)


def soma(x, y, /, *, a): 
    """
    Os parametros antes da barra não podem ser nomeados, 
    precisam ser posicional e os parametros após a * devem 
    ser nomeados.
        soma(1, 2, 2) # Errado
        soma(1, 2, a=2)
    """
    print(x + y + a)