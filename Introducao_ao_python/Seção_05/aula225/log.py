# Abstração 
class Log:
    def _log(self, mensagem):
        """."""
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, mensagem):
        """."""
        return self._log(f'Error: {mensagem}')
    
    def log_success(self, mensagem):
        """."""
        return self._log(f'Success: {mensagem}')


class LogFileMixin(Log):
    def _log(self, mensagem):
        """."""
        print(mensagem)


class LogPrintMixin(Log):
     def _log(self, mensagem):
        """."""
        print(f'{mensagem} ({self.__class__.__name__})')

 
if __name__ == '__main__':
    objeto = LogFileMixin()
    objeto.log_error('mensagem')

    objeto = LogPrintMixin()
    objeto.log_error('qualquer coisa')
    objeto.log_success('qualquer coisa')