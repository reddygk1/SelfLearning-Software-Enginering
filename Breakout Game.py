"""
 Sample Breakout Game

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""

# --- Import libraries used for this program
bif = "bg.jpg"

import sys
import pygame
from pygame.locals import *

# Define some colors
black = (0, 0, 0)
paddle = (255, 255, 255)
bricks = (0, 0, 255)

# --- Paddle class
class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(30, 50, 160, 16)


# --- Initialising all the Pygame modules
pygame.init()

screen = pygame.display.set_mode([800, 600])
background = pygame.image.load(bif).convert()
paddle = Paddle()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))

    pygame.display.update()

