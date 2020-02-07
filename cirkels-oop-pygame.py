from random import randint
import pygame, sys
from pygame.locals import *

import pygame.gfxdraw

WIDTH  = 800
HEIGHT = 600

BLACK = (0, 0, 0)
STEP = 1
AANTAL_CIRKELS = 100
FRAMERATE = 30

pygame.init()

class Cirkel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.r = randint(10, 40)
        self.x = int(WIDTH / 2) + randint(-50, 50)
        self.y = int(HEIGHT / 2)  + randint(-50, 50)
        self.xspeed = randint(-20, 20)
        self.yspeed = randint(-10, 10)
        self.color = (randint(0,255), randint(0,255), randint(0,255))

        self.image = pygame.Surface((self.r * 2, self.r * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        pygame.gfxdraw.filled_circle(self.image, self.r, self.r, self.r, self.color)

    def __repr__(self):
        print()
        print(f"x={self.x}, y={self.y}")
        print(f"straal= {self.r}")
        print(f"speed = {self.xspeed}, {self.yspeed}")
        print(f"color = {self.color}")
        return " "

    def update(self):
        self.x += self.xspeed
        if (self.x - self.r) < 0 or (self.x + self.r) > WIDTH:
            self.xspeed = self.xspeed * -1

        self.y += self.yspeed
        if (self.y - self.r) < 0 or (self.y + self.r) > HEIGHT:
            self.yspeed = self.yspeed * -1

        self.rect.center = (self.x, self.y)

class Sketch():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background =pygame.Surface((self.screen.get_width(), self.screen.get_height())) # Achtergrond met afmetingen van 'screen'
        pygame.display.set_caption("Een Window")

        self.cirkels = [Cirkel() for x in range(AANTAL_CIRKELS)]
        self.all_sprites = pygame.sprite.Group()
        for cirkel in self.cirkels:
            self.all_sprites.add(cirkel)   # Voeg iedere cirkel-sprite toe aan een sprite-group

    def run(self):
        clock = pygame.time.Clock()
        done = False
        while not done:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.all_sprites.clear(self.screen, self.background)
            self.all_sprites.update()          # Voer de .update methode uit voor iedere sprite in de sprites-Group
            self.all_sprites.draw(self.screen) # 'Teken' alle sprites.

            pygame.display.flip()
                
if __name__ == "__main__":
    sketch = Sketch()
    sketch.run()
