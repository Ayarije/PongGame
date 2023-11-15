import pygame
import yaml
import vector


# Open config file
with open('game/assets/utils/config.yml', 'r') as file:
    config = yaml.safe_load(file)


class Player:
    '''Player object'''
    def __init__(self, x: int, y: int, size: tuple[int, int], key_table: dict) -> None:
        '''Initializes the player object'''
        # Init variables
        self.x = x
        self.y = y
        self.size = size
        self.vector = vector.Vector(0, 0)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.key_table = key_table

    def get_directions(self):
        keys = pygame.key.get_pressed()

        if keys[self.key_table['up']]:
            self.vector = vector.Vector(0, -1)
        else:
            self.vector = vector.Vector(0, 0)
        if keys[self.key_table['down']]:
            self.vector = vector.Vector(0, 1)
        else:
            self.vector = vector.Vector(0, 0)
        

    def move(self) -> None:
        '''Moves the player'''
        vec = self.vector * config['players-speed']
        self.rect = vec.apply(self.rect)

    def draw(self, area) -> None:
        """Draws the player"""
        pygame.draw.rect(area, config['graphics']['players-color'], self.rect)
