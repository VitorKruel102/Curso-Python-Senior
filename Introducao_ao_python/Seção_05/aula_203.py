"""
Mantendo estados dentro da classe

Criado: 01/07/2023 18:11

Autor: Vitor Kruel
"""
class Camera:
    def __init__(self, nome, filmando=False) -> None:
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        """."""
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True


    def parar_filmar(self):
        """."""
        if not self.filmando:
            print(f'{self.nome} Não está está filmando...')
            return
        
        print(f'{self.nome} está parando de filmando...')
        self.filmando = False


    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando...')
            return         
        
        print(f'{self.nome} está fotografando...')


primeira_camera = Camera('Canon')
segunda_camera = Camera('Sony')

primeira_camera.filmar()
primeira_camera.filmar()
primeira_camera.fotografar()
primeira_camera.parar_filmar()
primeira_camera.fotografar()
