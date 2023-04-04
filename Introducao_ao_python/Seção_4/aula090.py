import sys
# Gerator expression, Iterables, Iterators:
iterable = ['Eu', 'tenho', '__iter__']
itarator = iter(iterable) # Permite utilizar o next()

print(next(itarator))
print(next(itarator))
print(next(itarator))


generator = (n for n in range(100000000000000)) 
"""
Generator Expression, entraga um valor por vez,
não pesa na memória, só entrega o valor e não
sabe o tamanho e nem index.
"""
print(sys.getsizeof(generator))