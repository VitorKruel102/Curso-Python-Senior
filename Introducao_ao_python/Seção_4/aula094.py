# Try, except, else, finally
try: 
    print('Abrir arquivo')
    a = 8 / 0
except ZeroDivisionError:
    print('Dividiu por zero')
finally: # SEMPRE SERÁ EXECUTADO
    print('Fechar o arquivo')
