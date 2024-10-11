import sys
import pygame as pg
from colors import OFF_WHITE, DARK_GREY
from settings import Settings
from ship import Ship
from vector import Vector
from fleet import Fleet
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from event import Event
from barrier import Barriers
from sound import Sound
from UFOspawner import UFOSpawner
from screens import Screens

class AlienInvasion:
    def __init__(self):
        pg.init()   
        self.clock = pg.time.Clock()
        self.settings = Settings()
        self.screen = pg.display.set_mode(self.settings.w_h)
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.sound = Sound()

        self.screens = Screens(ai_game=self)
        self.ship = Ship(ai_game=self)
        self.fleet = Fleet(ai_game=self)
        self.ship.set_fleet(self.fleet)
        self.ship.set_sb(self.sb)
        self.barriers = Barriers(ai_game=self)
        self.UFOSpawner = UFOSpawner(ai_game=self)

        pg.display.set_caption("Alien Invasion")
        self.bg_color = self.settings.bg_color

        # Start Alien Invasion in an inactive state.
        self.game_state = "Start"
        print("State: Start      Source: Init")
        self.game_active = False
        self.first = True

        self.event = Event(self)

    def game_over(self):
        self.sound.play_gameover()
        self.game_state = "Restart"
        print("State: Restart      Source: Death")
        self.restart_game()
        # print("Game over!") 
        # self.sound.play_gameover()
        # sys.exit()

    def reset_game(self):
        self.stats.reset_stats()
        self.sb.prep_score_level_ships()
        self.game_active = True
        self.first = False
        self.sound.play_background()

        self.ship.reset_ship()
        self.fleet.reset_fleet()
        pg.mouse.set_visible(False)

    def restart_game(self):
        #self.game_state = "Restart"
        self.game_active = False
        # self.first = True
        pg.mouse.set_visible(True)
        #self.screens.display_restart()
        #pg.display.flip()
        self.event.check_events()

    def run_game(self):
        self.finished = False
        self.first = True
        self.game_active = False
        self.game_state = "Start"
        print("State: Start      Source: Bootup")

        while not self.finished:
            self.finished = self.event.check_events()
            if  self.game_state == "Game":
                self.first = False
                self.screen.fill(self.bg_color)
                self.ship.update()
                self.fleet.update()
                self.sb.show_score()
                self.barriers.update()
                self.UFOSpawner.update()
            elif self.game_state == "Start":
                self.screen.fill(self.bg_color)
                self.screens.display_start()
            elif self.game_state == "Restart":
                self.screen.fill(self.bg_color)
                self.screens.display_restart()

            pg.display.flip()

            self.clock.tick(60)
        sys.exit()

      

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
