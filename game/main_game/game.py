import pygame
import sys
import yaml
from main_game.player import Player
from main_game.ball import Ball
from utils import get_font
import random
import main_game.key_tables as key_tables


# Open config file
with open('game/assets/utils/config.yml', 'r') as file:
    config = yaml.safe_load(file)


class LocalGame:
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock) -> None:
        # Init screen
        self.screen = screen
        pygame.display.set_caption("Pong")
        self.rect = pygame.Rect(0, 0, 900, 500)

        # Init players
        self.player1 = Player(20, 250, (20, 80), key_tables.PLAYER_ONE)
        self.player2 = Player(860, 250, (20, 80), key_tables.PLAYER_TWO)
        self.speed = config['players-speed']
        self.player1_speed = 0
        self.player2_speed = 0

        # Init ball
        self.ball = Ball(450, 250, (10, 10), random.choice([[-1, 1], [1, -1]]))
        self.ball_speed = 4
        self.game_starting = False

        # Init variables
        self.game_running = True
        self.clock = clock


    def loop_component(self):
        # Search for recurrents events
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Wait for user to press space in order to start the game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.game_starting = True

        # Update the screen
        bg = pygame.image.load('game/assets/images/background.png').convert()
        self.screen.blit(bg, (0, 0))

        # Update players position
        self.player1.move()
        self.player2.move()
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)

        # Update ball position
        if self.game_starting:
            result = self.ball.move(self.ball_speed, (self.player1.rect, self.player2.rect))
            if result == 'player1':
                self.game_running = False
            if result == 'player2':
                self.game_running = False
        else:
            txt = get_font(14).render('Press SPACE to start', True, config['graphics']['title-color'])
            txt_rect = txt.get_rect(center=(450, 75))
            self.screen.blit(txt, txt_rect)
        self.ball.draw(self.screen)

        # Update screen and set frame per second
        pygame.display.flip()
        self.clock.tick(60)


class Local1vs1Game(LocalGame):
    '''Main class for the game'''
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock) -> None:
        '''Initializes the game object'''
        super().__init__(screen, clock)


    def main_loop(self) -> None:
        '''Executes the main loop of the game'''
        while self.game_running:
            super().loop_component()
            # get keys pressed
            keys = pygame.key.get_pressed()

            # get players moves
            # player 2
            self.player2.get_directions()
            # player 1
            self.player1.get_directions()


class LocalSoloGame(LocalGame):
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock) -> None:
        '''init subclass for solo pong in local'''
        super().__init__(screen, clock)

    def main_loop(self) -> None:
        '''Execute game main loop'''
        while self.game_running:
            super().loop_component()
            # get key pressed
            keys = pygame.key.get_pressed()

            # get player move
            if keys[pygame.K_UP]:
                self.player2_speed = -self.speed
                self.player1_speed = -self.speed
            elif keys[pygame.K_DOWN]:
                self.player2_speed = self.speed
                self.player1_speed = self.speed
            else:
                self.player2_speed = 0
                self.player1_speed = 0
