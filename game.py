import pygame
from pygame.constants import VIDEOEXPOSE
from classe import *
import random
import time
from game_screen import game_screen


largura = 570
altura = 600
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Speed Menzinho')    

game_screen(window)