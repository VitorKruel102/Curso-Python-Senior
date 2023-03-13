# Imprecissão de ponto flutuante:
import decimal

numero_1 = decimal.Decimal(0.1) # Utilizamos para ter as casas precisas de um número decimal;
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2
print(numero_1)
print(numero_3)
print(f'{numero_3:.2f}') # type String
print(round(numero_3, 2)) # type float
