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

# Exercicio 02: 
"""Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. 
Ex:
    Bom dia (0-11) <---> Boa tarde (12-17) <---> Boa noite (18-23)
"""
current_time = input('Digite a hora atual do seu dia: ')

if not current_time.isdigit():
    print('Você não digitou a hora corretamente.')
else:
    current_time_int = int(current_time)
    is_morning = current_time_int <= 11 
    is_afternoon = current_time_int >= 12 and current_time_int < 18

    if is_morning:
        print('Bom dia!')
    elif is_afternoon:
        print('Boa tarde!')
    else:
        print('Boa noite!')

# Exercicio 03: 
"""Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
first_name = input('Digite seu primeiro nome: ')
has_number = any(char.isdigit() for char in first_name)

if has_number:
    print('Você digitou o nome corretamente.')
else:
    is_shot_name = len(first_name) < 5 
    is_normal_name = is_shot_name == False and len(first_name) <= 6
    
    if is_shot_name: 
        print('Seu nome é curto.')
    elif is_normal_name:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')
        