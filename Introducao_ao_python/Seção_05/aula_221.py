"""
Sobreposição de métodos.

Criado: 12/07/2023 10:40

Autor: Vitor Kruel
"""

"""
Quando queremos editar um método de uma Class Principal 
mas não queremos perder a funcionalidade principal
podemos utilizar super() para retornar o método 
original da Classe Principal

A.mro() --> Retorna uma lista dos 'Method resolution order'
"""


class MinhaString(str):
    def upper(self):
        print('CHAMOU UPPER:')
        return super().upper()


string = MinhaString('Luiz')
print(string)
print(string.upper())
print('-' * 80)


class A:
    atributo_a = 'Valor_A'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'Valor_B'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        """Se a classe Pai tem o método __init__,
        e preciso criar nesta classe o mesmo método,
        vou precisar colocar o super().__init__() 
        para enviar os atributos necessário para a 
        classe Pai para evitar erros;
        """
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'Valor_C'

    def metodo(self):
        super(B, self).metodo() # Pega o método da Classe Pai do B
        super(C, self).metodo() # Pega o método da Classe Pai do C
        print('C')


classe_c = C('Valor', 'Qualquer')
print(classe_c.atributo)
print(classe_c.outra_coisa)
print('-' * 80)
print(classe_c.atributo_a)
print(classe_c.atributo_b)
print(classe_c.atributo_c)
print('-' * 80)

classe_c.metodo()
