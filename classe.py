import pygame


class Parede(pygame.sprite.Sprite):
    def __init__(self, x, y, assets):
        super().__init__()
        self.image = assets['parede_img']
        self.rect = self.image.get_rect()
        self.rect.x = x*20
        self.rect.y = y*20