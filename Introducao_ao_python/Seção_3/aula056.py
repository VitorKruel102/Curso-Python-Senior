"""
Com Lista e String:
    split - Divide uma string
    join - une uma string

strip() - Corta os espaços em branco no inicio e no fim;
rstrip() - Corta os espaços em branco na direita
lstrip() - Corta os espaços em branco na esquerda
"""
frase = ' Olha só que , coisa interessante.'
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())
    
print(lista_frases_cruas)
print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
