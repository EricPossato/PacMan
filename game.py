import pygame
from classe import *
import random
import time
from game_screen import game_screen
from start_screen import start_screen
from game_over import game_over


largura = 570
altura = 600
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Speed Menzinho')    

state = 1

while state != 0:
    if state == 1:
        state = start_screen(window)
    elif state == 2:
        state = game_screen(window)
    elif state == 3:
        state = game_over(window)
    