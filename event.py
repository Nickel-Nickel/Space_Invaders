import pygame as pg
import sys 
from vector import Vector 
from screens import Screens

class Event:
    di = {pg.K_RIGHT: Vector(1, 0), pg.K_LEFT: Vector(-1, 0),
      pg.K_UP: Vector(0, -1), pg.K_DOWN: Vector(0, 1),
      pg.K_d: Vector(1, 0), pg.K_a: Vector(-1, 0),
      pg.K_w: Vector(0, -1), pg.K_s: Vector(0, 1)
      }

    def __init__(self, ai_game):
        self.ai_game = ai_game 
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.sb = ai_game.sb
        self.ship = ai_game.ship
        self.screens = ai_game.screens
        self.play_button = self.screens.play_button
        self.highscores_button = self.screens.highscores_button
        self.menu_button = self.screens.menu_button
        self.quit_button = self.screens.quit_button

    def check_events(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT) or (event.type == pg.KEYDOWN and event.key == pg.K_q):
                sys.exit()
                return True   # finished is True
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self.check_highscores_button(mouse_pos)
                self.check_menu_button(mouse_pos)
                self.check_quit_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and (self.ai_game.game_state == "Restart" or self.ai_game.game_state == "Start"):
            self.settings.initialize_dynamic_settings()
            self.ai_game.game_state = "Game"
            print("State: Game      Source: Play")
            self.ai_game.reset_game()
    
    def check_highscores_button(self, mouse_pos):
        button_clicked = self.highscores_button.rect.collidepoint(mouse_pos)
        if button_clicked and self.ai_game.game_state == "Start":
            print("Pressed Highscores!")
            sys.exit()
    
    def check_menu_button(self, mouse_pos):
        button_clicked = self.menu_button.rect.collidepoint(mouse_pos)
        if button_clicked and self.ai_game.game_state == "Restart":
            print("Pressed Menu!")
            self.ai_game.game_state = "Start"
            print("State: Start      Source: Menu")
            #sys.exit()
    
    def check_quit_button(self, mouse_pos):
        button_clicked = self.quit_button.rect.collidepoint(mouse_pos)
        if button_clicked and self.ai_game.game_state == "Start":
            print("Pressed Quit!")
            sys.exit()

    def _check_keydown_events(self, event):
        key = event.key
        if key in Event.di.keys():
            self.ship.v += self.settings.ship_speed * Event.di[key]
        elif event.key == pg.K_SPACE:
            self.ship.open_fire()
        elif event.type == pg.KEYUP:
            if event.key in Event.di.keys():
                self.ship.v = Vector()
            elif event.key == pg.K_SPACE:
                self.ship.cease_fire()

    def _check_keyup_events(self, event):
        if event.key in Event.di.keys():
            self.ship.v = Vector()
        elif event.key == pg.K_SPACE:
            self.ship.cease_fire()

 
