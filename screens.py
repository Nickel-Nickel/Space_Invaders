import pygame.font
from button import Button
import pygame as pg
from colors import WHITE

class Screens:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.screen_centerX = self.screen_rect.center[0]
        self.screen_centerY = self.screen_rect.center[1]

        self.play_button = Button(self, "Play", self.screen_centerY + 100)
        self.highscores_button = Button(self, "Highscores", self.screen_centerY + 175)
        self.menu_button = Button(self, "Menu", self.screen_centerY + 40)
        self.quit_button = Button(self, "Exit", self.screen_centerY + 250)

        self.alien1 = pg.image.load("images/alien-1a.png")
        self.alien2 = pg.image.load("images/alien-2a.png")
        self.alien3 = pg.image.load("images/alien-3a.png")
        self.ufo = pg.image.load("images/ufo.png")
        self.font = pg.font.SysFont(None, 48)
        
    def draw(self,image,x,y, text):
        pic_rect = image.get_rect()
        textbox = self.font.render(text, True, WHITE)
        text_rect = textbox.get_rect()
        
        pic_rect.x = x - (pic_rect.width/2) - (text_rect.width/2)
        pic_rect.y = y - (pic_rect.height/2)

        text_rect.x = x - (text_rect.width/2 )+ (pic_rect.width/2)
        text_rect.y = y - (text_rect.height/2)

        self.screen.blit(image, pic_rect)
        self.screen.blit(textbox, text_rect)
    
    def draw_all(self):
        self.draw(self.alien1,self.screen_centerX,self.screen_centerY-175, "= 10 PTS")
        self.draw(self.alien2,self.screen_centerX,self.screen_centerY-125, "= 20 PTS")
        self.draw(self.alien3,self.screen_centerX,self.screen_centerY-75, "= 40 PTS")
        self.draw(self.ufo,self.screen_centerX,self.screen_centerY-25, "= ???")

    def display_start(self):
        self.play_button.reset_message("Play")
        self.play_button.reset_height(self.screen_centerY+100)
        self.draw_all()
        self.play_button.draw_button()
        self.highscores_button.draw_button()
        self.quit_button.draw_button()
    
    def display_restart(self):
        self.play_button.reset_message("Play Again")
        self.play_button.reset_height(self.screen_centerY-40)

        self.play_button.draw_button()
        self.menu_button.draw_button()