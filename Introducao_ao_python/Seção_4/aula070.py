# Retorno  de valores das funções:


def soma(x, y) -> int:
    """Realiza a soma de dois números inteiros 
    se x <= 10 se não retorna o número 10.
    """
    if x > 10:
        return 10
    return x + y


soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)
