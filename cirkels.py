from random import randint
import pygame, sys
from pygame.locals import *

WIDTH  = 800
HEIGHT = 600

BLACK = (0, 0, 0)
STEP = 1

pygame.init()
mainClock = pygame.time.Clock()

class Cirkel():

    def __init__(self, scr):
        self.r = randint(20, 80)
        self.x = randint(self.r, WIDTH - self.r)
        self.y = randint(self.r, HEIGHT - self.r)
        
        self.color = (randint(0,255), randint(0,255), randint(0,255))
        self.screen = scr

    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.x,self.y), self.r, 0)

    def move(self):
        self.x += randint(-1*STEP, 1*STEP)
        if (self.x - self.r) < 0:
            self.x = self.r
        if (self.x + self.r) > WIDTH:
            self.x -= (self.r + STEP)

        self.y += randint(-1*STEP, STEP)
        if (self.y - self.r) < 0:
            self.y = self.r
        if (self.y + self.r) > HEIGHT:
            self.y -= (self.r + STEP)

screen = pygame.display.set_mode((WIDTH,HEIGHT))

cirkels = [Cirkel(screen) for x in range(25)]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    for cirkel in cirkels:
        cirkel.show()
        cirkel.move()

    msElapsed = mainClock.tick(30)
    pygame.display.update()