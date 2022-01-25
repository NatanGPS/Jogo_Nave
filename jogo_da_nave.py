import pygame
from pygame.sprite import Group

from configuracoes import Configuracoes
from nave import Nave
import game_fuctions as gf

def run_game():
    # inicia o pygame
    pygame.init()
    ai_settings = Configuracoes()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # muda cor de fundo.
    bg_color = (230, 230, 230)
    
    # cria uma nave
    ship = Nave(ai_settings, screen)
    # cria um ggrupo pra colocar balas dentro
    bullets = Group()

    # loop principal
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()