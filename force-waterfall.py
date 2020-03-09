import pygame, sys
from pygame.locals import *

import pygame.gfxdraw
from pygame import math

from random import randint

WIDTH  = 1600 #1024
HEIGHT = 768

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
STEP = 1
AANTAL_CIRKELS = 10
FRAMERATE = 30
VELOCITY = 0
ACCELERATION = 0
GRAVITY = math.Vector2(0, 0.3)
WIND    = math.Vector2(0.1, -0.2)
FRICTION_COEF = 0.03

pygame.init()

class Cirkel(pygame.sprite.Sprite):
    def __init__(self, x, y, r, text):
        pygame.sprite.Sprite.__init__(self)

        self.mass   = randint(2, 4)
        self.radius = self.mass * r  # Hoe zwaarder, hoe groter
        self.pos    = math.Vector2(int(x), int(y))
        self.vel    = math.Vector2(int(randint(-1*VELOCITY, VELOCITY)), int(randint(-1*VELOCITY, VELOCITY)))
        self.acc    = math.Vector2(0, 0)
        
        self.color  = (randint(0,255), randint(0,255), randint(0,255))
        self.text   = text
        self.collided = False
        self.remove = False

        self.image  = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)  # Voor een standaard cirkel sprite
        #self.image2  = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)  # Voor een standaard rode cirkel sprite
        self.rect    = self.image.get_rect()  # Zelfde RECT voor image1 en image2

        self.font      = pygame.font.SysFont("Arial", 20)     # Font van text op sprite
        self.text_surf = self.font.render(text, 1, WHITE)  # Surface van de text

        pygame.gfxdraw.filled_circle(self.image, self.radius, self.radius, self.radius, self.color) # Standaard Sprite met gevulde cirkel
        #pygame.gfxdraw.filled_circle(self.image2, self.radius, self.radius, self.radius, RED)        # Sprite gevuld met rode cirkel

        W = self.text_surf.get_width()
        H = self.text_surf.get_height()
        self.image.blit(self.text_surf, [self.radius - W/2, self.radius - H/2])  # 'Blit' de text in het midden van de sprite.
        #self.image2.blit(self.text_surf, [self.radius - W/2, self.radius - H/2])  # 'Blit' de text in het midden van de sprite.
        
        self.vectors = []  # Vectors wijzend naar andere objecten

    def apply_force(self, force):
        f = force / self.mass
        self.acc += f

    def update(self, sprites):

        self.vel += self.acc
        self.pos += self.vel

        if (self.pos.x - self.radius) > WIDTH:  # Verwijder sprite wanneer deze 'verdwijnt' aan de linkerrand
            #self.remove = True
            nr = self.text
            sprites.remove(self)
            #self.cirkels.append(Cirkel(0+45, (HEIGHT/2+randint(-50, 50)), randint(10,20), "A" ))
            sprites.add(Cirkel(0+45, (HEIGHT/2+randint(-50, 50)), randint(10,20), nr))

        if ((self.pos.y - self.radius) < 0):
            self.vel += self.acc
            self.vel.y = self.vel.y * -1
        else:
            if ((self.pos.y + self.radius) > HEIGHT):
                self.vel += self.acc
                self.vel.y = self.vel.y * -1  #int(self.vel.y * -1)

        self.acc = self.acc * 0
        self.rect.center = (self.pos.x, self.pos.y)

        #self.vectors = []
#
        #for cirkel in sprites:  # Bereken de vector tussen 2 sprites
        #   if cirkel == self:   # Niet met zichzelf
        #       continue
        #   else:
        #       v_diff = cirkel.pos - self.pos   # Vector van deze sprite naar een andere
        #       self.vectors.append(v_diff.normalize() * 100)

    def draw(self, screen):

        #if self.collided:
        screen.blit(self.image, self.rect) # Standaard sprite-image
        #else:
        #    screen.blit(self.image1, self.rect) # Rode sprite-image  

        #for vector in self.vectors:
        #    pygame.gfxdraw.line(screen, int(self.pos.x), int(self.pos.y), int(vector.x + self.pos.x), int(vector.y + self.pos.y), WHITE)
        #    pygame.gfxdraw.filled_circle(screen, int(self.pos.x+vector.x), int(self.pos.y+vector.y), 5, RED)  # Bolletje op lijn   

    def __repr__(self):
        print()
        print(f"x={self.pos.x}, y={self.pos.y}")
        print(f"radius = {self.radius}")
        print(f"speed  = {self.vel.x}, {self.vel.y}")
        print(f"color  = {self.color}")
        print(f"text   = {self.text}")
        return " "

class Sketch():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background =pygame.Surface((self.screen.get_width(), self.screen.get_height())) # Achtergrond met afmetingen van 'screen'
        self.col = 0
        
        self.cirkels = [Cirkel(0+45, (HEIGHT/2+randint(-50, 50)), randint(10,20), str(x) ) for x in range(1, AANTAL_CIRKELS+1)]
        self.all_sprites = pygame.sprite.RenderUpdates(self.cirkels)

        pygame.display.set_caption(f"Venster met {len(self.all_sprites.sprites())} sprites o.i.v. wind {WIND} en frictie {FRICTION_COEF}")
    
    def detect_collisions(self):
        for a_sprite in self.all_sprites:
            other_sprites = self.all_sprites.copy()
            other_sprites.remove(a_sprite)  # Zodat other_sprites alle sprites zijn minus a_sprite
            sprite_coll = pygame.sprite.spritecollideany(a_sprite, other_sprites) # Bepaal collision met a_sprite
            if sprite_coll:
                a_sprite.collided = True
            else:
                a_sprite.collided = False

    def run(self):
        clock = pygame.time.Clock()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            for sprite in self.all_sprites:
                
                sprite.apply_force(GRAVITY * sprite.mass)  # Vermenigvuldigen met Mass en delen door Mass in apply_force: heffen elkaar op.
                sprite.apply_force(WIND)                   # Wordt in apply_force nog gedeeld door Mass.

                #if sprite.vel != [0,0]:   # Als sprite.vel 0 -> geen normalize() van 0.
                #    f_vel = (sprite.vel.normalize() * -1) * FRICTION_COEF
                #    sprite.apply_force(f_vel)

            #sprite.update(self.all_sprites)
            self.all_sprites.update(self.all_sprites)

            #self.detect_collisions()

            #self.screen.fill((BLACK))

            #self.all_sprites.draw(self.screen)
            for sprite in self.all_sprites:
                sprite.draw(self.screen)

            pygame.display.update()
            clock.tick(FRAMERATE)
                
if __name__ == "__main__":
    sketch = Sketch()
    sketch.run()
