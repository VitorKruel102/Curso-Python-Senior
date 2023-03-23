# Métodos úteis no dicionário:
perfil_vitor = {
    'nome': 'Vitor',
    'sobrenome': 'Kruel',
}

perfil_vitor.setdefault('idade', 0) # Coloca valores padrões, caso não exista a chave

print(perfil_vitor.__len__()) # Quantas chaves tem no dicionário
print(len(perfil_vitor))      # Quantas chaves tem no dicionário
print(perfil_vitor.keys())    # Retorna uma lista com as chaves
print(perfil_vitor.values())  # Retorna uma lista com os valoes
print(perfil_vitor.items())   # Retorna uma lista com chaves e valores


for chave in perfil_vitor:
    print(chave)
