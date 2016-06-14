
import pygame, sys
from pygame.locals import *

pygame.init()


screen = pygame.display.set_mode((640, 800))
color = (210, 90, 0)
color1 = (190, 245, 0)
wickets = pygame.Rect(280, 30, 60, 100)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.lock()

  #---  pygame.draw.circle(screen, color, position, radius)

    pygame.draw.rect(screen, color, wickets)
    print(wickets.left)

    screen.unlock()

    pygame.display.update()
  

     
    
