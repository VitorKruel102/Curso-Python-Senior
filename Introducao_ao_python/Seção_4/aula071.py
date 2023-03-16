# args- Argumentos não nomeados


def soma(*args) -> int:
    """."""
    total = 0
    for numero in args:
        total += numero
    return total


print(soma(1, 2, 3, 4))