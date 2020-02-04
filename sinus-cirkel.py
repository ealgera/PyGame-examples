from random import randint
import pygame, sys
from pygame.locals import *
from math import sin, cos, pi, radians

WIDTH  = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FRAMERATE = 30

pygame.init()
mainClock = pygame.time.Clock()

def cirkel(r, iteraties):
    punten = []
    #hoek = ((2 * pi) / iteraties)
    hoek = ((360) / iteraties)

    #print(f"iteraties: {iteraties}, hoek: {hoek}\n")

    for i in range(iteraties):
        x = int(r * cos(radians(hoek)) + WIDTH/2)
        y = int(r * sin(radians(hoek)) + HEIGHT/2)
        v_c = pygame.Vector2(x,y)
        punten.append((v_c))
        #print(f"({x}, {y}) - {hoek} graden")
        hoek = hoek + ((360) / iteraties)

    print(punten)
    
    return (punten)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(BLACK)
pygame.draw.polygon(screen, WHITE, cirkel(200,100), 1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #screen.fill(BLACK)

    #for x, y in cirkel(100, 5):
    #    screen.set_at((int(x + WIDTH/2), int(y + HEIGHT/2)), (255, 255, 255))
    #pygame.draw.polygon(screen, WHITE, cirkel(200,5))
    
    msElapsed = mainClock.tick(FRAMERATE)
    pygame.display.update()
