frase = 'O python é uma linguagem de programação' \
    'multiparadigma.' \
    'Foi criado por Guino Van Rossum.' 

i = 0
quantidade_repetida = 0
letra_repetidas_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue

    numero_repeticao_da_letra_atual_na_frase = frase.count(letra_atual)    

    if quantidade_repetida < numero_repeticao_da_letra_atual_na_frase:
        quantidade_repetida = numero_repeticao_da_letra_atual_na_frase
        letra_repetidas_mais_vezes = letra_atual
    
    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_repetidas_mais_vezes}" '
    f'que apareceu {quantidade_repetida}x')