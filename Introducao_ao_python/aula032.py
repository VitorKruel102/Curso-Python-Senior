# Exercicio 01: 
""" Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
number = input('Dígite um número inteiro: ')

if not number.isdigit():
    print('Você não digitou um número inteiro.')
else:
    number_int = int(number)
    is_even_number = number_int % 2 == 0

    if is_even_number:
        print('O número é par.')
    else:
        print('O número é impar.')
