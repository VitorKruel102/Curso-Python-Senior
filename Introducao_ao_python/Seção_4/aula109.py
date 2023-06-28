"""
Combinations, Permutations e Product - Itertools

Combinations: Ordem não importa
Permutations: Ordem Importa
Product: Ordem Importa e repete valores únicos
"""

from itertools import combinations
from itertools import permutations
from itertools import product

def print_iter(iterator):
    """."""
    print(*list(iterator), sep='\n')
    print()



pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['Preta', 'Branca'], 
    ['P', 'M', 'G'], 
    ['Masculino', 'Feminino']
]




print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
