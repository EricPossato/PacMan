import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, assets):
        super().__init__()
        self.image = assets['player']
        self.rect = self.image.get_rect()
        self.rect.x = x*30
        self.rect.y = y*30

class Parede(pygame.sprite.Sprite):
    def __init__(self, x, y, assets):
        super().__init__()
        self.image = assets['parede']
        self.rect = self.image.get_rect()
        self.rect.x = x*30
        self.rect.y = y*30

