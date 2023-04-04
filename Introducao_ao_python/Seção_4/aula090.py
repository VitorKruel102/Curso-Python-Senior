import sys
# Gerator expression, Iterables, Iterators:
iterable = ['Eu', 'tenho', '__iter__']
itarator = iter(iterable) # Permite utilizar o next()

print(next(itarator))
print(next(itarator))
print(next(itarator))


generator = (n for n in range(100000000000000)) 
"""
Genetator Expression, entraga um valor por vez,
não pesa na memória.
"""
print(sys.getsizeof(generator))