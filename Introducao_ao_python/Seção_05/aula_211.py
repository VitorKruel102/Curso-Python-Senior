"""
Method VS @classmethod VS @staticmethod

Criado: 04/07/2023 18:18

Author: Vitor Kruel
"""


class Connection:
    def __init__(self, host='localhost') -> None:
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):  # self, Médodo de Instância
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_user_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print(f'LOG: {msg}')


c1 = Connection()
print(c1.user)
print(c1.password)
c1.set_user('VitorKruel')
c1.set_password('1231683213')
print(c1.user)
print(c1.password)


c2 = Connection.create_user_auth('Vitor', '51615431')
print(c2.user)
print(c2.password)
