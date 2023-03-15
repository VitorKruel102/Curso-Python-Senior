# Introdução ao try/except:

numero_str = input('Vou dobrar o número que você digitar: ')

while True:
    try:
        numero_float = float(numero_str)
        print(f'o dobro de {numero_str} é {(numero_float * 2):.2f}')
        break
    except:
        print('Isso não é um número')
