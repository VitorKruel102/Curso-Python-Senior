# Try, except, else, finally
try:
    a = 18
    b = 0
    c = a / b
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome não está definido')
print('FINALIZOU')