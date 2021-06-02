import pygame
from pygame.constants import VIDEOEXPOSE
from classe import *
import random

pygame.init()

all_sprites = pygame.sprite.Group()
all_paredes = pygame.sprite.Group()
all_pontos = pygame.sprite.Group()
clock = pygame.time.Clock()
FPS = 30

largura = 570
altura = 600
diametro = 5

white = (255, 255, 255)
black = (0, 0, 0)

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Pac Menzinho')
assets = {}


assets['player_img'] = pygame.image.load('sprites/pp.png').convert_alpha()
assets['player_img'] = pygame.transform.scale(assets['player_img'], (20, 20))

andando = []
for i in range(1,7):
    filename = 'sprites/personagem/walk{}.png'.format(i)
    img = pygame.image.load(filename).convert_alpha()
    img = pygame.transform.scale(img, (20, 20))
    andando.append(img)
assets["player_img"] = andando

player = Player(assets['player_img'])
all_sprites.add(player)
assets['parede'] = pygame.image.load('sprites/Parede.png').convert_alpha()
assets['parede'] = pygame.transform.scale(assets['parede'], (29, 29))

assets['ponto'] = pygame.image.load('sprites/juul.png').convert_alpha()
assets['ponto'] = pygame.transform.scale(assets['ponto'], (30, 30))


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

while len(all_pontos) < 3:
    pontox = random.randint(0,18)
    pontoy = random.randint(0,19)
    if matriz_paredes[pontoy][pontox] == 1:
        ponto = Pontos(pontoy,pontox, assets)
        all_pontos.add(ponto)
        all_sprites.add(ponto)
  

continua = True
while continua:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continua = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continua = False
            if event.key == pygame.K_DOWN:
                player.speedx = 0
                player.speedy = 2
            if event.key == pygame.K_UP:
                player.speedx = 0
                player.speedy = -2
            if event.key == pygame.K_LEFT:
                player.speedx = -2
                player.speedy = 0
            if event.key == pygame.K_RIGHT:
                player.speedx = 2
                player.speedy = 0

    while len(all_pontos) < 3:
        pontox = random.randint(0,18)
        pontoy = random.randint(0,19)
        if matriz_paredes[pontoy][pontox] == 1:
            ponto = Pontos(pontoy,pontox, assets)
            pygame.sprite.spritecollide(ponto,all_pontos,True)
            all_pontos.add(ponto)
            all_sprites.add(ponto)

    all_sprites.update()
    
    colisao = pygame.sprite.spritecollide(player,all_paredes,False)
    if len(colisao) > 0:
        player.speedx = 0
        player.speedy = 0
        print('COLIDIU')

    coletar = pygame.sprite.spritecollide(player,all_pontos,True)

    window.fill((0, 0, 0))
    all_sprites.draw(window)

    pygame.display.update()

pygame.quit()