"""
Decoradores:
---> Adicionar / Remover / Restringir / Alterar

"""
def criar_funcao(func):
    """."""
    def interna(*args, **kwargs):
        """."""
        for arg in args:
            is_string(arg)

        return func(*args, **kwargs)
    return interna

  
def is_string(param):
    """."""
    if not isinstance(param, str):
        raise TypeError('Deve ser uma string')


@criar_funcao
def inverte_string(string):
    return string[::-1]


print(inverte_string('123'))