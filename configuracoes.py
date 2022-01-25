class Confirguracoes():
    """Aqui fica todas as configurações do jogo"""

    def __init__(self):
        """inicia as configurações"""
        # setting da tela.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # settings da nave.
        self.ship_speed_factor = 1.5

        # settings da bala.
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3