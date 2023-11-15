import pygame
import sys
import yaml
from main_game.game import Local1vs1Game, LocalSoloGame
from utils import Button, get_font


# Open config file
with open('game/assets/utils/config.yml', 'r') as file:
    config = yaml.safe_load(file)


class Menu:
    '''superclass for Menu'''
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock, title: str) -> None:
        self.screen = screen
        self.clock = clock
        self.font = get_font(14)
        self.title = get_font(100).render(title, True, config['graphics']['title-color'])
        self.title_rect = self.title.get_rect(center=(450, 75))
        self.buttons = {}
        self.mouse_pos = pygame.mouse.get_pos()

    def loop_components(self) -> None:
        # Define variables
        self.mouse_pos = pygame.mouse.get_pos()

        # set permanent elements
        bg = pygame.image.load('game/assets/images/background.png').convert()
        self.screen.blit(bg, (0, 0))
        self.screen.blit(self.title, self.title_rect)

        # Update the buttons
        for key, button in self.buttons.items():
            if button.checkForInput(self.mouse_pos):
                button.changeColor(True)
            else: button.changeColor(False)
            button.update(self.screen)

        # Update the screen
        pygame.display.flip()

    def recurrent_events(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

class MainMenu(Menu):
    '''Menu object'''
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock) -> None:
        '''Initializes the menu object'''
        super().__init__(screen, clock, 'PONG')
        self.buttons['quit'] = Button(size=30, pos=(450, 450), text_input="QUIT")
        self.buttons['solo'] = Button(size=30, pos=(450, 250), text_input="SOLO")
        self.buttons['multi'] = Button(size=30, pos=(450, 350), text_input="MULTI")


    def main_loop(self) -> None:
        '''Main loop of the menu'''
        while True:
            super().loop_components()
            # Search for events
            for event in pygame.event.get():
                super().recurrent_events(event)
                # Detect if someone click on the button
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                    # Solo button
                    if self.buttons['solo'].checkForInput(self.mouse_pos):
                        SoloMenu(self.screen, self.clock).main_loop()
                    # Multi button
                    if self.buttons['multi'].checkForInput(self.mouse_pos):
                        MultiMenu(self.screen, self.clock).main_loop()
                    # Quit button
                    if self.buttons['quit'].checkForInput(self.mouse_pos):
                        pygame.quit()
                        sys.exit()


class SoloMenu(Menu):
    '''Menu for solo modes'''
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock) -> None:
        '''Init the menu'''
        super().__init__(screen, clock, 'SOLO')
        self.buttons['solo'] = Button(size=30, pos=(450, 250), text_input='SOLO')
        self.buttons['1vs1'] = Button(size=30, pos=(450, 350), text_input='1VS1')
        self.buttons['back'] = Button(size=30, pos=(450, 450), text_input='BACK')


    def main_loop(self) -> None:
        running = True
        while running:
            super().loop_components()
            # Search for events
            for event in pygame.event.get():
                super().recurrent_events(event)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                    if self.buttons['1vs1'].checkForInput(self.mouse_pos):
                        Local1vs1Game(self.screen, self.clock).main_loop()
                    if self.buttons['solo'].checkForInput(self.mouse_pos):
                        LocalSoloGame(self.screen, self.clock).main_loop()
                    if self.buttons['back'].checkForInput(self.mouse_pos):
                        running = False
                        break

class MultiMenu(Menu):
    '''Menu for multiplayers modes'''
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock) -> None:
        super().__init__(screen, clock, 'MULTI')
        self.buttons['create'] = Button(size=30, pos=(450, 250), text_input='CREATE')
        self.buttons['join'] = Button(size=30, pos=(450, 350), text_input='JOIN')
        self.buttons['back'] = Button(size=30, pos=(450, 450), text_input='BACK')

    def main_loop(self):
        running = True
        while running:
            super().loop_components()
            for event in pygame.event.get():
                super().recurrent_events(event)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                    if self.buttons['create'].checkForInput(self.mouse_pos):
                        pass
                    if self.buttons['join'].checkForInput(self.mouse_pos):
                        pass
                    if self.buttons['back'].checkForInput(self.mouse_pos):
                        running = False
                        break            
