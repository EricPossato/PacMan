import pygame
from pygame.constants import VIDEOEXPOSE
from classe import *

pygame.init()

all_sprites = pygame.sprite.Group()
all_paredes = pygame.sprite.Group()



largura = 560
altura = 590
diametro = 5

white = (255, 255, 255)
black = (0, 0, 0)

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Pac Menzinho')
assets = {}


player = pygame.image.load('sprites/PacMan.png').convert()
player = pygame.transform.scale(player, (29, 29))

assets['player'] = player
assets['parede'] = pygame.image.load('sprites/Parede.png').convert()



centro = pygame.Vector2(largura / 2, altura / 2)
vx = 0
vy = 0
v = pygame.Vector2(vx, vy)

matriz_paredes =[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


i = 0 
while i < len(matriz_paredes):
    j=0
    while j < len(matriz_paredes[i]):
        if matriz_paredes[i][j] == 0:
            p = Parede(i, j, assets)
            all_paredes.add(p)
            all_sprites.add(p)
        j+=1
    i+=1

pos = centro  



continua = True
while continua:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continua = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continua = False
            if event.key == pygame.K_DOWN:
                vx = 0
                vy = 0.05
            if event.key == pygame.K_UP:
                vx = 0
                vy = -0.05
            if event.key == pygame.K_LEFT:
                vx = -0.05
                vy = 0
            if event.key == pygame.K_RIGHT:
                vx = 0.05
                vy = 0

    v = pygame.Vector2(vx, vy)
    all_sprites.update()
    
    pos = pos + v
    
    colisao = pygame.sprite.spritecollide(player,all_paredes,True)
    if len(colisao) > 0:
        

    window.fill((0, 0, 0))
    
    
    window.blit(player, (pos))
    all_sprites.draw(window)

    pygame.display.update()

pygame.quit()