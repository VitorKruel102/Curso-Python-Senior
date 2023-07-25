"""
Polimorfirsmo

Criado: 25/07/2023 12:45

Autor: Vitor Kruel
"""

 
# ASSINATURA DO MÉTODO = Nome, Parâmetros e Retorno iguais.


from abc import ABC, abstractmethod


class Notificacao(ABC):


    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        pass


class NotificacaoEmail(Notificacao):


    def enviar(self):
        print(f'E-mail: enviando - {self.mensagem}')
        return True


class NotificacaoSMS(Notificacao):


    def enviar(self):
        print(f'SMS: enviando - {self.mensagem}')
        return True


# foo = NotificacaoEmail('Testando notificação')
# foo.enviar()


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação envida')
    else:
        print('Notificação NÃO enviada')


notificar(NotificacaoEmail('Testando e-mail'))
notificar(NotificacaoSMS('Testando sms'))