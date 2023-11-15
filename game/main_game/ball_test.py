import pygame
import random
import yaml
import vector


# Open config file
with open('game/assets/utils/config.yml', 'r') as file:
    config = yaml.safe_load(file)


class Ball:
    '''Ball object'''
    def __init__(self, x: int, y: int, size: tuple[int, int]) -> None:
        '''Initializes the ball object'''
        # Init variables
        self.x = x
        self.y = y
        self.size = size
        self.max = config['ball-speed']['max']
        self.min = config['ball-speed']['min']
        self.vector = vector.random_vector()
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])


    def detect_players_collisions(self, players_rect: tuple[pygame.Rect, pygame.Rect]) -> None:
        '''detect players collisions and change ball direction to make it bounce'''
        # detect hitbox collision
        # player 1 (Left side) :
        if self.rect.colliderect(players_rect[0]):
            self.vector[0] = random.randint(self.min, self.max)
        # player 2 (Right side)
        if self.rect.colliderect(players_rect[1]):
            self.vector[0] = random.randint(self.max*-1, self.min*-1)


    def move(self, speed: int, players_rect: tuple[pygame.Rect, pygame.Rect]) -> None:
        '''Moves the ball'''
        # Detect collision with up and down walls
        if self.y < 0 or self.y+self.rect.size[1] > 500:
            self.vector[1] = -self.vector[1]

        # Detect collision with left and right walls
        if self.x < 0:
            return 'player1'
        if self.x > 900:
            return 'player2'
        
        # Detect collision with the players
        self.detect_players_collisions(players_rect)

        # Move the ball
        self.x += self.vector[0] * speed
        self.y += self.vector[1] * speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, area: pygame.Surface) -> None:
        """Draws the ball"""
        pygame.draw.rect(area, config['graphics']['ball-color'], self.rect)