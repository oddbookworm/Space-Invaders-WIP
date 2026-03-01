import pygame
from os.path import join, dirname

class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()

        base_path = dirname(__file__)
        file_path = join(base_path, '..', 'graphics', f'{color}.png')

        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y)) # dies geht bis Zeile 8 im Tutorial

        if color == 'red': self.value = 100
        elif color == 'green': self.value = 200
        else: self.value = 300 

    def update(self, direction):
        self.rect.x += direction

class Extra(pygame.sprite.Sprite):
    def __init__(self, side, screen_width):
        super().__init__()

        base_path = dirname(__file__)
        file_path = join(base_path, '..', 'graphics', 'extra.png')
        self.image = pygame.image.load(file_path).convert_alpha()

        if side == 'right':
            x = screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3

        self.rect = self.image.get_rect(topleft=(x, 80))

    def update(self):
        self.rect.x += self.speed