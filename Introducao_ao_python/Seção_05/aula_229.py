"""
Classe Abstratas = Abstract Base Class (abc)

Criado: 17/07/2023 16:28

Author: Vitor Kruel
"""

"""
Classe Abstratas = Abstract Base Class (abc)

Ela á utilizadas para definir novas classes, 
podem forçar outra classe a criarem métodos 
concretos e também podem ter métodos concretos 
por elas mesmas.

Método abstrato = Forçar que utilizem subclasse 
para utilizar esse método.

Método concreto = São métodos que fazem coisas.

Classes Abstratas NÃO DEVEM ser instânciadas diretamente.
"""
from abc import ABC, abstractmethod


class Log(ABC): # Classe Abstrata
    """Para tornar uma classe 100% abstrata, precisamos herdar a class ABC e 
    utilizar pelo menos um método abstrato. Com isso, ninguém conseguirá 
    acessar a classe Abstrata."""
    
    @abstractmethod # Método abstrato
    def _log(self, mensagem): ...
    
    def log_error(self, mensagem): # Método Concreto
        """."""
        return self._log(f'Error: {mensagem}')
    
    def log_success(self, mensagem): # Método Concreto
        """."""
        return self._log(f'Success: {mensagem}')


class LogPrintMixin(Log):
     def _log(self, mensagem):
        """."""
        print(f'{mensagem} ({self.__class__.__name__})')


objeto = LogPrintMixin()
objeto.log_error('teste')