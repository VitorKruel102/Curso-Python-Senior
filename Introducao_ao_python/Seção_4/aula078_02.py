conjunto = set({1, 2, 3, 4})
print(conjunto)


conjunto.clear()
print(conjunto)

conjunto.add(5)
print(conjunto)

conjunto.update((5, 6, 7))
print(conjunto)

conjunto.discard(5) # Descarta um valor que estiver dentro do set
print(conjunto)
