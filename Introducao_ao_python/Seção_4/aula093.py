# Try, except, else, finally
try:
    a = 18
    b = 0
    c = a / b
except ZeroDivisionError as error:
    print('Dividiu por zero.', error.__class__.__name__, sep=' --> ')
except NameError:
    print('Nome não está definido')

print('FINALIZOU')