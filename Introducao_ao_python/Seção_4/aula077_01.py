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

dicionario_01 = {
    'c1': 1,
    'c2': 2,
}

dicionario_02 = dicionario_01.copy() # Cria uma cópia do dicionário

"""Precisamos ter ATENÇÃO, pois se conter listas dentro do dicionário,
e for realizado alterações desta lista dentro da copy, ela também será
alterada dentro do dicionário principal."""

perfil_vitoria = {
    'nome': 'Vitória',
    'sobrenome': 'Dias',
}

print(perfil_vitoria.get('nome')) # Retorna o valor, caso não exista a chave, retorna None;
print(perfil_vitoria.pop('nome')) # Retorna o valor, e exclue a chave;
print(perfil_vitoria.popitem())   # Retorna o valor da ultima chave, e exclue a chave;

perfil_vitoria.update({
    'nome': 'Vitória',
    'sobrenome': 'Dias',
    'idade': 21
})   # Retorna o valor da ultima chave, e exclue a chave;

perfil_vitoria.update(idade=22)

print(perfil_vitoria)
