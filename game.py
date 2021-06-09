import pygame
from classe import *
import random
import time
from game_screen import game_screen
from start_screen import start_screen


largura = 570
altura = 600
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Speed Menzinho')    

start_screen(window)