# Argumento nomeado e não nomeado:
def soma(x, y):
    """."""
    print(f'{x=} + {y=} | x + y = {x + y}')


soma(1, 2) # Não nomeado
soma(y=2, x=1) # Nomeado
