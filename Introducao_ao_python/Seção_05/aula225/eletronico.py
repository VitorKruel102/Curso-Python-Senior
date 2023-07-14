from log import LogPrintMixin, LogFileMixin


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        """Liga o aparelho eletrônico."""
        if not self._ligado:
            self._ligado = True
            
    def desligar(self):
        """Desliga o aparelho eletrônico."""
        if self._ligado:
            self._ligado = False


class Smartphone(Eletronico, LogFileMixin):    
    def ligar(self):
        """Liga o smartphone."""
        super().ligar()

        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)

    def desligar(self):
        """Desliga o smartphone."""
        super().desligar()

        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_success(msg)
