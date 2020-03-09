import pygame, sys
from pygame.locals import *

import pygame.gfxdraw
from pygame import math

from random import randint
import numpy as np
from math import cos, sin, pi

WIDTH  = 1024
HEIGHT = 768

XMIN, XMAX = -300, 300  # Gebruikte coordinaten, GEEN pygame-coordinaten!
YMIN, YMAX = -300, 300

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

FRAMERATE = 30

m_rechthoek = [[-100, 50],
               [100, 50],
               [100, -50],
               [-100, -50],
               [-100, 50]]

kanten = [[0,1], [1,2], [2,3], [3,0]]
m_trans = [[0,-1],
           [1, 1]]

pygame.init()


class Sketch():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background =pygame.Surface((self.screen.get_width(), self.screen.get_height())) # Achtergrond met afmetingen van 'screen'

        pygame.display.set_caption(f"Venster met roterende rechthoek")

    def screenXY(self, punt):
        # Vertaal scherm-coordinaten (xmin/xmax enz) naar pygame-coordinaten
        return [(punt[0]*(WIDTH/(XMAX-XMIN)) + WIDTH/2),       # X gaat van links (-) naar rechts (+)
                (punt[1]*(HEIGHT/(YMAX-YMIN)*-1) + HEIGHT/2)]  # Y gaat van beneden (-) naar boven (+)

    def matMult(self, a, b):
        return np.dot(a, b)

    def rotate(self, rad):
        m_rot = [
            [cos(rad), -sin(rad)],
            [sin(rad),  cos(rad)]
        ]
        return m_rot

    def setup(self):
        self.draw(m_rechthoek, RED)

    def update(self, a, hoek):
        return self.matMult(a, self.rotate(hoek))

    def draw(self, m, kleur):
        for k in kanten:
            pygame.draw.line(self.screen, kleur, self.screenXY(m[k[0]]), self.screenXY(m[k[1]]), 2)
    
    def run(self):
        clock = pygame.time.Clock()
        done = False
        hoek = pi/64

        self.setup()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            self.screen.fill((BLACK))
            new_m = self.update(m_rechthoek, hoek)
            self.draw(new_m, WHITE)
            
            hoek += pi/64

            pygame.display.update()
            clock.tick(FRAMERATE)
                
if __name__ == "__main__":
    sketch = Sketch()
    sketch.run()
