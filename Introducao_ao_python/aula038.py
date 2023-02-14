QUANTIDADE_LINHAS = 5 # Constante
QUANTIDADE_COLUNAS = 5 # Constante

linha = 1
while linha <= QUANTIDADE_LINHAS:
    coluna = 1
    while coluna <= QUANTIDADE_COLUNAS:
        print(f'{linha=}, {coluna=}')
        coluna += 1 
    linha += 1

print('Acabou!')
