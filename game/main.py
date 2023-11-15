import pygame
from menu import MainMenu


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((900, 500))
    clock = pygame.time.Clock()
    MainMenu(screen, clock).main_loop()
    pygame.quit()
