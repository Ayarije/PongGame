import pygame
import yaml


with open('game/assets/utils/config.yml', 'r') as file:
    config = yaml.safe_load(file)


class Button:
    '''Button object'''
    def __init__(self, pos, text_input, size) -> None:
        '''Initializes the button object'''
        # Variables
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = get_font(size)
        self.base_color = config['graphics']['buttons-color']['normal']
        self.hovering_color = config['graphics']['buttons-color']['hovering']
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
    
    def update(self, screen: pygame.Surface) -> None:
        """Updates the button object on screen"""
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position: tuple[int, int]) -> bool:
        """Checks if the button is in the position"""
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False
    def changeColor(self, is_mouse_on_it: bool) -> None:
        """Changes the color of the button when mouse is on it"""
        if is_mouse_on_it:
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)


def get_font(size):
    return pygame.font.Font('game/assets/font.ttf', size)