# Raise - lança exceções (erros)
def is_not_zero(d):
    """."""
    if d == 0:
        raise ZeroDivisionError('Você mandou um zero')
    return True

def is_float_or_int(n):
    """."""
    tipo_n = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError(
            f'"{n}" deve ser int ou float.'
            f'"{tipo_n.__name__}" enviado'
        )
    return True

def divide(n, d):
    """Divide n por d."""
    is_float_or_int(n)
    is_float_or_int(d)
    is_not_zero(d)
    return n / d  

print(divide(8, 2))