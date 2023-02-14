# Interando strings com while

nome_completo = 'Vitor Kruel da Silva'
tamanho_nome = len(nome_completo)
nova_string = ''

contador = 0
while contador < tamanho_nome:
    nova_string += f'*{nome_completo[contador]}'
    contador += 1

print(nova_string)