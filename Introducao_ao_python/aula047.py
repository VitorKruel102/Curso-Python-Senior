"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os


PALAVRA_SECRETA = 'perfume'

quantidade_tentativas = 0
letras_acertadas = ''
while True:
    letra_digitada = input('Digite uma letra: ').lower()

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        quantidade_tentativas += 1
        continue
    
    if letra_digitada in PALAVRA_SECRETA:
        letras_acertadas += letra_digitada
    
    palavra_descoberta = ''
    for letra in PALAVRA_SECRETA:
        if letra in letras_acertadas:
            palavra_descoberta += letra
        else:
            palavra_descoberta += '*'   
    
    if palavra_descoberta == PALAVRA_SECRETA:
        os.system('cls')
        print('VOCÊ GANHO O JOGO')
        print(f'Palavra formada {palavra_descoberta}')
        print(f'Número de tantativas: {quantidade_tentativas}')
    else:
        print(f'Palavra formada {palavra_descoberta}')

    quantidade_tentativas += 1
