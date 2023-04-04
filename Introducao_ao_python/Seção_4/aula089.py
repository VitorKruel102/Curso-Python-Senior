# Dir, hasattr e getattr:
string = 'Vitor'

print(dir(string)) # Nomes definidos em string
print(hasattr(string, 'upper')) # Analise se existe o método upper em string
print(getattr(string, 'upper')())
