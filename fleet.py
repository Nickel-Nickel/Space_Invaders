import pygame as pg
from vector import Vector
from point import Point
from laser import Laser 
from sound import Sound
from alien import Alien
from pygame.sprite import Sprite
from random import randint

class Fleet(Sprite):
    def __init__(self, ai_game): 
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.ship = ai_game.ship
        self.aliens = pg.sprite.Group()
        self.fleet_lasers = pg.sprite.Group()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.sb = ai_game.sb
        self.v = Vector(self.settings.alien_speed, 0)
        # alien = Alien(ai_game=ai_game)
        # self.aliens.add(alien)
        self.spacing = 1.4
        self.create_fleet()
        # self.create_row()
        self.sound = Sound()
        self.lasers = pg.sprite.Group()
        self.laser_timer = 0
        self.laser_rate = 60

    def reset_fleet(self):
        self.aliens.empty()
        self.create_fleet()

    def create_fleet(self):
        alien = Alien(ai_game=self.ai_game, v=self.v)
        alien_height = alien.rect.height
        current_y = alien_height
        while current_y < (self.settings.scr_height - self.spacing * 6 * alien_height):
            self.create_row(current_y)
            current_y += self.spacing * alien_height
        
    def create_row(self, y):
        alien = Alien(ai_game=self.ai_game, v=self.v)
        alien_width = alien.rect.width
        current_x = alien_width 
        while current_x < (self.settings.scr_width - self.spacing * alien_width):
             new_alien = Alien(self, v=self.v)
             new_alien.rect.y = y
             new_alien.y = y
             new_alien.x = current_x
             new_alien.rect.x = current_x
             self.aliens.add(new_alien)
             current_x += self.spacing * alien_width

    def check_edges(self):
        for alien in self.aliens:
            if alien.check_edges(): 
                return True 
        return False
    
    def check_bottom(self):
        for alien in self.aliens:
            if alien.rect.bottom >= self.settings.scr_height:
                self.ship.ship_hit()
                return True
        return False
    
    def fire_laser(self):
        if self.laser_timer >= self.laser_rate:
            aliens_left = int(len(self.aliens))-1
            target = randint(0,aliens_left)
            index = 0
            for alien in self.aliens:
                if index == target:
                    laser = Laser(self.ai_game, alien, True) 
                    self.lasers.add(laser)
                    self.laser_timer = 0
                    self.laser_rate = randint(int((-aliens_left/2 + 71)),int((-aliens_left/2 + 98)))   
                    # Decreases rate of fire with fewer aliens
                index += 1
        else:
            self.laser_timer += 1

        self.lasers.update()
        for laser in self.lasers.copy():
            if laser.rect.bottom <= 0:
                self.lasers.remove(laser)
        for laser in self.lasers.sprites():
            laser.draw() 

    def update(self): 
        collisions = pg.sprite.groupcollide(self.ship.lasers, self.aliens, True, False)

        if collisions:
            for aliens in collisions.values():
                for alien in aliens:
                    self.sound.play_deathsound()
                    alien.image = alien.alien_explosion
                    alien.is_dying = True
                    self.stats.score += alien.point_value
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.ship.lasers.empty()
            self.create_fleet()
                    # Increase level.
            self.stats.level += 1
            self.sb.prep_level()
            return
        if pg.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!")
            self.ship.ship_hit()
            return
        
        if self.check_bottom():
            return 
        
        if self.check_edges():
            self.v.x *= -1 
            for alien in self.aliens:
                alien.v.x = self.v.x
                alien.y += self.settings.fleet_drop_speed
            
        for alien in self.aliens:
            alien.update()
            if alien.is_dead:
                        self.aliens.remove(alien)

        self.fire_laser()

    def draw(self): pass
        # for alien in self.aliens:
        #     alien.draw()

def main():
    print('\n run from alien_invasions.py\n')

if __name__ == "__main__":
    main()
