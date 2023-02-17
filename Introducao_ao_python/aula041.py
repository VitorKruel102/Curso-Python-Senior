string = 'Valor Qualquer'

i = 0
while i < len(string):
    letra = string[i]
    
    print(letra)
    i += 1
else:
    """Não é executado se o While for interrompido pelo Break."""
    print('O else foi executado')

