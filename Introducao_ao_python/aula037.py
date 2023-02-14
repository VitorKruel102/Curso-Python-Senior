# Repetição
contator = 0

while contator <= 100:
    contator += 1
    
    if contator == 6:
        print(f'Não vou mostrar o {contator}')
        continue

    if contator >= 10 and contator <= 27:
        print(f'Não vou mostrar o {contator}')
        continue

    print(contator)

    if contator == 40:
        break
    
print('Acabou!')