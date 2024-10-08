import pygame as pg
from pygame.sprite import Sprite
from random import randint

class Laser(Sprite):


    ship_missile = pg.image.load("images/laser-reg.png")
    alien_missile = pg.image.load("images/laser-alien.png")

    def __init__(self, ai_game, is_alien = False):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # self.color = self.settings.laser_color
        if not is_alien:
            self.image = self.ship_missile
        else:
            self.image = self.alien_missile
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.laser_speed
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)

def main():
    print("\nYou have to run from alien_invasion.py\n")

if __name__ == "__main__":
    main()
