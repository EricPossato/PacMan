import pygame
largura = 560
altura = 590
class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura / 2
        self.speedx = 0
        self.speedy = 0
    def update (self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Parede(pygame.sprite.Sprite):
    def __init__(self, x, y, assets):
        super().__init__()
        self.image = assets['parede']
        self.rect = self.image.get_rect()
        self.rect.x = x*30
        self.rect.y = y*30

