import pygame
from pygame.locals import *
from random import randint

SCREEN_W = 1280
SCREEN_H = 600

BLACK = pygame.Color(0,0,0)
RED = pygame.Color(255,0,0)
WHITE = pygame.Color(255,255,255)
GREEN = pygame.Color(0,255,0)
BLUE = pygame.Color(0,0,255)
PURPLE = pygame.Color(255, 0, 255)
YELLOW = pygame.Color(255, 255, 0)
TEAL = pygame.Color(0,255,255)

def randColor():
    return pygame.Color(randint(0,255),randint(0,255),randint(0,255))
