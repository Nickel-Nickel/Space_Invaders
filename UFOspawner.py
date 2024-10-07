from random import randint
import pygame as pg
from vector import Vector
from point import Point
from laser import Laser 
from sound import Sound
from UFO import UFO
from pygame.sprite import Sprite

class UFOSpawner(Sprite):
    def __init__(self, ai_game): 
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.ship = ai_game.ship
        self.UFOs = pg.sprite.Group()
        self.fleet_lasers = pg.sprite.Group()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.sb = ai_game.sb
        self.v = Vector(self.settings.ufo_speed, 0)
        self.sound = Sound()
        self.spawn_delay = randint(600,900)
        self.spawn_timer = 0
        
        self.create_UFO()


    def reset_UFOs(self):
        self.UFOs.empty()
        self.create_UFO()

    def create_UFO(self):
        if self.spawn_timer < self.spawn_delay:
             self.spawn_timer += 1
             return
        
        rng = randint(1,2)
        if rng == 2:             # spawn right, move left
            self.v = -self.v
        
        ufo = UFO(ai_game=self.ai_game, v=self.v)
        self.UFOs.add(ufo)
        
        if rng == 1:
            ufo.x = -ufo.rect.width
        elif rng == 2:
            ufo.x = self.screen.get_width()
        
        self.spawn_timer = 0
        

    def update(self):
        collisions = pg.sprite.groupcollide(self.ship.lasers, self.UFOs, True, False)

        if collisions:
            for UFOs in collisions.values():
                for ufo in UFOs:
                    ufo.image = ufo.ufo_explosion
                    ufo.is_dying = True
                self.stats.score += self.settings.UFO_points[randint(0,4)]
                self.sound.play_deathsound()
            self.sb.prep_score()
            self.sb.check_high_score()

        for ufo in self.UFOs:
            ufo.update()
            if (ufo.is_dead) or (ufo.x > self.screen.get_width() + ufo.rect.width) or (ufo.x < 2 * -ufo.rect.width):
                        self.UFOs.remove(ufo)
                        self.spawn_delay = randint(600,1500)

        if not self.UFOs:
            self.create_UFO()
    

def main():
    print('\n run from alien_invasions.py\n')

if __name__ == "__main__":
    main()

    
