# Yield from
def generator_one():
    yield 1
    yield 2
    yield 3

def genetator_two():
    yield from generator_one()
    yield 2
    yield 3
    yield 6

g = genetator_two()
for numero in g:
    print(numero)