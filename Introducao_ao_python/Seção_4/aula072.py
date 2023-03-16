# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplica(*args) -> int:
    """Realiza a multiplicação e retorna o valor total."""
    total = 1
    for numero in args:
        total *= numero
    return total


def par_impar(numero) -> str:
    """Retorna se o número é par ou impar."""
    return 'Par' if (numero % 2) == 0 else 'Impar'


multiplicao = multiplica(1, 2, 3, 4, 7)
print(multiplicao)
print(1 * 2 * 3 * 4 * 7)
print(par_impar(multiplicao))