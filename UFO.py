import pygame as pg
from vector import Vector
from point import Point
from laser import Laser 
from pygame.sprite import Sprite
from timer import Timer
from random import randint

class UFO(Sprite):
    ufo_image = pg.image.load("images/ufo.png")
    ufo_explosion = pg.image.load("images/ufo-explosion.png")

    def __init__(self, ai_game,v): 
        super().__init__()
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.ship = ai_game.ship
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.sb = ai_game.sb
        self.v = v


        self.image = self.ufo_image
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.y)
        self.y = float(self.rect.y)

        self.is_dying = False
        self.death_timer = 0
        self.is_dead = False
        self.is_spawned = True
        self.spawn_timer = randint(15,45)
        self.time_since_last_spawn = 0

    def update(self):
        
        if not self.is_spawned:
            self.time_since_last_spawn += 1
            if self.time_since_last_spawn >= self.spawn_timer:
                self.spawn_ufo()
            return


        self.check_collision()
        
        if not self.is_dying:
            self.x = self.x + self.v.x

        if self.is_dying:
            self.image = self.ufo_explosion
            self.death_timer += 1
            if self.death_timer >= 15:
                self.is_dead = True

        self.draw()

    def check_collision(self):
        if pg.sprite.spritecollide(self,self.ship.lasers,True):
            self.is_dying = True

    def draw(self): 
        self.rect.x = self.x
        self.rect.y = self.y
        self.screen.blit(self.image, self.rect)


def main():
    print('\n run from alien_invasions.py\n')

if __name__ == "__main__":
    main()