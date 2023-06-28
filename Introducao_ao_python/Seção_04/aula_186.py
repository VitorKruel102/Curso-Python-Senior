"""
Criando arquivos com Python + Context Manager with

Criado: 28/06/2023 09:32

Autor: Vitor Kruel
"""

caminho_arquivo = r'D:\AREA_DE_TRABALHO_\Git_vitorkruel\Curso-Python-Senior\Introducao_ao_python\Seção_04\arquivo.txt'

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(['Linha 3\n', 'Linha 4\n'])

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())

with open(caminho_arquivo, 'a', encoding='utf-8') as arquivo:
    arquivo.write('Linha 5 Ação\n')
