import pygame
import sys
from pygame.locals import *
pygame.init()

SCREEN_SIZE = pygame.display.set_mode((640,360),0,32)

Brick_Colour = (240,186,0)
Brick_Width = 60
Brick_Height = 15
Paddle_Width = 60
Paddle_Height = 12
Ball_Diameter = 16
Ball_Radius = Ball_Diameter/2

Max_Paddle_X = SCREEN_SIZE[0] - Paddle_Width
Max_Ball_X   = SCREEN_SIZE[0] - Ball_Diameter
Max_Ball_Y   = SCREEN_SIZE[1] - Ball_Diameter

Paddle_Y     = SCREEN_SIZE[1] - Paddle_Height -10
Xpos = 35
Ypos = 35
bricks = []
for i in range(10):
    for i in range(4):
        bricks.append(pygame.Rect(Xpos, Ypos, Brick_Width, Brick_Height))
        Xpos += Brick_Width + 10
        Ypos += Brick_Height + 5    

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    

    for brick in bricks:
        pygame.draw.rect(SCREEN_SIZE, Brick_Colour, brick)



    pygame.display.update()                       
    
