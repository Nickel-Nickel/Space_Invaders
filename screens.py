import pygame.font
from button import Button
import pygame as pg
from colors import WHITE, GREEN

class Screens:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.highscores = ai_game.highscores

        self.screen_centerX = self.screen_rect.center[0]
        self.screen_centerY = self.screen_rect.center[1]

        self.play_button = Button(self, "Play", self.screen_centerY + 125)
        self.highscores_button = Button(self, "Highscores", self.screen_centerY + 175)
        self.menu_button = Button(self, "Menu", self.screen_centerY + 40)
        self.quit_button = Button(self, "Exit", self.screen_centerY + 225)

        self.alien1 = pg.image.load("images/alien-1a.png")
        self.alien2 = pg.image.load("images/alien-2a.png")
        self.alien3 = pg.image.load("images/alien-3a.png")
        self.ufo = pg.image.load("images/ufo.png")
        self.font = pg.font.SysFont(None, 48)
        self.spacefont = pg.font.SysFont(None, 150)
        self.invadersfont = pg.font.SysFont(None, 70)

        self.space = self.spacefont.render("SPACE", True, WHITE)
        self.invaders = self.invadersfont.render("INVADERS", True, GREEN)

        self.space_rect = self.space.get_rect()
        self.invaders_rect = self.invaders.get_rect()
        
        self.space_rect.x = self.screen_centerX - (self.space_rect.width/2)
        self.space_rect.y = self.screen_centerY - 300
        self.invaders_rect.x = self.screen_centerX- (self.invaders_rect.width/2)
        self.invaders_rect.y = self.screen_centerY - 210

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
        self.draw(self.alien1,self.screen_centerX,self.screen_centerY-100, "= 10 PTS")
        self.draw(self.alien2,self.screen_centerX,self.screen_centerY-50, "= 20 PTS")
        self.draw(self.alien3,self.screen_centerX,self.screen_centerY, "= 40 PTS")
        self.draw(self.ufo,self.screen_centerX,self.screen_centerY+50, "= ???")

        self.screen.blit(self.space, self.space_rect)
        self.screen.blit(self.invaders, self.invaders_rect)

    def display_start(self):
        self.play_button.reset_message("Play")
        self.play_button.reset_pos(self.screen_centerX,self.screen_centerY+125)
        self.draw_all()
        self.play_button.draw_button()
        self.highscores_button.draw_button()
        self.quit_button.draw_button()
    
    def display_restart(self):
        self.play_button.reset_message("Play Again")
        self.play_button.reset_pos(self.screen_centerX,self.screen_centerY-40)
        self.menu_button.reset_message("Menu")
        self.menu_button.reset_pos(self.screen_centerX,self.screen_centerY+40)

        self.play_button.draw_button()
        self.menu_button.draw_button()
        pg.display.flip()

    def display_highscores(self):
        self.menu_button.reset_message("< Back")
        self.menu_button.reset_pos(self.screen_centerX-400,self.screen_centerY-300)

        self.highscores.display()
        self.menu_button.draw_button()