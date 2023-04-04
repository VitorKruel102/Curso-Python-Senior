# Dictionary Comprehesion
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
}
print(produto.items())

dicionario = {
    chave: valor 
    if isinstance(valor, (float, int)) else valor.upper()
    for chave, valor in produto.items()
}
print(dicionario)