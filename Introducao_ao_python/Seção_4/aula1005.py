def decorador(func):
    """."""
    def aninhada(*args, **kwargs):
        print('A soma é:')
        return func(*args, **kwargs)
    return aninhada


@decorador
def soma(x, y):
    """."""
    return (x + y)


print(soma(10, 5))