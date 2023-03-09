# Enumerate - enumera iteráveis(indices)
lista = ['Vitor', 'Vitoria', 'Vania']
for index, nome in enumerate(lista):
    print(index, nome)

for index, nome in enumerate(lista, start=10):
    print(index, nome)
 