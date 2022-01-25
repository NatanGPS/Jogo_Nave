import pygame

class Nave():

    def __init__(self, ai_settings, screen):
        """Inicia a nave e define sua posição"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da nave e le seu rect
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # cetraliza a nave 
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # guarda um valor decimal do cetro da nave
        self.center = float(self.rect.centerx)
        
        # Move as flags
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Atualiza a posição da nave de acordo com as flags"""
        # Atualiza a nave
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # Atualiza o obejto rect no  self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Desenha a nave de acordo com sua posição"""
        self.screen.blit(self.image, self.rect)