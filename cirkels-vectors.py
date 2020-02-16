from random import randint
import pygame, sys
from pygame.locals import *

import pygame.gfxdraw
from pygame import math

WIDTH  = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
STEP = 1
AANTAL_CIRKELS = 5
FRAMERATE = 60

pygame.init()

class Cirkel(pygame.sprite.Sprite):
    def __init__(self, x, y, r, text):
        pygame.sprite.Sprite.__init__(self)

        self.radius = r
        self.pos = math.Vector2(int(x), int(y))
        self.vel = math.Vector2(int(randint(-15, 15)), int(randint(-15, 15)))
        self.color = (randint(0,255), randint(0,255), randint(0,255))
        self.text = text

        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        self.font = pygame.font.SysFont("Arial", 20)       # Font van text op sprite
        self.text_surf = self.font.render(text, 1, WHITE)  # Surface van de text
        W = self.text_surf.get_width()
        H = self.text_surf.get_height()

        pygame.gfxdraw.filled_circle(self.image, self.radius, self.radius, self.radius, self.color)
        self.image.blit(self.text_surf, [self.radius - W/2, self.radius - H/2])  # 'Blit' de text in het middem van de sprite.

    def __repr__(self):
        print()
        print(f"x={self.pos.x}, y={self.pos.y}")
        print(f"radius = {self.radius}")
        print(f"speed  = {self.vel.x}, {self.vel.y}")
        print(f"color  = {self.color}")
        print(f"text   = {self.text}")
        return " "

    def update(self):
        self.pos.x += self.vel.x
        if (self.pos.x - self.radius) < 0 or (self.pos.x + self.radius) > WIDTH:
            self.vel.x = self.vel.x * -1

        self.pos.y += self.vel.y
        if (self.pos.y - self.radius) < 0 or (self.pos.y + self.radius) > HEIGHT:
            self.vel.y = self.vel.y * -1

        self.rect.center = (self.pos.x, self.pos.y)

    def draw(self, screen):
        #v = other.pos - self.pos
        #pygame.gfxdraw.filled_circle(screen, int(self.pos.x), int(self.pos.y), self.radius, self.color)
    #    aaline(surface, color, start_pos, end_pos)
        pass

class Sketch():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background =pygame.Surface((self.screen.get_width(), self.screen.get_height())) # Achtergrond met afmetingen van 'screen'
        self.col = 0
        
        self.cirkels = [Cirkel(randint(100,500), randint(200,500), randint(20,40), str(x) ) for x in range(AANTAL_CIRKELS)]
        self.all_sprites = pygame.sprite.Group(self.cirkels)
        self.dirty_rects = []

        pygame.display.set_caption(f"Venster met {len(self.all_sprites.sprites())} sprites en collision-detection")
    
    def detect_collisions(self):
        for a_sprite in self.all_sprites:
            other_sprites = self.all_sprites.copy()
            other_sprites.remove(a_sprite)  # Zodat other_sprites alle sprites zijn minus a_sprite
            sprite_coll = pygame.sprite.spritecollideany(a_sprite, other_sprites) # Bepaal collision met a_sprite
            if sprite_coll:
                #self.col += 1
                #print(f"{self.col}) - Collision: {a_sprite.text} met {sprite_coll.text}")
                pygame.gfxdraw.filled_circle(a_sprite.image, a_sprite.radius, a_sprite.radius, a_sprite.radius, (255,0,0))  # Rode sprite
            else:
                pygame.gfxdraw.filled_circle(a_sprite.image, a_sprite.radius, a_sprite.radius, a_sprite.radius, a_sprite.color)
            W = a_sprite.text_surf.get_width()
            H = a_sprite.text_surf.get_height()
            a_sprite.image.blit(a_sprite.text_surf, [a_sprite.radius - W/2, a_sprite.radius - H/2])  # 'Blit' de text in het middem van de sprite.

    def run(self):
        clock = pygame.time.Clock()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            for cirkel in self.cirkels:
                pygame.gfxdraw.filled_circle(cirkel.image, int(cirkel.pos.x), int(cirkel.pos.y), cirkel.radius, BLACK)  # Clear Sprite
                #self.dirty_rects.append(cirkel.rect)
                cirkel.update()
                cirkel.draw(self.screen)
                self.dirty_rects.append(cirkel.rect)
            
            print(len(self.dirty_rects))
            pygame.display.update(self.dirty_rects)
            self.dirty_rects = []

            #self.all_sprites.update()          # Voer de .update methode uit voor iedere sprite in de sprites-Group
            #self.one_sprite.update()

            #self.detect_collisions()

            #self.all_sprites.clear(self.screen, self.background)
            #self.one_sprite.clear(self.screen, self.background)
            

            #self.all_sprites.draw(self.screen) # 'Teken' alle sprites.
            #self.one_sprite.draw(self.screen)

            #for this_cirkel in self.cirkels:
            #    for other_cirkel in self.cirkels:
            #        if this_cirkel != other_cirkel:
            #            this_cirkel.draw(self.screen, other_cirkel)

            #pygame.display.flip()
            clock.tick(FRAMERATE)
                
if __name__ == "__main__":
    sketch = Sketch()
    sketch.run()
