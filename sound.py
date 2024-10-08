import pygame as pg 
import time
from random import randint


class Sound:
    def __init__(self): 
        self.pickup = pg.mixer.Sound('sounds/pickup.wav')
        self.gameover = pg.mixer.Sound('sounds/gameover.wav')

        self.ah = pg.mixer.Sound('sounds/Death_Sounds/ah.mp3')
        self.aliendeath = pg.mixer.Sound('sounds/Death_Sounds/aliendeath.mp3')
        self.cutitout = pg.mixer.Sound('sounds/Death_Sounds/cutitout.mp3')
        self.darnit = pg.mixer.Sound('sounds/Death_Sounds/darn.mp3')
        self.hey = pg.mixer.Sound('sounds/Death_Sounds/hey.mp3')
        self.nothappy = pg.mixer.Sound('sounds/Death_Sounds/nothappy.mp3')
        self.ooh = pg.mixer.Sound('sounds/Death_Sounds/ooh.mp3')
        self.ow = pg.mixer.Sound('sounds/Death_Sounds/ow.mp3')
        self.owww = pg.mixer.Sound('sounds/Death_Sounds/owwww.mp3')
        self.stop = pg.mixer.Sound('sounds/Death_Sounds/stop.mp3')
        self.wilhelm = pg.mixer.Sound('sounds/Death_Sounds/wilhelm.mp3')
        self.yeouch = pg.mixer.Sound('sounds/Death_Sounds/yeouch.mp3')
        self.hover = pg.mixer.Sound('sounds/UFO-hover.mp3')

        pg.mixer.music.load('sounds/ride_of_the_valkyries.mp3')
        pg.mixer.music.set_volume(0.1)
        

        
                                             
    def play_background(self): 
        pg.mixer.music.play(-1, 0.0)
        self.music_playing = True
        
    def play_pickup(self): 
        if self.music_playing: self.pickup.play()

    def play_ufo(self):
        self.hover.play()
    
    def play_deathsound(self):
        randline = randint(1,1000)
        
        if 1<= randline <= 550:
            pass
        elif 551 <= randline <=600 :
            self.ah.play()
        elif 601 <= randline <=650 :
            self.ow.play()
        elif 651 <= randline <= 700:
            self.ooh.play()
        elif 701 <= randline <= 750:
            self.hey.play()
        elif 751 <= randline <= 800:
            self.yeouch.play()
        elif 801 <= randline <= 850:
            self.owww.play()
        elif 851 <= randline <= 880:
            self.cutitout.play()
        elif 881 <= randline <=920 :
            self.stop.play()
        elif 921 <= randline <=970 :
            self.darnit.play()
        elif 971 <= randline <=990 :
            self.nothappy.play()
        elif 991 <= randline <= 995:
            self.aliendeath.play()
        elif 996 <= randline <= 1000:
            self.wilhelm.play()
        
    def play_gameover(self):
        if self.music_playing: 
            self.stop_background()
            self.gameover.play()
            time.sleep(3.0)       # sleep until game over sound has finished
        
    def toggle_background(self):
        if self.music_playing: 
            self.stop_background()
        else:
            self.play_background()
        self.music_playing = not self.music_playing
        
    def stop_background(self): 
        pg.mixer.music.stop()
        self.music_playing = False 
    
        
    
    
