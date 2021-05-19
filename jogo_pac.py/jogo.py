import pygame
from pygame.constants import VIDEOEXPOSE

pygame.init()

largura = 500
altura = 400
diametro = 5

white = (255, 255, 255)
black = (0, 0, 0)

window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Exemplo 3')

centro = pygame.Vector2(largura / 2, altura / 2)
vx = 0
vy = 0
v = pygame.Vector2(vx, vy)



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
                vy = 0.005
            if event.key == pygame.K_UP:
                vx = 0
                vy = 0.005
            if event.key == pygame.K_LEFT:
                vx = -0.005
                vy = 0
            if event.key == pygame.K_RIGHT:
                vx = 0.005
                vy = 0
    pos = pos + v

    # Para que serve os vetores?
    window.fill((0, 0, 0))
    
    
    pygame.draw.circle(window, white, pos, diametro)
    pygame.display.update()

pygame.quit()