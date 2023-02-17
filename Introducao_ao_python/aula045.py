"""
Iterável -> str, range, etc (Precisa ter o método __iter__)
Iterador -> Quem sabe entregar um valor por vez
next -> me entrega o próximo valor
iter -> me entrega o seu iterador
"""
texto = iter('Vitor') # __iter__
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

segundo_texto = 'Outro'
iterador = iter(segundo_texto)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
