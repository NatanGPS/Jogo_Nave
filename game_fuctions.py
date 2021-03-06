import sys

import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responde ao pressionamento de teclas"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
def check_keyup_events(event, ship):
    """Responde a soltura de teclas."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Responde ao pressionamento de teclas e mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def fire_bullet(ai_settings, screen, ship, bullets):
    """dispara uma bala, se o limite permitir."""
    # cria uma bala e adiciona no grupo.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(ai_settings, screen, ship, bullets):
    """atualiza as imagens na tela"""
    # redesenha a tela a cada passo no loop.
    screen.fill(ai_settings.bg_color)
    
    # reedesenha as balas.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # faz a mais atualizada informação aparrecer na tela.
    pygame.display.flip()
    
def update_bullets(bullets):
    """atualiza as posições de novas balas e de velhas."""
    bullets.update()

    # garente que as balas vao sumir
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)