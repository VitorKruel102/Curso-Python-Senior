# Interando strings com while

nome_completo = 'Vitor Kruel da Silva'
tamanho_nome = len(nome_completo)
nova_string = ''

indice = 0
while indice < tamanho_nome:
    nova_string += f'*{nome_completo[indice]}'
    indice += 1

print(nova_string)