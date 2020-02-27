import pygame, sys
from pygame.locals import *

WIDTH  = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
FRAMERATE = 60

pygame.init()
mainClock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

v_c = pygame.Vector2(WIDTH/2, HEIGHT/2)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    v_m = pygame.Vector2(mouse_x, mouse_y)

    v_m = v_m - v_c   # Verschil
    #v_m = v_m.normalize()
    #v_m = v_m * 50
    #v_m = v_m * 0.5   # Vermenigvuldiging

    m = v_m.magnitude()
    pygame.draw.rect(screen,BLUE,(0,0,m,10))

    pygame.draw.line(screen, WHITE, (0 + v_c.x, 0 + v_c.y), (v_m.x + WIDTH/2, v_m.y + HEIGHT/2)) # Translate naar het midden. 

    msElapsed = mainClock.tick(FRAMERATE)
    #pygame.display.update()
    pygame.display.flip()