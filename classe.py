import pygame
largura = 560
altura = 590
class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.andando = img
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.andando[self.frame]
        self.rect = self.image.get_rect()
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 120

        #self.image = img
        #self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura / 2
        self.speedx = 0
        self.speedy = 0
    def update (self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.andando):
                self.frame = 0
            else:
                x = self.rect.x
                y = self.rect.y
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                self.image = self.andando[self.frame]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y


        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Parede(pygame.sprite.Sprite):
    def __init__(self, x, y, assets):
        super().__init__()
        self.image = assets['parede']
        self.rect = self.image.get_rect()
        self.rect.x = x*30
        self.rect.y = y*30

class Pontos(pygame.sprite.Sprite):
    def __init__(self, x, y, assets):
        super().__init__()
        self.image = assets['juul']
        self.rect = self.image.get_rect()
        self.rect.x = x *20
        self.rect.y = y* 20