import pygame as pg
from vector import Vector
from point import Point
from laser import Laser 
from pygame.sprite import Sprite
from timer import Timer
from random import randint

class Alien(Sprite):
    # alien_images0 = [pg.image.load(f"images/alien0{n}.png") for n in range(2)]
    alien_images0 = [pg.image.load("images/alien-1a.png"),pg.image.load("images/alien-1b.png")]
    alien_images1 = [pg.image.load("images/alien-2a.png"),pg.image.load("images/alien-2b.png")]
    alien_images2 = [pg.image.load("images/alien-3a.png"),pg.image.load("images/alien-3b.png")]
    alien_images = [alien_images0, alien_images1, alien_images2]
    alien_explosion = [pg.image.load("images/alien-explosion-1.png"),pg.image.load("images/alien-explosion-2.png")]  # fill in explosion images here

    def __init__(self, ai_game, v): 
        super().__init__()
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.v = v

        type = randint(0, 2)
        self.timer = Timer(images=Alien.alien_images[type], delta=900, start_index=type % 2)
        self.point_value = (2 ** type) * 10
       
        self.image = self.timer.current_image()
        #print(self.image)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.is_dying = False
        self.death_timer = 0
        self.current_frame = 1
        self.frame_length = 4
        self.last_breath = 0

        self.is_dead = False
        self.speedboost = 0

    def check_edges(self):
        sr = self.screen.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        r = self.rect 
        return self.x + self.rect.width >= sr.right or self.x <= 0
    
    def death_animation(self):
        if self.last_breath > 0:
            self.last_breath -= 1
            if self.last_breath == 0:
                self.is_dead = True
            return
        if self.is_dying:
            if self.death_timer % self.frame_length == 0:
                self.current_frame = (self.current_frame + 1) % 2
                self.image = self.alien_explosion[self.current_frame]
            self.death_timer += 1

            if self.death_timer >= 5 * self.frame_length:
                self.last_breath = 6

    #def increase_speed(self,speedboost):
    #    self.speedboost = speedboost
        
    def update(self):
        if not self.is_dying and not self.is_dead:
            self.x += self.v.x + self.speedboost
            self.y += self.v.y
            self.image = self.timer.current_image()
        if self.is_dying:
            self.death_animation()
            #self.image = self.alien_explosion
            #self.death_timer += 1
            #if self.death_timer >= 20:
            #    self.is_dead = True

        self.draw()
        
        
    def draw(self): 
        self.rect.x = self.x
        self.rect.y = self.y
        self.screen.blit(self.image, self.rect)


def main():
    print('\n run from alien_invasions.py\n')

if __name__ == "__main__":
    main()




