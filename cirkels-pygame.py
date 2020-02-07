from random import randint
import pygame, sys
from pygame.locals import *

WIDTH  = 800
HEIGHT = 600

BLACK = (0, 0, 0)
STEP = 1
AANTAL_CIRKELS = 100
FRAMERATE = 30

pygame.init()
mainClock = pygame.time.Clock()

class Cirkel():

    def __init__(self, scr):
        self.r = randint(20, 25)
        self.x = int(WIDTH / 2) + randint(-50, 50)
        self.y = int(HEIGHT / 2)  + randint(-50, 50)
        self.xspeed = randint(-20, 20)
        self.yspeed = randint(-10, 10)
        self.color = (randint(0,255), randint(0,255), randint(0,255))
        self.screen = scr

    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.x,self.y), self.r, 0)

    def move(self):
        self.x += self.xspeed
        if (self.x - self.r) < 0 or (self.x + self.r) > WIDTH:
            self.xspeed = self.xspeed * -1

        self.y += self.yspeed
        if (self.y - self.r) < 0 or (self.y + self.r) > HEIGHT:
            self.yspeed = self.yspeed * -1
        
screen = pygame.display.set_mode((WIDTH,HEIGHT))

cirkels = [Cirkel(screen) for x in range(AANTAL_CIRKELS)]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    for cirkel in cirkels:
        cirkel.show()
        cirkel.move()

    msElapsed = mainClock.tick(FRAMERATE)
    pygame.display.update()