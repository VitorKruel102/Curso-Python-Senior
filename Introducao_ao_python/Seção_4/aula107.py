
def zipper(lista1, lista2):
    """."""
    intervalo = min(len(lista1), len(lista1))
    return [(lista1[i], lista2[i]) for i in range(intervalo)]

print(zipper(['1', '2', '3'], ['4', '5', '6', '7']))