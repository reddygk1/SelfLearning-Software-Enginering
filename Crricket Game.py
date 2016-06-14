import pygame, sys
import random
from pygame.locals import *
pygame.init()

black = (0, 0, 0)
WicketsColour = (160, 82, 45)
PitchColour = (255, 250, 250)
ballColour = (178, 34, 34)
red = (	139, 69, 19)

class Pitch:
    def __init__(self):

        self.rect = pygame.Rect(235, 30, 150, 750)

    def draw(self):
        pygame.draw.rect(screen, PitchColour, self.rect)


class Layout:
    def __init__(self):

        self.wicket = pygame.Rect(300, 20, 5, 100)
        self.wicket2 = pygame.Rect(320, 20, 5, 100)
        self.wicket3 = pygame.Rect(280, 20, 5, 100)
        self.bail1 = pygame.Rect(303, 15, 18, 5)
        self.bail2 = pygame.Rect(283, 15, 18, 5)

    def draw(self):

        pygame.draw.rect(screen, WicketsColour, self.wicket)
        pygame.draw.rect(screen, WicketsColour, self.wicket2)
        pygame.draw.rect(screen, WicketsColour, self.wicket3)
        pygame.draw.rect(screen, WicketsColour, self.bail1)
        pygame.draw.rect(screen, WicketsColour, self.bail2)


class Ball:
    def __init__(self, pos):
        self.reset(pos)

    def reset(self, pos):
        self.rect = pygame.Rect(pos, 750, 18, 18)
        self.dx = 1
        self.dy = -3

    def move(self):
        self.rect.y += self.dy

    def moveRight(self):
        self.rect.x += 1
        self.rect.y += self.dy

    def moveLeft(self):
        self.rect.x -= 1
        self.rect.y += self.dy

    def draw(self):
        pygame.draw.ellipse(screen, ballColour, self.rect)

screen = pygame.display.set_mode((640, 800), 0, 32)


class Game:
    def __init__(self):
        self.running = False
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screenSize = self.screenWidth, self.screenHeight = (640, 800)
        pygame.display.set_caption("Cricket!!")
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(self.screenSize)

        self.boopSound = pygame.mixer.Sound('boop.wav')
        self.bloopSound = pygame.mixer.Sound('bloop.wav')
        self.explosionSound = pygame.mixer.Sound('explosion.wav')

        self.font = pygame.font.Font(None, 16)
        self.pitch = Pitch()
        self.layout = Layout()
        self.ball = Ball(240)

        self.topEdge = pygame.Rect(235, 30, 150, 18)
        self.wicketEdge = pygame.Rect(250, 30, 60, 70)

        self.balls = 6
        self.score = 0
        self.count = 0

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.event.post(pygame.event.Event(QUIT))

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.tick()
            self.render()

            pygame.display.update()
            self.clock.tick(30)

    def render(self):
        self.screen.fill(black)
        self.pitch.draw()
        self.layout.draw()
        self.ball.draw()

        # Draw scoreboard
        scoreSurface = self.font.render("Balls  " + str(self.balls) + "   Score  " + str(self.score), False, red)
        self.screen.blit(scoreSurface, (30, 30))

        scoreSurface1 = self.font.render("", False, red)
        self.screen.blit(scoreSurface1, (30, 30))

        pygame.display.update()


    def tick(self):

        # Update the ball position
        self.ball.moveRight()
        self.ball.move()


        if self.ball.rect.top > (self.topEdge.top + 150):
            self.rand = random.randrange(1, 4)
            if self.rand == 1:
                self.ball.moveRight()
                self.ball.moveRight()
            elif self.rand == 2:
                self.ball.moveLeft()
                self.ball.moveLeft()
            elif self.rand == 3:
                self.ball.move()
                self.ball.moveRight()

        if self.ball.rect.right >= self.topEdge.right:
             self.boopSound.play()
             self.offPitch()
        elif self.ball.rect.top <= self.topEdge.top:
             self.bloopSound.play()
             self.missed()
        elif self.ball.rect.left <= self.topEdge.left:
             self.boopSound.play()
             self.offPitch()

        if self.ball.rect.top + 18 <= self.wicketEdge.bottom and self.ball.rect.centerx + 18 > 250 and self.ball.rect.centerx - 18 < 315:
            self.explosionSound.play()
            self.bowled()


        if self.balls <= 0:
            self.gameOver()

    def offPitch(self):
        self.balls = self.balls - 1
        messageSurface = self.font.render("Its off the Pitch", False, red)
        self.screen.blit(messageSurface, (500, 30))
        self.count = 0
        pygame.display.update()
        pygame.time.wait(2000)
        self.ball.reset(240)
        pygame.display.update()

    def bowled(self):
        self.balls = self.balls - 1
        messageSurface2 = self.font.render("You got a wicket", False, red)
        self.screen.blit(messageSurface2, (500, 30))
        self.count += 1
        self.score = self.score + 10 * self.count
        pygame.display.update()
        pygame.time.wait(2000)
        self.ball.reset(240)
        pygame.display.update()

    def missed(self):
        self.balls = self.balls - 1
        messageSurface1 = self.font.render("You missed the stump", False, red)
        self.screen.blit(messageSurface1, (500, 30))
        pygame.display.update()
        self.count = 0
        pygame.time.wait(2000)
        self.ball.reset(240)
        pygame.display.update()

    def gameOver(self):
        messageSurface = self.font.render("Game Over and your score is " + str(self.score), False, red)
        self.screen.blit(messageSurface, ((self.screenWidth - messageSurface.get_width()) / 2, 240))
        scoreSurface3 = self.font.render("Balls  " + str(self.balls) + "   Score  " + str(self.score), False, red)
        self.screen.blit(scoreSurface3, (30, 30))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()
        #self.resetGame()

game = Game()
game.run()




