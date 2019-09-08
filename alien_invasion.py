import pygame
from settings import Settings
from ship import Ship
import game_fuctions as gf


def run_game():
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("s41_blizzard invasion")
    ship = Ship(screen)
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)
        ship.update()


run_game()
