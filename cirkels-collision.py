from random import randint
import pygame, sys
from pygame.locals import *

import pygame.gfxdraw

WIDTH  = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
STEP = 1
AANTAL_CIRKELS = 100
FRAMERATE = 60

pygame.init()

class Cirkel(pygame.sprite.Sprite):
    def __init__(self, x, y, r, text):
        pygame.sprite.Sprite.__init__(self)

        self.radius = r
        self.x = x
        self.y = y
        self.xspeed = randint(-5, 5)
        self.yspeed = randint(-5, 5)
        self.color = (randint(0,255), randint(0,255), randint(0,255))
        self.text = text

        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        self.font = pygame.font.SysFont("Arial", 24)       # Font van text op sprite
        self.text_surf = self.font.render(text, 1, WHITE)  # Surface van de text
        W = self.text_surf.get_width()
        H = self.text_surf.get_height()

        pygame.gfxdraw.filled_circle(self.image, self.radius, self.radius, self.radius, self.color)
        self.image.blit(self.text_surf, [self.radius - W/2, self.radius - H/2])  # 'Blit' de text in het middem van de sprite.

    def __repr__(self):
        print()
        print(f"x={self.x}, y={self.y}")
        print(f"radius = {self.radius}")
        print(f"speed  = {self.xspeed}, {self.yspeed}")
        print(f"color  = {self.color}")
        print(f"text   = {self.text}")
        return " "

    def update(self):
        self.x += self.xspeed
        if (self.x - self.radius) < 0 or (self.x + self.radius) > WIDTH:
            self.xspeed = self.xspeed * -1

        self.y += self.yspeed
        if (self.y - self.radius) < 0 or (self.y + self.radius) > HEIGHT:
            self.yspeed = self.yspeed * -1

        self.rect.center = (self.x, self.y)

class Sketch():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background =pygame.Surface((self.screen.get_width(), self.screen.get_height())) # Achtergrond met afmetingen van 'screen'
        self.col = 0
        
        #self.cirkels = [Cirkel() for x in range(AANTAL_CIRKELS)]
        c1 = Cirkel(100, 100, 20, "1")
        c2 = Cirkel(200, 200, 20, "2")
        c3 = Cirkel(300, 300, 20, "3")
        c4 = Cirkel(400, 400, 20, "4")
        c5 = Cirkel(500, 500, 20, "5")
        self.objects = [c1 , c2, c3, c4, c5]
        self.all_sprites = pygame.sprite.Group(c1 , c2, c3, c4, c5)

        pygame.display.set_caption(f"Venster met {len(self.all_sprites.sprites())} sprites")
    
    def detect_collisions(self):
        for a_sprite in self.all_sprites:
            other_sprites = self.all_sprites.copy()
            other_sprites.remove(a_sprite)
            sprite_coll = pygame.sprite.spritecollideany(a_sprite, other_sprites)
            if sprite_coll:
                self.col += 1
                print(f"{self.col}) - Collision: {a_sprite.text} met {sprite_coll.text}")
                pygame.gfxdraw.filled_circle(a_sprite.image, a_sprite.radius, a_sprite.radius, a_sprite.radius, (255,0,0))

    def run(self):
        clock = pygame.time.Clock()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.all_sprites.update()          # Voer de .update methode uit voor iedere sprite in de sprites-Group
            #self.one_sprite.update()

            self.detect_collisions()

            self.all_sprites.clear(self.screen, self.background)
            #self.one_sprite.clear(self.screen, self.background)
            
            self.all_sprites.draw(self.screen) # 'Teken' alle sprites.
            #self.one_sprite.draw(self.screen)

            pygame.display.flip()
            clock.tick(FRAMERATE)
                
if __name__ == "__main__":
    sketch = Sketch()
    sketch.run()
